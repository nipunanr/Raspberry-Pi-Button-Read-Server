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
import OPi.GPIO as GPIO
import threading
from time import sleep
from flask import Flask, jsonify

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT)

# Startup LED Pattern
GPIO.output(11, GPIO.HIGH)
sleep(0.2)
GPIO.output(11, GPIO.LOW)
sleep(0.2)
GPIO.output(11, GPIO.HIGH)
sleep(0.2)
GPIO.output(11, GPIO.LOW)
sleep(0.2)
GPIO.output(11, GPIO.HIGH)
sleep(0.2)
GPIO.output(11, GPIO.LOW)
sleep(1)

try:
    def toggle_pin11():
        while True:
            if GPIO.input(5) == GPIO.HIGH:
                GPIO.output(11, GPIO.HIGH)
                sleep(1)
                GPIO.output(11, GPIO.LOW)
                sleep(1)
            else:
                GPIO.output(11, GPIO.LOW)

    def get_pin_status():
        if GPIO.input(5) == GPIO.HIGH:
            data = {
                'zone': '10.10.60.25',
                'status': 1
            }
            return jsonify(data)
        elif GPIO.input(5) == GPIO.LOW:
            data = {
                'zone': '10.10.60.25',
                'status': 0
            }
            return jsonify(data)

    @app.route('/status')
    def status():
        pin_status = get_pin_status()
        return pin_status

    def main():
        # Start the thread to toggle pin 11
        pin_thread = threading.Thread(target=toggle_pin11)
        pin_thread.daemon = True
        pin_thread.start()

    if __name__ == '__main__':
        main()
        app.run(host='0.0.0.0', port=8008)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    GPIO.cleanup()