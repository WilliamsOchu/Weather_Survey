#!/usr/bin/env python3 

## This program will help forecast weather over a period of 5 days 

## Lets start by importing the necessary modules 

import json, requests, sys, datetime
import secret_configs

## Lets get the city name from the sys argv 1 variable 
city_name = sys.argv[1]

## Lets denote our API_url and our API_key
API_url = "https://api.openweathermap.org/data/2.5/forecast?q="



## Lets get our API to retrieve wether details from the openweathermap API
weather_API = API_url + city_name + "&appid=" + secret_configs.api_key + "&units=metric"

## Lets pull the data from the Weather_API and save it as json

weather_bulk = requests.get(weather_API)

weather_details = weather_bulk.json()

## Function to keep printing out details 
def print_weather_details():
    print('Average Temperature: {}°C'.format(temps))
    print('Average Humidity: {} g.m-3'.format(humidity))
    print('Average Pressure: {} millibars'.format(pressure))
    print('Average Wind Speed: {} km/h'.format(wind_speed))
    print('Weather Description: {}'.format(weather_report.title()))
    print('\n\033[1m{:-^30}\033[0m'.format('-'))
 
print('\033[1m{:-^30}\033[0m'.format(city_name.title()))
## To get weather details for 5 days

## Day 1
time_now = datetime.datetime.fromtimestamp(weather_details['list'][0]['dt'])
print('Estimated Weather Details for: {}'.format(time_now))
temps = weather_details['list'][0]['main']['temp']
humidity = weather_details['list'][0]['main']['humidity']
pressure = weather_details['list'][0]['main']['pressure']
wind_speed = weather_details['list'][0]['wind']['speed']
weather_report = weather_details['list'][0]['weather'][0]['description']
## Print out and format the details
print_weather_details()

## Day 2
time_now = datetime.datetime.fromtimestamp(weather_details['list'][8]['dt'])
print('Estimated Weather Details for: {}'.format(time_now))
temps = weather_details['list'][8]['main']['temp']
humidity = weather_details['list'][8]['main']['humidity']
pressure = weather_details['list'][8]['main']['pressure']
wind_speed = weather_details['list'][8]['wind']['speed']
weather_report = weather_details['list'][8]['weather'][0]['description']
print_weather_details()

## Day 3 
time_now = datetime.datetime.fromtimestamp(weather_details['list'][16]['dt'])
print('Estimated Weather Details for: {}'.format(time_now))
temps = weather_details['list'][16]['main']['temp']
humidity = weather_details['list'][16]['main']['humidity']
pressure = weather_details['list'][16]['main']['pressure']
wind_speed = weather_details['list'][16]['wind']['speed']
weather_report = weather_details['list'][16]['weather'][0]['description']
print_weather_details()

## Day 4
time_now = datetime.datetime.fromtimestamp(weather_details['list'][24]['dt'])
print('Estimated Weather Details for: {}'.format(time_now))
temps = weather_details['list'][24]['main']['temp']
humidity = weather_details['list'][24]['main']['humidity']
pressure = weather_details['list'][24]['main']['pressure']
wind_speed = weather_details['list'][24]['wind']['speed']
weather_report = weather_details['list'][24]['weather'][0]['description']
print_weather_details()

## Day 5
time_now = datetime.datetime.fromtimestamp(weather_details['list'][32]['dt'])
print('Estimated Weather Details for: {}'.format(time_now))
temps = weather_details['list'][32]['main']['temp']
humidity = weather_details['list'][32]['main']['humidity']
pressure = weather_details['list'][32]['main']['pressure']
wind_speed = weather_details['list'][32]['wind']['speed']
weather_report = weather_details['list'][32]['weather'][0]['description']
print_weather_details()