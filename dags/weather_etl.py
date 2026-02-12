import psycopg2
from tabulate import tabulate
from datetime import datetime

class WeatherDataAnalyzer:
    def __init__(self):
        self.connection_params = {
            "dbname": "airflow",
            "user": "airflow",
            "password": "airflow",
            "host": "localhost",
            "port": "5432"
        }
    
    def connect(self):
        return psycopg2.connect(**self.connection_params)
    
    def get_city_statistics(self):
        """Get statistics for each city"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # SOLO CAMBIA city -> location
        cursor.execute("""
            SELECT 
                location,
                COUNT(*) as total_readings,
                AVG(temperature)::numeric(10,2) as avg_temp,
                MIN(temperature) as min_temp,
                MAX(temperature) as max_temp,
                AVG(humidity)::numeric(10,2) as avg_humidity,
                AVG(wind_speed)::numeric(10,2) as avg_wind_speed,
                MAX(timestamp) as latest_reading
            FROM weather_data 
            GROUP BY location
            ORDER BY location
        """)
        
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    def display_statistics(self):
        """Display only city statistics table"""
        stats = self.get_city_statistics()
        
        if stats:
            headers = ['City', 'Readings', 'Avg Temp (°C)', 'Min Temp', 'Max Temp', 'Avg Humidity (%)', 'Avg Wind (km/h)', 'Latest Reading']
            formatted_stats = []
            for row in stats:
                formatted_row = list(row)
                if isinstance(formatted_row[7], datetime):
                    formatted_row[7] = formatted_row[7].strftime('%Y-%m-%d %H:%M:%S')
                formatted_stats.append(formatted_row)
            
            print("\n=== WEATHER STATISTICS BY CITY ===\n")
            print(tabulate(formatted_stats, headers=headers, tablefmt='grid'))
        else:
            print("No statistics available")

if __name__ == "__main__":
    analyzer = WeatherDataAnalyzer()
    analyzer.display_statistics()