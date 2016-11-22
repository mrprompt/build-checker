#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import time
import urllib
import urllib2
import json
import RPi.GPIO as GPIO

# LEDs GPIO port: 11 = Green, 13 = Gray, 16 = Red
pins = [11, 13, 16]
delay = 30

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

url = 'https://api.travis-ci.org/QueroUmaLoja/api-server/builds'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)

try:
    while True:
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        content = response.read()

        obj = json.loads(content)
        build = obj[0]

        if build['state'] == 'failed':
            pin = pins[2]

        elif build['state'] == 'finished':
            pin = pins[0]

        else:
            pin = pins[1]

        GPIO.output(pins, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)

        time.sleep(delay)

except KeyboardInterrupt:
    print("A keyboard interrupt has been noticed")

except urllib2.HTTPError as e:
    print("An HTTP error or exception has ocurred: " + str(e))

except Exception, e:
    print("An error or exception has ocurred: " + str(e))

finally:
    GPIO.cleanup()
