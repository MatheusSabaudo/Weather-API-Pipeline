from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2
import os

API_KEY = os.getenv("WEATHERSTACK_API_KEY", "INSERT_YOUR_API_KEY")
CITIES = ["Turin"]

def create_table():
    conn = psycopg2.connect(
        dbname="airflow",  # Match your docker-compose
        user="airflow",
        password="airflow",
        host="postgres"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            temperature FLOAT,
            humidity INT,
            wind_speed INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_weather():
    results = []
    for city in CITIES:
        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
        response = requests.get(url).json()
        
        # Add error handling for API failures
        if "error" in response:
            print(f"API Error for {city}: {response['error']['info']}")
            continue
            
        data = {
            "city": city,
            "temperature": response['current']['temperature'],
            "humidity": response['current']['humidity'],
            "wind_speed": response['current']['wind_speed']
        }
        results.append(data)
    return results

def insert_weather():
    conn = psycopg2.connect(
        dbname="airflow",  # Match your docker-compose
        user="airflow",
        password="airflow",
        host="postgres"
    )
    cursor = conn.cursor()
    weather_data = fetch_weather()
    for data in weather_data:
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, humidity, wind_speed)
            VALUES (%s, %s, %s, %s)
        """, (data['city'], data['temperature'], data['humidity'], data['wind_speed']))
    conn.commit()
    cursor.close()
    conn.close()

with DAG(
    'weather_etl',
    start_date=datetime(2026, 2, 12),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    create_table_task = PythonOperator(
        task_id='create_table',
        python_callable=create_table
    )
    
    load_weather = PythonOperator(
        task_id='load_weather',
        python_callable=insert_weather
    )
    
    create_table_task >> load_weather