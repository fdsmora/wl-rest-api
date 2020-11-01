from flask import Blueprint,jsonify
import requests 

bp = Blueprint('weather', __name__)

openWeatherAPIKey = '8cb95285a2549c48dfc603cb7bf9e81d'
weatherEndPointUrl = f'http://api.openweathermap.org/data/2.5/weather?APPID={openWeatherAPIKey}&q='

@bp.route('/hola', methods=('GET',))
def hola():
    return 'hola'

@bp.route('/weather/<city>', methods=('GET',))
@bp.route('/weather/<city>/', methods=('GET',))
def getWeather(city):
    r = requests.get(weatherEndPointUrl + city)
    return r.json()
