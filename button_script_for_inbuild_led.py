# --------------------------------------------------------------------

# Client       : Phoenix Industries
# Project      : Support Zone Indication System
# Period       : 10-08-2023 - 15-09-2023

# Script By    : Nipuna Rangika 

# Copyright Reserved | MISL Holdings (Pvt) Ltd

#----------------------------------------------------------------------

# Use Pin2 - 5V (Brown), Pin7 - Yellow, Ground Pin - Orange
# Access API from 'http://192.168.3.150:8008/status'  -- Method : GET

# Import necessary libraries
import OPi.GPIO as GPIO  # Use as 'RPi.GPIO' if it is a Raspberry Pi board.
from time import sleep
from flask import Flask, jsonify

# Create a Flask web application
app = Flask(__name__)

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set GPIO mode to use the physical pin numbering (BOARD mode)
GPIO.setmode(GPIO.BOARD)

# Set up Pin 7 (Yellow) as an input with a pull-down resistor
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to get the status of Pin 7
def get_pin_status():
    if GPIO.input(7) == GPIO.HIGH:
        # If Pin 7 is HIGH, return status 1 (indicating the zone is active)
        data = {
            'zone': '192.168.3.150',
            'status': 1
        }
        return jsonify(data)
    elif GPIO.input(7) == GPIO.LOW:
        # If Pin 7 is LOW, return status 0 (indicating the zone is not active)
        data = {
            'zone': '192.168.3.150',
            'status': 0
        }
        return jsonify(data)

# Define a route for the '/status' endpoint
@app.route('/status')
def status():
    # Call the get_pin_status function to get the zone status
    pin_status = get_pin_status()
    # Return the status as a JSON response
    return pin_status

# Run the Flask application on host 0.0.0.0 (accessible from any network interface) and port 8008
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)