import os
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


@app.route("/")
@app.route("/weather")
def recipes():
    """
    App route to show weather application
    """
    g = geocoder.ip('me')
    # print(g.latlng)
    cur_lat = g.latlng[0]
    cur_lng = g.latlng[1]
    # print(g.latlng[1])
    geo_loc = Nominatim(user_agent="GetLoc")
    locname = geo_loc.reverse(f'{cur_lat}, {cur_lng}', language='en', addressdetails=True)
    print(locname)
    print(f'{cur_lat}, {cur_lng}')
    my_location = locname.address
    loc_dict = g.raw
    print(loc_dict['city'])
    city = loc_dict['city']
    country = loc_dict['country']
    region = loc_dict['region']
    return render_template('weather.html', 
                           my_location=my_location, 
                           locname=locname,
                           city=city,
                           country=country,
                           region=region)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
