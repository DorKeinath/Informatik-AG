# Raspberry Pi Setup mit Raspbian

## Download
https://www.raspberrypi.org/downloads/raspbian/
Ich denke für Schüler ist die Desktop-Variante (Pixel) einen Tick besser. Wobei es schon auch einen gewissen Reiz hat, nur mit dem Terminal arbeiten zu können. Die Tastatureinstellung ist mit Pixel schneller gemacht :-)

## Entpacken
Die zip-Datei entpacken

`unzip ...zip`

## Image auf die SD-Karte schreiben
Anscheinend braucht man für Pixel 8 GB.
Entweder man verwendet das Terminal:

`sudo dd bs=4M if=2017-03-02-raspbian-jessie.img of=/dev/sdc`

wobei `sdc` die SD-Karte sein muss. Kann man mit `df` oder mit `GParted` herausfinden.

Oder noch leichter (unter Linux Mint vorinstalliert) mit **gnome-disks**. Da sieht man automatisch, wie lang's noch geht :-)

## Tastatur umstellen
Menü/Preferences/Mouse and Keyboard Settings/Keyboard Layout auf Germany/German einstellen.

## Einstellungen für LITE
Hat man sich gegen Pixel entschieden, kann man die Tastatur so umstellen:

`sudo raspi-config`

Unter Internationalisation
1. Change Local: de_DE.UTF-8 UTF-8 mittel *Leertaste* auswählen und mit OK bestätigen, dann nochmal de... auswählen.
2. Change Timezone: Europa/Berlin
3. Change Keyboard Layout: Microsoft Office Keyboard/Other/German.

## Optional
### Update
Da das Updaten sonst noch viel ewiger geht, sollte man vorher
1. Wolfram deinstallieren: `sudo apt-get remove wolfram-engine`
2. `sudo apt-get update`
3. `sudo apt-get upgrade`
### Python-Programme
Unter LITE ist nur Python2 installiert. Hier also evtl. noch

`sudo apt-get install python3-rpi.gpio`

Manche empfehlen noch

`sudo apt-get install python-dev`
