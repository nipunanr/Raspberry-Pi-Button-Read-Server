# Use Pin2 - 5V (Brown), Pin7 - Yellow, Ground Pin - Orange  
# Access API from 'http://192.168.3.150:8008/status'

import RPi.GPIO as GPIO
from time import sleep
from flask import Flask, jsonify

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_pin_status():
    if GPIO.input(7) == GPIO.HIGH:

        data = {
            'zone': '192.168.3.150',
            'status': 1
        }
        return jsonify(data)

    elif GPIO.input(7) == GPIO.LOW:

        data = {
            'zone': '192.168.3.150',
            'status': 0
        }
        return jsonify(data)

@app.route('/status')
def status():
    pin_status = get_pin_status()
    return pin_status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
