from flask import Flask, request, jsonify
import config
import requests


app = Flask(__name__)


# Get client IP address
# def get_client_ip():
#     if request.headers.getlist("X-Forwarded-For"):
#         ip = request.headers.getlist("X-Forwarded-For")[0]
#     else:
#         ip = request.remote_addr
#     return ip

# #get location
# def get_location(ip):
#     response = requests.get(f"https://ipinfo.io/{ip}?token={config.IPINFO_API_KEY}")
#     return response.json()


# # get weather information
# def get_weather(lat, lon):
#     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={config.WEATHER_API_KEY}")
#     return response.json()


@app.route('/')  #('/api/hello', methods=['GET'])
def greet():
    return "Hello MF!"
    # visitor_name = request.args.get('visitor_name', default='Guest')
    # # clientip = '1.1.1.1'
    # client_ip = get_client_ip()
    # location = get_location(client_ip)

    # if 'loc' in location:
    #     lat, lon = location['loc'].split(',')
    #     city = location['city']
    #     region = location['region']
    #     country = location['country']git
        
    #     weather = get_weather(lat, lon)
    #     if 'cod' in weather and weather['cod'] == 200:
    #         temperature = weather['main']['temp']
    #         response = {
    #                     'client_ip': f'{client_ip}',
    #                     'location': f'{city}',
    #                     'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees celsius in {city}'}
    #     else:
    #         response = {"error": 'could not retrieve temperature data'}
    # else:
    #     response = {"error": 'Could not retrieve location'}
    # return jsonify(response)

    
 

if __name__ == '__main__':
    # run_with_ngrok(app)
    app.run()