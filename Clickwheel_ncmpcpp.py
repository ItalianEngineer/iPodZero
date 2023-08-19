import RPi.GPIO as GPIO
import subprocess

# Define GPIO pin numbers for the click wheel components
CW_SCL = 23  # Adjust to match your setup
CW_SDA = 5   # Adjust to match your setup

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set GPIO pins as inputs without pull-up resistors
GPIO.setup(CW_SCL, GPIO.IN)
GPIO.setup(CW_SDA, GPIO.IN)

def execute_ncmpcpp_command(command):
    subprocess.run(["ncmpcpp", "-c", command])

scroll_position = 0  # Initialize scroll position

def scroll_action(channel):
    global scroll_position
    if GPIO.input(CW_SDA):
        scroll_position += 1
        execute_ncmpcpp_command(f"seek {scroll_position}")
    else:
        scroll_position -= 1
        if scroll_position < 0:
            scroll_position = 0
        execute_ncmpcpp_command(f"seek {scroll_position}")

# Detect rising and falling edge events (click wheel rotations)
GPIO.add_event_detect(CW_SCL, GPIO.BOTH, callback=scroll_action, bouncetime=200)
GPIO.add_event_detect(CW_SDA, GPIO.BOTH, callback=scroll_action, bouncetime=200)

try:
    # Keep the script running
    while True:
        pass

except KeyboardInterrupt:
    print("Script terminated by user")
    GPIO.cleanup()
