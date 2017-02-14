# Linux
[distrochooser.de](https://distrochooser.de/?l=1)

[Verzeichnisstruktur](https://wiki.ubuntuusers.de/Verzeichnisstruktur/)

# Terminal
[HO](http://www.321tux.de/wp-content/uploads/2010/03/shell-uebersicht.pdf)

[Kurze Einführung auf ubuntuusers](https://wiki.ubuntuusers.de/Shell/Einf%C3%BChrung/)

[Nette Übersicht auf Linuxmint](https://community.linuxmint.com/tutorial/view/244)

## Einführung im Plenum
* `pwd`
* `ls`
* `ls -lhtra` (long humanreadable zeitgeordnet umgekehrt versteckte)
* Tabulator zur Syntaxergänzung.
* Pfeil-nach-oben zum Aufruf der letzten Eingabe.
* Pfeiltasten, `history` mit `!` und Strg+R für bisherige Aufrufe.
* Strg+C zum Beenden eines Prozesses.
* `sudo`



## Übungen in EA/PA
Wofür sind die folgenden Befehle gut? Finde heraus, wofür die Befehle verwendet werden können und probiere den einen oder anderen Befehl aus.

Das Minimalziel der Stunde ist es, dass du **Ordner und Datei erstellen und kopieren** kannst.

Es gibt mehrere Möglichkeiten, wie du etwas über einen Befehl x herausfinden kannst:

1. `whatis x`
2. `x --help`
3. `man x`

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
* `df -h`
* `ifconfig`
* `which`
* `whereis`
* `locate`
* `rsync`

## Spielereien
* `curl wttr.in/bretten`
* `rev`
* `time read`
* `tr -c "[:digit:]" " " < /dev/urandom | dd cbs=$COLUMNS conv=unblock | GREP_COLOR="1;32" grep --color "[^ ]"`
* `cat /dev/urandom | hexdump -C | grep "ca fe"`
* [Freakige Befehle](https://www.commandlinefu.com/commands/browse/sort-by-votes)

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

"Programmiere" mit Hilfe [dieses Links](https://github.com/mydzor/bash2048) ein Bash-Spiel
