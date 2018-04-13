# Linux
[distrochooser.de](https://distrochooser.de/?l=1)

[Verzeichnisstruktur](https://wiki.ubuntuusers.de/Verzeichnisstruktur/)

# Terminal
[HO](http://www.321tux.de/wp-content/uploads/2010/03/shell-uebersicht.pdf)

[Nette Übersicht auf Linuxmint](https://community.linuxmint.com/tutorial/view/244)

Kurze Einführungen auf ubuntuusers: [Shell](https://wiki.ubuntuusers.de/Shell/Einf%C3%BChrung/), [Bash](https://wiki.ubuntuusers.de/Bash/#source-2)


## Einführung im Plenum
* `pwd`
* `ls`
* `ls -lhtra` (long humanreadable zeitgeordnet umgekehrt versteckte)
* **Tabulator** zur Syntaxergänzung.
* **Pfeil-nach-oben** zum Aufruf der letzten Eingabe.
* **Strg+C** zum Beenden eines Prozesses.
* `sudo`
* Ein `^`, z.B. beim Bearbeiten einer Datei mit `nano` bedeutet die *Strg-Taste*.

## Übungen in EA/PA
Wofür sind die folgenden Befehle gut? Finde heraus, wofür die Befehle verwendet werden können und probiere den einen oder anderen Befehl aus.

Das Minimalziel der Stunde ist es, dass du **Ordner und Datei erstellen und kopieren** kannst.

Es gibt mehrere Möglichkeiten, wie du etwas über einen Befehl X herausfinden kannst:

1. `whatis X`
2. `X --help`
3. `man X`

Zum Beispiel spuckt das Terminal bei `ls --help` so etwas aus wie

> Aufruf: ls [OPTION]... [DATEI]...

Das heißt, dass man eine Option oder einen Dateinamen eingeben kann, aber nicht muss.

* `cd`
* `cd ..`
* `cd -`
* `mkdir`
* `rmdir`
* `touch`
* `cp`
* `mv`
* `rm`
* `clear`
* `tree`
* `find`
* `echo`
* `firefox`
* `cal`
* `wget`
* `tar`
* `gzip`
* `nano`
* `vi`
* `cat`
* `apt`
* `ifconfig`
* `which`
* `whereis`
* `rsync`
* `history`
* `df -h`
* `cat /proc/partitions`
* `dmesg`

## Spielereien
* `curl wttr.in/bretten`
* `rev`
* `time read`
* `tr -c "[:digit:]" " " < /dev/urandom | dd cbs=$COLUMNS conv=unblock | GREP_COLOR="1;32" grep --color "[^ ]"`
* `cat /dev/urandom | hexdump -C | grep "ca fe"`
* [Freakige Befehle](https://www.commandlinefu.com/commands/browse/sort-by-votes)

## Effektiver Umgang mit dem Terminal
* Bisherige Befehle nochmal aufrufen mit
    * **Ausrufezeichen** gefolgt von einem Zeichen ruft den letzten Befehl mit diesem Zeichen auf.
    * `history`, dann `!` gefolgt von der Nummer.
    * **Strg+R**
* `sudo !!`
* [Aliase](https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias) über die Datei `~/.bashrc`.
* [Dateien durchsuchen] mit `locate` oder `find`: [1](https://wiki.ubuntuusers.de/locate/), [2](https://wiki.ubuntuusers.de/find/), [3](https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-a-linux-vps), [4](http://www.linfo.org/locate.html), [5](https://unix.stackexchange.com/questions/151700/how-to-add-specific-directories-to-updatedb-locate-search-path), [6](https://askubuntu.com/questions/160424/how-do-i-get-mlocate-to-only-index-certain-directories)


## Weitere Beispiele
* `sudo pm-hibernate`
* `find \( -iname '*.jpg' -or -iname '*.jpeg' -or -iname '*.gif' -or -iname '*.png' -or -iname '*.bmp' \) |  wc -l`
* `ls -1 *.jpg | parallel -j 3 convert '{}' -resize 1920x -quality 60 '{}_1920px'`
* [http://www.shellbefehle.de/bash-tipps/](http://www.shellbefehle.de/bash-tipps/)

## Security mit dem Terminal

Mit dem Terminal kann man seine [Sicherheit hinsichtlich seines Datenschutzes](https://secitem.at/blog/terminal-tipps) erhöhen. Z.B.

* `diceware -n 4` [diceware auf GitHub](https://github.com/ulif/diceware)
* `find \( -iname '*.jpg' -or -iname '*.jpeg' -or -iname '*.gif' -or -iname '*.png' -or -iname '*.bmp'  \) -print0 | xargs -0 mogrify -strip`

# Bash-Skripte

Bash-Skripte haben die Endung `*.sh` und können in der ersten Zeile ein Shebang haben. Mit einem Bash-Skript kann man mehrere Terminal-Befehle hintereinander ausführen lassen; ein Bash-Skript ist also quasi ein Terminal-Programm. Und so sieht der Code der Datei `test.sh` aus:

```Bash
#!/bin/bash
notify-send "Start"

```
Dabei sind Zeilen mit `#` Kommentare.

Das Skript starten geht z.B. mit

`bash test.sh`

oder

`./test.sh`

Beim letzteren Startbefehl muss man vor dem Ausführen bei den Zugriffsrechten das starten zulassen:

`chmod u+x test.sh`


## Bash-Spiel

Programmiere mit Hilfe [dieses Links](https://github.com/mydzor/bash2048) ein Bash-Spiel.
