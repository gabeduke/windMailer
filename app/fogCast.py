#!/usr/bin/env python
import forecastio
import pylab as pl
from settings import *

# fetching weather
forecast = forecastio.load_forecast(forecast_key, lat, lng)
by_day = forecast.daily()
by_hour = forecast.hourly()

fogTimes = []

for hourlyData in by_hour.data:
    diff = abs(hourlyData.dewPoint - hourlyData.temperature)
    if diff <= 10:
        fogTimes.append('fog is possible on ' + '{:%a at %I %P}'.format(hourlyData.time))

print('\n').join(fogTimes)
