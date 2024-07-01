from flask import Flask, request, jsonify, send_from_directory
import requests
import streamlit as st


app = Flask(__name__)

IPINFO_API_KEY = '21523ec2a35b11'
WEATHER_API_KEY = '3f41f879b45466727784a5d1220d10d2'
clientip = '1.1.1.1'

# Get client IP address
def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

#get location
def get_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}?token={IPINFO_API_KEY}")
    return response.json()


# get weather information
def get_weather(lat, lon):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={WEATHER_API_KEY}")
    return response.json()


@app.route('/api/hello', methods=['GET'])
def greet():
    visitor_name = request.args.get('visitor_name', default='Guest')
    clientip = '1.1.1.1'
    # client_ip = get_client_ip()
    location = get_location(clientip)

    if 'loc' in location:
        lat, lon = location['loc'].split(',')
        city = location['city']
        region = location['region']
        country = location['country']
        response = {"client_ip": f'{clientip}',
                    "location": f'{city}',
                    "greeting": f'Hello, {visitor_name}'}
        
        weather = get_weather(lat, lon)
        if 'cod' in weather and weather['cod'] == 200:
            temperature = weather['main']['temp']
            response = {"client_ip": f'{clientip}',
                    "location": f'{city}',
                    "greeting": f'Hello, {visitor_name}!, the temperature is {temperature}'}
        else:
            response = {"error": 'could not retrieve temperature data'}
    else:
        response = {"error": 'Could not retrieve location'}
    return jsonify(response)

    # return jsonify({"client_ip": f'{client_ip}',
    #                 "location": f'{city}',
    #                 "greeting": f'Hello, {visitor_name}'})

def main():
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)