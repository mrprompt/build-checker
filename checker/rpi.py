import RPi.GPIO as GPIO
import time
import os
import checker.travis as checker


# LEDs GPIO port: 11 = Green, 13 = White, 16 = Red
pins = [11, 13, 16]
delay = 30

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

project = os.environ['GITHUB_REPOSITORY']
token = os.environ['GITHUB_TOKEN']

while True:
    print(".")

    try:
        build = checker.cli(project, token)

        if build == 'failed':
            pin = pins[2]

        elif build == 'finished':
            pin = pins[0]

        else:
            pin = pins[1]

        GPIO.output(pins, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)

        time.sleep(delay)

    except KeyboardInterrupt:
        print("A keyboard interrupt has been noticed")

    except Exception as e:
        print("An error or exception has ocurred: " + str(e))

    finally:
        GPIO.cleanup()
