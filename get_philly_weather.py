import requests
import os
from datetime import datetime

def get_philly_weather():
    # You'll need to sign up for a free API key at https://openweathermap.org/api
    #api_key = os.environ.get('OPENWEATHER_API_KEY')
    api_key = '46f14555bfea703c815480f7a0322262'
    if not api_key:
        raise ValueError("OpenWeather API key not found in environment variables")

    # Philadelphia coordinates
    lat = "39.9526"
    lon = "-75.1652"
    
    # API endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        report = (
            f"Philadelphia Weather Report ({timestamp})\n"
            f"Temperature: {temp}°F\n"
            f"Feels like: {feels_like}°F\n"
            f"Conditions: {description}"
        )
        
        # Write to a report file
        with open('weather_report.txt', 'w') as f:
            f.write(report)
            
        print(report)
        return True
        
    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")
        return False

if __name__ == "__main__":
    get_philly_weather() 
    