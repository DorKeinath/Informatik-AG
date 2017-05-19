#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

# Die Nummerierungen der PINs auf die physikalische Nummerierungen (1-40) festlegen.
GPIO.setmode(GPIO.BOARD)

# PIN als Ausgänge definieren
GPIO.setup(12, GPIO.OUT)

# Einschalten des PINs und 5 Sekunden warten
GPIO.output(12, 1)
sleep(5)

# Den Ausgangszustand wiederherstellen
GPIO.cleanup()
