#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from random import randrange
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton

HOST = "localhost"
PORT = 4223
UID = "Dne"

def cb_button_state_changed(state):
    # On click change button color
    if state == BrickletRGBLEDButton.BUTTON_STATE_PRESSED:
        r = randrange(0, 255)
        b = randrange(0, 255)
        g = randrange(0, 255)
        print( str(r) + " / " + str(g) + " / " + str(b))
        rlb.set_color(r, b, g)

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rlb = BrickletRGBLEDButton(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    rlb.register_callback(rlb.CALLBACK_BUTTON_STATE_CHANGED, cb_button_state_changed)

    for i in range(10):
        print("Tick")
    time.sleep(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
