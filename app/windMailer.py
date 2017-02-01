#!/usr/bin/env python
import forecastio
import slackweb
from settings import *

wind_threshold = 10
w = ""  # initializing in global context

# fetching weather
forecast = forecastio.load_forecast(forecast_key, lat, lng)
by_day = forecast.daily()
by_hour = forecast.hourly()

for dailyData in by_day.data:
    wind = dailyData.windSpeed
    time = dailyData.time
    wind_message = "Wind is expected to be " + str(wind) + "mph on " + str(time.strftime("%A\n"))

    if wind >= wind_threshold:
        w += wind_message

if w:
    slack = slackweb.Slack(url=web_hook)
    slack.notify(text=w, channel=slack_channel)
