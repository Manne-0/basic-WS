from flask import request
import requests
import os
from dotenv import load_dotenv
load_dotenv()

ip_info = os.getenv('IPINFO_API_KEY')
weather_key = os.getenv('WEATHER_API_KEY')


def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip



#get location
def get_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}?token={ip_info}")
    return response.json()


# get weather information
def get_weather(lat, lon):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={weather_key}")
    return response.json()