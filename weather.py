import googlemaps
import requests
from datetime import datetime

# Use my own API key from Google Cloud Console
gmaps = googlemaps.Client(key = 'AIzaSyCtSI4crkEMG7oqly1D_Sqk8EjUaa-RlQ4')

location = input("Please enter the name of the location for which you would like to retrieve the weather:")

# Geocode the location to get the coordinates
geocode_results = gmaps.geocode(location)

if not geocode_results:
    print("Location not found")
else:
    location_results = geocode_results[0]['geometry']['location']
    lat = location_results['lat']
    long = location_results['lng']
    print(f"Coordinates of {location}: Latitude: {lat}, Longitude {long}")
    
# Weather API key from OpenWeatherMap.org
weather_api_key = "4c8510f0473cb053d8a235c5aea9974c"
weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={weather_api_key}&units=metric'

# Fetch the weather data
response = requests.get(weather_url)
weather_data = response.json()

if response.status_code != 200:
    print ("Failed to retrieve weather data.")
else:
    # Extract relevant weather information
    weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    # Print the weather information
    print(f"Weather in {location}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Wind_speed: {wind_speed}")