from flask import Blueprint,jsonify, current_app
import requests 

bp = Blueprint('weather', __name__)

@bp.route('/weather/<city>', methods=('GET',))
@bp.route('/weather/<city>/', methods=('GET',))
def getWeather(city):
    config = current_app.config
    request_url = config['OW_ENDPOINT_URL'] + "&q=" + city
    r = requests.get(request_url)
    return r.json()
