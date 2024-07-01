from flask import Flask, request, jsonify
import requests
import os

ip_info = os.getenv('IPINFO_API_KEY')
weather_key = os.getenv('WEATHER_API_KEY')

app = Flask(__name__)


# Get client IP address
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


@app.route('/')  #('/api/hello', methods=['GET'])
def greet():
    visitor_name = request.args.get('visitor_name', default='Guest')
    # clientip = '1.1.1.1'
    client_ip = get_client_ip()
    location = get_location(client_ip)

    if 'loc' in location:
        lat, lon = location['loc'].split(',')
        city = location['city']
        # region = location['region']
        # country = location['country']
        
        weather = get_weather(lat, lon)
        if 'cod' in weather and weather['cod'] == 200:
            temperature = weather['main']['temp']
            response = {
                        "client_ip": f'{client_ip}',
                        "location": f'{city}',
                        "greeting": f'Hello, {visitor_name}!, the temperature is {temperature} degrees celsius in {city}'}
        else:
            response = {"error": 'could not retrieve temperature data'}
    else:
        response = {"error": 'Could not retrieve location',
                    "return_location": f'{location}',
                    "client_ip": f'{client_ip}'}
    return jsonify(response)

    
 

if __name__ == '__main__':
    # run_with_ngrok(app)
    app.run()