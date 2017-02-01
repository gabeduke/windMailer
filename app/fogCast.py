#!/usr/bin/env python
import forecastio
import sys
import os.path
import pdb

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# import sys
# sys.path.insert(0, "home/gabeduke/windMailer/settings.py")
from settings import *

# fetching weather
forecast = forecastio.load_forecast(forecast_key, lat, lng)
by_day = forecast.daily()
by_hour = forecast.hourly()

fogTimes = []
debug = []

for hourlyData in by_hour.data:
    deg = hourlyData.temperature
    dew = hourlyData.dewPoint
    diff = abs(dew - deg)
    debug.append('{:%a: %I %P}'.format(hourlyData.time) + " | dewpoint = " + str(int(dew)) + " | deg = " + str(int(deg)) + " | diff = " + str(int(diff)))
    if deg <= 66 and diff <= 5:
        fogTimes.append('Chance of fog on ' + '{:%a at %I %P}'.format(hourlyData.time))

pdb.set_trace()
if len(sys.argv)>1 and "debug" in sys.argv[1:]:
    print('\n').join(debug)
print('\n').join(fogTimes)
