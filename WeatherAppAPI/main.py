import os
import requests
import json
import pyttsx3

# Using pyttsx3 to convert text to speech
engine = pyttsx3.init()
engine.say("Hi. Welcome to the Weather App Robot. I'll find out the weather of any city you want me to!! To get started enter the name of the city you want to know about")
engine.runAndWait()

while True:
    city = input('Enter the name of the city you wish to find out (type "exit" to quit):\n')

    if city.lower() == 'exit':
        break

    url = f"https://api.weatherapi.com/v1/current.json?key=4a03ea2cdd62423bbd2200602231111&q={city}"

    r = requests.get(url)

    # Check if the request was successful (status code 200)
    if r.status_code == 200:
        weather_data = json.loads(r.text)

        # Extract temperature from the response
        temperature_celsius = weather_data["current"]["temp_c"]
        temperature_feelslike = weather_data["current"]["feelslike_c"]
        temperature_condition = weather_data["current"]["condition"]["text"]

        print(f"The current weather in {city} is {temperature_celsius} degrees Celsius.And it feels like {temperature_feelslike} degree celcius. And the weather outside is of  {temperature_condition}")

        # Using pyttsx3 to convert text to speech
        engine.say(f"The current weather in {city} is {temperature_celsius} degrees Celsius. And it feels like {temperature_feelslike} degree celcius.  And the weather outside is of {temperature_condition}")
        engine.runAndWait()

        # Ask if the user wants to find the weather of a new city
        engine.say("Can I help you find the weather of a new city?")
        engine.runAndWait()
    else:
        engine.say("Sorry.. Looks like you entered a wrong city name! Please check the spellings and give me a proper city name")
        engine.runAndWait()

# Optionally, you can add a goodbye message
engine.say("Goodbye! Thanks for using the Weather App Robot. Check out my GitHub for more interesting projects")
engine.runAndWait()
