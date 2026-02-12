CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    observation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
