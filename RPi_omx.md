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

Für gleichzeitiges Abspielen mehrerer Dateien, kann man `subprocess.Popen` verwenden 

```bash
from subprocess import Popen

Popen("mplayer 1.mp3", shell=True)
Popen("mplayer 2.mp3", shell=True)

```

oder jeweils ein `xterm` mit `&` starten.

```bash
from subprocess import call

call("xterm -e mplayer 1.mp3 &", shell=True)
call("xterm -e mplayer 2.mp3 &", shell=True)

```
