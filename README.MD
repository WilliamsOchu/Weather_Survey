# Weather_Survey
### Retrieve Weather details of cities Worldwide 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Weather Survey is a python suite developed to help retrieve accurate weather statistics of cities worldwide.
This suite uses an API from openweathermap.org to comprehensively track and monitor weather statistics of cities around the globe. 
With this tool we can retrieve accurate weather details of a city at a particular timestamp or we can fetch an average forcast over the span of five(5) days.
The use of this script provides the user with weather details such as temperature, humidity, pressure, wind speed and also predictions of rain and clear sky.

## Contents of this Suite
- weather_check_instant.py
- weather_check_lengthy.py
 
## Explaining the contents of the suite

##### weather_check_instant.py
This script returns a well formatted report showing the weather statistics of a desired city at a particular timestamp.
##### weather_check_lengthy.py
This script returns an average weather forecast of any desired city over a period of five days.

## How to use 
#### <ins>Weather_check_instant.py</ins>
Run the script while passing the name of the desired city as a system argument on the shell. An example is illustrated below,<br>
./weather_check_instant.py torino <br>
./weather_check_instant.py london

#### <ins>Weather_check_lengthy.py</ins> 
Run the script while passing the name of the desired city as a system argument on the shell. An example is illustrated below, <br>
./weather_check_lenghty.py seville <br>
./weather_check_lenghty.py sydney

## Python Techniques Employed
- Use of openweathermap.org free tier API
- Extracting exact date and timestamp from python datetime module
- Fetching data from json
- Retrieving data from an API using python requests library

I will continue to modify this script as time goes on
This work of mine is open source, feel free to make changs and commits if you deem it fit 
Work hard, Have fun and Make history