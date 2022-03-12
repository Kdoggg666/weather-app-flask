import os
import requests
from flask import (Flask, render_template, request)
from geopy.geocoders import Nominatim
import geocoder


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["WEATHER_API_KEY"] = os.environ.get("WEATHER_API_KEY")
app.config["MAPS_API_KEY"] = os.environ.get("MAPS_API_KEY")
weather_api_key = os.environ.get("WEATHER_API_KEY")
app.secret_key = os.environ.get("SECRET_KEY")


def get_weather_results(city, api_key):
    """
    Api call to openweather
    """
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    r = requests.get(api_url)
    return r.json()


@app.route("/")
@app.route("/weather")
def weather():
    """
    App route to show weather application
    """
    user_ip_adr = request.environ['REMOTE_ADDR']
    g = geocoder.ipinfo(f'{user_ip_adr}')
    print(type(user_ip_adr))
    cur_lat = g.latlng[0]
    cur_lng = g.latlng[1]
    geo_loc = Nominatim(user_agent="GetLoc")
    locname = geo_loc.reverse(f'{cur_lat}, {cur_lng}',
                              language='en',
                              addressdetails=True)
    print(locname)
    print(f'{cur_lat}, {cur_lng}')
    my_location = locname.address
    loc_dict = g.raw
    city = loc_dict['city']
    country = loc_dict['country']
    region = loc_dict['region']
    weather_data = get_weather_results('gothenburg', weather_api_key)
    temp = int(weather_data['main']['temp'])
    description = weather_data['weather'][0]['description']
    return render_template('weather.html',
                           my_location=my_location,
                           locname=locname,
                           city=city,
                           country=country,
                           temp=temp,
                           region=region,
                           description=description,
                           user_ip_adr=user_ip_adr)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
