# Raspberry Pi

Denk daran, deinen Code in einer [Try-Schleife](RPi_Try.md) einzufügen.

## 7-Segmentanzeige
7-Segmentanzeigen werden bei ihren mittleren Pins an der Erde angeschlossen. Den Rest der [Pinbelegung unserer 7-Segmentanzeigen](https://www.mymakerstuff.de/2016/05/12/die-siebensegmentanzeige#cc-m-header-13360887824) kannst du nachlesen oder selbst herausfinden. Verwende bitte 470-Ohm-Widerstände und wie immer `try`.

![](files/7-Segmentanzeige-01.png)

Wenn du z.B. von 0 bis 9 hochzählen lassen willst oder eine Tastatureingabe eine bestimmte Anzeige bewirken soll, solltest du [Listen und Dictionaries](python.md#pl-kollektionen) bei deiner Programmierung verwenden.

```python
...
zeige = ["a","b","ab"]
pin = {"a":3, "b":5}
# Auf die Werte greift man mit .values zu
for i in pin.values():
    GPIO.output(i,0)
# Auf die Schlüssel greift man mit eckiger Klammer zu
for k in range(len(zeige)):
    for i in zeige[k]:
        GPIO.output(pin[i],1)
sleep(1)
for i in zeige[]:
    GPIO.output(pin[i],1)
...
```

[Diese Codierung](https://www.mymakerstuff.de/2016/05/12/die-siebensegmentanzeige#cc-m-header-13360887824) könnte dir helfen, keinen Knoten im Hirn zu bekommen.
