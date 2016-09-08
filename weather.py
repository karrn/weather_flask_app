import os
from dotenv import load_dotenv, find_dotenv
import forecastio
from geopy.geocoders import Nominatim

load_dotenv(find_dotenv())

api_key = os.environ['WEATHER_API_KEY']
loc = {}
#address = "San Francisco"

def show_weather():
	address = input("Enter your location to get the weather: ")
	return get_weather(address)


def get_weather(address):
	location(address)
	forecast = forecastio.load_forecast(api_key, loc['lat'], loc['lng']).currently()
	return "{} and {}˚ in {}".format(forecast.summary, forecast.temperature, address)
	
def location(address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	loc['lat'] = location.latitude
	loc['lng'] = location.longitude

#address = input("Enter your location to get the weather: ")
#print(address)


#print(show_weather())