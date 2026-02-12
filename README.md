# Weather-API-Pipeline

A scalable **ETL (Extract-Transform-Load) pipeline** that ingests
weather data from a public Weather API, processes it, stores it in
PostgreSQL, and provides utilities for analysis. Designed with
automation and portability in mind using Docker and Apache Airflow.

## 🧠 Overview

This project demonstrates:

-   Automated retrieval of weather data from a Weather API\
-   Transformation of API data into a structured format\
-   Loading into a PostgreSQL database\
-   Workflow orchestration using Apache Airflow\
-   Post-processing and analysis using Python

## 🚀 Features

-   📡 Weather API Integration\
-   🔄 ETL Pipelines with Airflow\
-   🐘 PostgreSQL Storage Layer\
-   🐳 Dockerized Infrastructure\
-   📊 Data Analysis Script

## 📦 Project Structure
```
Weather-API-Pipeline/
│
├── dags/ # Airflow DAG definitions
├── postgres/ # PostgreSQL init scripts
├── weather_data_analyzer.py # Data analysis utility
├── docker-compose.yaml # Docker stack (Airflow + Postgres)
├── README.md # Documentation
```
## 📥 Getting Started

### Prerequisites

-   Docker & Docker Compose\
-   Python 3.8+\
-   Weather API Key (e.g. Weatherstack, OpenWeather, etc.)

### Clone the repository

git clone https://github.com/MatheusSabaudo/Weather-API-Pipeline.git\
cd Weather-API-Pipeline

### Environment configuration

Create a .env file:

WEATHER_API_KEY=your_api_key_here\
POSTGRES_USER=weather_user\
POSTGRES_PASSWORD=weather_password\
POSTGRES_DB=weather_db

### Start the pipeline

docker-compose up -d

### Access Airflow

http://localhost:8080

## ⚙️ ETL Flow

1.  Extract → Weather data pulled from API\
2.  Transform → JSON normalization & cleaning\
3.  Load → Data stored in PostgreSQL\
4.  Analyze → Python analysis layer

## 🗄️ Example Database Schema

CREATE TABLE weather_data ( id SERIAL PRIMARY KEY, location TEXT,
timestamp TIMESTAMP, temperature FLOAT, humidity FLOAT, pressure FLOAT,
wind_speed FLOAT, weather_description TEXT );

## 📊 Data Analysis

python weather_data_analyzer.py

## 🎯 Project Goal

This project is designed to demonstrate real-world Data Engineering
skills: - Pipeline architecture\
- Workflow orchestration\
- Data modeling\
- Containerization\
- Automation\
- Scalable design patterns

## 📄 License

MIT License
