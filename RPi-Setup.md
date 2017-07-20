<!-- MDTOC maxdepth:1 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [Raspberry Pi Setup mit Raspbian](#raspberry-pi-setup-mit-raspbian)   
- [Raspberry Pi Setup mit KivyPie](#raspberry-pi-setup-mit-kivypie)   

<!-- /MDTOC -->

# Raspberry Pi Setup mit Raspbian

## Download
https://www.raspberrypi.org/downloads/raspbian/

Ich denke für Schüler ist die Desktop-Variante (Pixel) ein bisschen besser. Wobei es schon auch einen gewissen Reiz hat, nur mit dem Terminal arbeiten zu können. Die Tastatureinstellung ist mit Pixel schneller gemacht :-)

## Prüfen und entpacken
Die sha1-Checksumme prüfen:

`sha1sum 2017...zip`

Die zip-Datei entpacken:

`unzip 2017...zip`

## Image auf die SD-Karte schreiben
Anscheinend braucht man für Pixel 8 GB.

Entweder man verwendet das Terminal:

`sudo dd bs=4M if=2017-07-05-raspbian-jessie.img of=/dev/sdc; sync`

wobei `sdc` die SD-Karte sein muss. Kann man mit `df` oder mit `GParted` herausfinden.

Oder man verwendet eine [andere Installationsmethode](https://www.raspberrypi.org/downloads/raspbian/), z.B. mit [NOOBS](https://www.raspberrypi.org/downloads/noobs/) oder [Etcher](https://etcher.io/?ref=etcher_footer).

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

# Raspberry Pi Setup mit KivyPie

Es gibt ein Debian-Image, das Kivy vorinstalliert hat.

## Download
http://kivypie.mitako.eu/kivy-download.html

## Image auf die SD-Karte schreiben
s.o.

## Zugangsdaten
Name: sysop
Passwort: posys

## Desktop starten
startx

## Tastatur umstellen
Ein Desktop-Terminal starten und folgendes eingeben:
`setxkbmap de`

## SD-Karte mounten
z.B. so:
```
dmesg
mkdir /mnt/sdkarte
mount /dev/sda1 /mnt/sdkarte
```
