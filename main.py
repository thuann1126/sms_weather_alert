import requests
from tkinter import*
import os
from twilio.rest import Client
import datetime
from dotenv import load_dotenv # this package use for take env
load_dotenv()


#-------Properties---------
WEATHER_KEY = os.getenv('WEATHER_KEY')
LOCATION_LAT = 10.352900
LOCATION_LON = 106.363213
URL = "https://api.openweathermap.org/data/2.5/onecall"

condition_colection = {
    "Rain": [],
    "Clouds": [],
    "Snow": [],
    "Sun": [],
    "unknown":[]
}

parameters = {
    "lat" : LOCATION_LAT,
    "lon" : LOCATION_LON,
    "appid" : WEATHER_KEY
}

#----------SET UP Environment variables
# Use your own twilio account id and token
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
print(WEATHER_KEY)
print(account_sid)
print(auth_token)

client = Client(account_sid, auth_token)

# get weather data
data = requests.get(URL, params=parameters).json()

# Check the weather in the next 5 hours
for i in range(0, 5):
    weather_condition = data["hourly"][i]["weather"][0]["main"]
    if weather_condition == "Rain":
        condition_colection["Rain"].append(i)
    elif weather_condition == "Clouds":
        condition_colection["Clouds"].append(i)
    elif weather_condition == "Sun":
        condition_colection["Sun"].append(i)
    elif weather_condition == "Snow":
        condition_colection["Snow"].append(i)
    else:
        condition_colection["unknown"].append(i)

# use your twilio number
if len(condition_colection["Rain"]) > 0:
    print("It's gonna be rainy in the next 5 hours, please bring the rain cover")
    message = client.messages \
        .create(
        body="It's gonna be rainy in the next 5 hours, please bring the rain cover",
        from_=os.getenv('SENDER_NUMBER'),
        to=os.getenv('RECEIVER_NUMBER')
    )
if len(condition_colection["Clouds"]) > 0:
    print(f"It's gonna be cloudy in the next 5 hours, cool weather, good to play")
    message = client.messages.create(
        body="It's gonna be cloudy in the next 5 hours, cool weather, good to play",
        from_=os.getenv('SENDER_NUMBER'),
        to=os.getenv('RECEIVER_NUMBER')
    )
if len(condition_colection["Snow"]) > 0:
    print("It's gonna be snowy in the next 5 hours, please wear warm")
    message = client.messages \
        .create(
        body="It's gonna be snowy in the next 5 hours, please wear warm",
        from_=os.getenv('SENDER_NUMBER'),
        to=os.getenv('RECEIVER_NUMBER')
    )
if len(condition_colection["Sun"]) > 0:
    print(f"It's gonna be sunny in the next 5 hours, best time for going outside")
    message = client.messages \
        .create(
        body="It's gonna be sunny in the next 5 hours, best time for going outside",
        from_=os.getenv('SENDER_NUMBER'),
        to=os.getenv('RECEIVER_NUMBER')
    )
print(message.status)




