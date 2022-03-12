import os
import requests
from flask import (
                   Flask, flash, render_template,
                   redirect, request, session, url_for)
from geopy.geocoders import Nominatim
import geocoder


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["WEATHER_API_KEY"] = os.environ.get("WEATHER_API_KEY")
app.config["MAPS_API_KEY"] = os.environ.get("MAPS_API_KEY")
weather_api_key = os.environ.get("WEATHER_API_KEY")


def get_weather_results(city, api_key):
    """
    Api call to openweather
    """
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    r = requests.get(api_url)
    print(r.json())
    return r.json()



@app.route("/")
@app.route("/weather")
def recipes():
    """
    App route to show weather application
    """
    
    g = geocoder.ip('me')
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
    return render_template('weather.html',
                           my_location=my_location,
                           locname=locname,
                           city=city,
                           country=country,
                           temp=temp,
                           region=region)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
