from flask import Flask, request, jsonify
from packages import get_client_ip, get_location, get_weather

app = Flask(__name__)
app.json.sort_keys = False



@app.route('/api/hello', methods=['GET'])
def greet():
    visitor_name = request.args.get('visitor_name', default='Guest')
    client_ip = get_client_ip()
    location = get_location(client_ip)
    # return jsonify(client_ip, location)

    if 'loc' in location:
        lat, lon = location['loc'].split(',')
        city = location['city']
        
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
    app.run()