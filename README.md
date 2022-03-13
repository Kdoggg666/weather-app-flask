# Weather App

Welcome to my weather application.  
  
A live preview of the web app can be found [Here](https://weather-app-flask-kenan.herokuapp.com/) 

## Table of Contents

1. [Brief](#brief)

2. [Features](#features)

3. [Technologies Used](#technologies)

4. [Testing](#testing)

5. [Disclaimer](#disclaimer)

<a name="brief"></a> 

### Project Brief
- The client has requested a minimal app as part of their website displaying the weather in the users current location. The site is mostly visited on mobile, but should work on any device.

### Requirements

- Check for the user location
- Request the current weather based on the location from any freely available source
- Show the current weather to the user

<a name="features"></a>
## Features

- The site is a simple one page application which gets the users location from the browser, makes a call to the Google Maps api to resolve the coordinates to a city name and pushes the coordinates in an api call to the visual crossing weather api. Once the data is returned in json format the app provied the user with local weather data. 

![Weather page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1647111497/weather-app_xk8lzt.png "Weather(Home) Page")


<a name="technologies"></a>
## Technologies Used

- **Flask** - Used as web app framework to make creating the app faster and easier.   
- **Heroku** - Heroku was used to host the live version of this app.  
- **Github** - Github was used for storing my code and version control.    
- **Gitpod** - I used Gitpod to code the site as well as push updates to Github.    
- **Python** - Python 3 was used for the backend code to run the app and logic.    
- **HTML5** - The core of the site was built with HTML version 5.  
- **CSS** - CSS was used to style the website and define fonts and layout.  
- **JavaScript** - JavaScript was used to provide logic and funtionality.
- **Jquery** - Jquery was used to simplify some vanilla JS functions.
- **Google Chrome** - The website was built and tested in google Chrome.    
- **Cloudinary** - Hosting images to make the site load faster.  
- **Apple Safari** - Used for testing.  
- **Mozilla Firefox** - Used for testing.  
- **Opera** - Used for testing.  
- **Skycons** - Used for the weather icons.
- **Google Maps API** - Used to resolve coordinates into a city name.
- **Visual Crossing Weather API** - Used to get weather data for current location. 


<a name="testing"></a>
## Testing and Troubleshooting

Initially I planned to make this only using the front-end, I soon found that it was almost impossible to hide the api keys in an environment variable. I then decided to use flask as its quick and doesn't take much code to start a project. 

I was trying to resolve the location and make the API call on the server side. I ran into problems here as geolocation in python is limited to ip based and this was wildly inaccurate as well as only providing the server location and not the users location. I solved this by using JS in the front end to do the geolocation and the api calls. Using Jinja templates I was able to pass the api keys to the front-end without exposing them in version control or the live site. 

I tested the site on various resolution screens, various mobile phones as well as chrome devtools to check responsiveness.

## Code Validation

- HTML passed validation with no errors on [The W3 Nu HTML Checker](https://validator.w3.org/)
- CSS passed validation with CSS level 3 + SVG on [The W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fweather-app-flask-kenan.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=)
- JS showed no errors using jshint.

<a name="disclaimer"></a>
## Disclaimer
This project is for educational purposes only and will not be used for commercial use. All media has been credited and any similarities to other companies/websites/applications are purely unintentional.  