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
rotation_count = 0

while True:
    clkState = GPIO.input(CLK)
    dtState = GPIO.input(DT)

    if clkState != clkLastState:
        if dtState != clkState:
            # Clockwise rotation
            rotation_count += 1
        else:
            # Counter-clockwise rotation
            rotation_count -= 1

        if rotation_count >= 3:
            print("UP key activated")
            rotation_count = 0
        elif rotation_count <= -3:
            print("DOWN key activated")
            rotation_count = 0

    clkLastState = clkState
