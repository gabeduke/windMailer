#!/usr/bin/env python
import forecastio
import slackweb
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg['API_KEYS'])
print(cfg['VARS'])
print(cfg['SLACK'])

wind_threshold = 10
w = "" # initializing in global context

# fetching weather
forecast = forecastio.load_forecast(forecast_key, lat, lng)
by_day = forecast.daily()

for dailyData in by_day.data:
    wind = dailyData.windSpeed
    time = dailyData.time
    wind_message = "Wind is expected to be " + str(wind) + "mph on " + str(time.strftime("%A\n"))

    if wind >= wind_threshold:
        w += wind_message

if w:
    slack = slackweb.Slack(url=web_hook)
    slack.notify(text=w, channel=slack_channel)
