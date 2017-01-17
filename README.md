## windMailer

windMailer reads the weather forcast and extracts the windspeed for the upcoming week. If the wind exceeds a given value then it will mail you a warning to your slack channel.

You will need to have your Slack webhook and Darksky API keys in order to run the program initially.

## Code Example

`0 11 * * * /usr/bin/python /home/user/windMailer/app/windMailer &>> /var/log/windMailer.log`

## Installation

Clone the repository & install packages
```
git clone https://github.com/gabeduke/windMailer.git
python setup.py install
```

Copy the config & fill in datas
```
cp config-example.yml config.yml && vim config.yml
```

run app
```
./app/windmailer
```
