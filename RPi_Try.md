# Raspberry Pi

## Try

Wenn man ein Programm abbricht, weil es nicht so funktioniert wie man sich das gedacht hat, hat man ein Problem: Das `cleanup` wird nicht aufgerufen. Verwendet daher bitte den `try-except`-Befehl im folgenden Beispiel:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
print('Diese Programm kann man mit Strg+C abbrechen, ohne das RPi kaputt zu machen.')
# An dieser Stelle können später Funktionen stehen.
try:
    while True:
        # Ab hier steht das Hauptprogramm
        GPIO.output(12, GPIO.HIGH)
        sleep(1)
        GPIO.output(12, GPIO.LOW)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
```
