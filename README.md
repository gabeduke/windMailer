## windMailer

windMailer reads the weather forcast and extracts the windspeed for the upcoming week. If the wind exceeds a given value then it will mail you a warning to your slack channel.

## Code Example

`0 11 * * * /usr/bin/python /home/user/windMailer/app/windMailer &>> /var/log/windMailer.log`

## Installation

```
git clone https://github.com/gabeduke/windMailer.git
python setup.py install
./app/windmailer
```