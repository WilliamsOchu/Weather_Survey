#!/usr/bin/env python3

## We will write a script to get instant weather details of a specific location

## Let us import the necessary libraries

import json, requests, sys, datetime, secret_configs

## This script will be run by appending the desired city name as a positional parameter when calling the script

city_name = sys.argv[1]

## Instantiate the API url. We are using openweathermap API endpoint

api_url = "https://api.openweathermap.org/data/2.5/weather?"


## Lets jam the url together to ge the weather details of a particular city

weather_url = api_url + "q=" + city_name + "&appid=" + secret_configs.api_key + "&units=metric"

## To obtain bulk weather details from the API
weather_bulk = requests.get(weather_url)
if weather_bulk.ok:
    weather_details = weather_bulk.json()
    
    ## To get exact timestamp
    to_time_now = weather_details['dt']
    time_now = datetime.datetime.fromtimestamp(to_time_now)

    ## To get the parameters we want to report 
    temps = weather_details['main']['temp']
    max_temps = weather_details['main']['temp_max']
    min_temps = weather_details['main']['temp_min']
    humidity = weather_details['main']['humidity']
    pressure = weather_details['main']['pressure']
    wind_speed = weather_details['wind']['speed']
    weather_report = weather_details['weather'][0]['main']
    weather_report_description = weather_details['weather'][0]['description']

    ## Genrate a well formatted report of the weather 
    print('\033[1m{:-^30}\033[0m'.format(city_name.title()))
    print('Last Curated: {}'.format(time_now))
    print('Average Temperature is: {}°C'.format(temps))
    print('Estimated Max Temps is: {}°C'.format(max_temps))
    print('Estimated Min Temps is: {}°C'.format(min_temps))
    print('Humidity is: {} g.m-3'.format(humidity))
    print('Pressure is: {} millibars'.format(pressure))
    print('Wind speed is: {} km/h\n'.format(wind_speed))
    print('Weather description: {}'.format(weather_report_description.title()))
    

else:
    print("Unable to pull Live Weather due to poor Network Connection")
    



