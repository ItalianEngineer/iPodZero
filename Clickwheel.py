import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins for the click wheel
CLK = 23
DT = 5

GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the variables to keep track of the click wheel state
clkLastState = GPIO.input(CLK)

while True:
    clkState = GPIO.input(CLK)
    dtState = GPIO.input(DT)

    if clkState != clkLastState:
        if dtState != clkState:
            # clockwise rotation
            print("UP key activated")
            time.sleep(0.1)
        else:
            # counter-clockwise rotation
            print("DOWN key activated")
            time.sleep(0.1)

    clkLastState = clkState
