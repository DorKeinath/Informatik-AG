# Raspberry Pi

## Medien abspielen

Zum Abspielen von Video- und Musik-Dateien kann man **omxplayer** verwenden.

```bash
from subprocess import call

call('omxplayer -o local /home/pi/Downloads/dr.mp3', shell=True)

```

Weitere Informationen

* [https://www.raspberrypi.org/documentation/usage/audio/](https://www.raspberrypi.org/documentation/usage/audio/)
* [https://www.raspberrypi.org/documentation/usage/video/README.md](https://www.raspberrypi.org/documentation/usage/video/README.md)
