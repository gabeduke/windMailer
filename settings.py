import os
import yaml

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, ".env"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

API_KEYS = cfg['API_KEYS']
VARS = cfg['VARS']
SLACK = cfg['SLACK']

web_hook = API_KEYS['web_hook']
forecast_key = API_KEYS['forecast_key']

lat = VARS['lat']
lng = VARS['lng']

slack_channel= SLACK['slack_channel']
