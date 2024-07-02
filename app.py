from flask import Flask, request, jsonify
import requests
import os
# from dotenv import load_dotenv
# load_dotenv()

ip_info = os.getenv('IPINFO_API_KEY')
weather_key = os.getenv('WEATHER_API_KEY')
# print(ip_info)

app = Flask(__name__)


# Get client IP address
# def get_client_ip():
#     if request.headers.getlist("X-Forwarded-For"):
#         ip = request.headers.getlist("X-Forwarded-For")[0]
#     else:
#         ip = request.remote_addr
#     return ip


def get_client_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

# #get location
def get_location(ip):
    # response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={ip_info}&ip={ip}')
    response = requests.get(f"https://ipinfo.io/{ip}?token={ip_info}")
    return response.json()


# # get weather information
def get_weather(lat, lon):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={weather_key}")
    return response.json()


@app.route('/api/hello', methods=['GET'])
def greet():
    # return ip_info
    # visitor_name = request.args.get('visitor_name', default='Guest')
    # client_ip = get_client_ip()
    # # ip = '1.1.1.1'
    # location = get_location(client_ip)
    return jsonify({'ip_env': ip_info})

    # if 'loc' in location:
    #     lat, lon = location['loc'].split(',')
    #     # lat = location['latitude']
    #     # lon = location['longitude']
    #     city = location['city']
    #     # region = location['region']
    #     # country = location['country']
        
    #     weather = get_weather(lat, lon)
    #     if 'cod' in weather and weather['cod'] == 200:
    #         temperature = weather['main']['temp']
    #         response = {
    #                     "client_ip": f'{client_ip}',
    #                     "location": f'{city}',
    #                     "greeting": f'Hello, {visitor_name}!, the temperature is {temperature} degrees celsius in {city}'}
    #     else:
    #         response = {"error": 'could not retrieve temperature data'}
    # else:
    #     response = {"error": 'Could not retrieve location',
    #                 "return_location": f'{location}',
    #                 "client_ip": f'{client_ip}'}
    # return jsonify(response)

    
 

if __name__ == '__main__':
#     # run_with_ngrok(app)
    app.run(debug=True)