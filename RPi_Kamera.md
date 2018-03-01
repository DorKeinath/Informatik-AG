# Raspberry Pi

Denk daran, deinen Code in einer [Try-Schleife](RPi_Try.md) einzufügen.

## Kamera

Um die Kamera benutzen zu können, muss man bei

```bash
sudo raspi-config
```
unter *camera* dieselbe durch Auswahl von **Enable** aktivieren. Speichern und ein Neustart sind nicht verkehrt.

**Bilder** kann man aufnehmen mit:

```bash
raspistill -o bild.jpg
```

Eine **Video** der Länge 10 Sekunden kann man z.B. aufnehmen mit:

```bash
raspivid -o video1.h264 -t 10000
```
Anschauen kann man ein Video mittels:

```bash
omxplayer video.h264
```
Mehr Infos zum [omxplayer](RPi_omx.md)

Weitere Informationen:
* [Offizielle Rpi-Seite](https://www.raspberrypi.org/documentation/raspbian/applications/camera.md)
* [Video aus Bilder erstellen](https://trevorappleton.blogspot.de/2013/11/creating-time-lapse-camera-with.html)
+ [Kamera als Bewegungsmelder](www.pcpro.co.uk/features/386086/make-a-motion-sensing-camera-with-the-raspberry-pi)
* [Weitere Anleitungen zur Kamera](http://kampis-elektroecke.de/?page_id=4129)

### Arbeitsaufträge mit der Kamera

* Programmiere einen Fotoapparat, d.h. durch einen Taster soll ein Bild aufgenommen werden.
