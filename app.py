import os
import requests
from flask import (Flask, render_template, request)


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["WEATHER_API_KEY"] = os.environ.get("WEATHER_API_KEY")
app.config["MAPS_API_KEY"] = os.environ.get("MAPS_API_KEY")
weather_api_key = os.environ.get("WEATHER_API_KEY")
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
@app.route("/weather")
def weather():
    """
    App route to show weather application and pass environment variables
    """
    api_key = os.environ.get("MAPS_API_KEY")
    weather_key = os.environ.get("WEATHER_API_KEY")
    return render_template('weather.html',
                           api_key=api_key,
                           weather_key=weather_key)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
