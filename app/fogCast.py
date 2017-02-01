#!/usr/bin/env python
import forecastio
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# import sys
# sys.path.insert(0, "home/gabeduke/windMailer/settings.py")
from settings import *

# fetching weather
forecast = forecastio.load_forecast(forecast_key, lat, lng)
by_day = forecast.daily()
by_hour = forecast.hourly()

fogTimes = []

for hourlyData in by_hour.data:
    diff = abs(hourlyData.dewPoint - hourlyData.temperature)
    if diff <= 10:
        fogTimes.append('Chance of fog on ' + '{:%a at %I %P}'.format(hourlyData.time))

print('\n').join(fogTimes)
