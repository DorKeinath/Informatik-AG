# Linux
[distrochooser.de](https://distrochooser.de/?l=1)

[Verzeichnisstruktur](https://wiki.ubuntuusers.de/Verzeichnisstruktur/)

# Terminal
[HO](http://www.321tux.de/wp-content/uploads/2010/03/shell-uebersicht.pdf)

[Kurze Einführung auf ubuntuusers](https://wiki.ubuntuusers.de/Shell/Einf%C3%BChrung/)

## Einführung im Plenum
* `pwd`
* `ls`
* `ls -lhtra` (long humanreadable zeitgeordnet umgekehrt versteckte)
* Tabulator zur Syntaxergänzung
* Pfeiltasten, `history` mit `!` und Strg+R für bisherige Aufrufe.
* Strg+C zum Beenden eines Prozesses
* `sudo`



## Übungen in EA/PA
Wofür sind die folgenden Befehle gut? Finde heraus, wofür die Befehle verwendet werden können und probiere den einen oder anderen Befehl aus.

Das Minimalziel der Stunde ist es,dass du **Ordner und Datei erstellen und kopieren** kannst.

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
* `find`
* `echo`
* `firefox`
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
* `time read`
* `tr -c "[:digit:]" " " < /dev/urandom | dd cbs=$COLUMNS conv=unblock | GREP_COLOR="1;32" grep --color "[^ ]"`
* `cat /dev/urandom | hexdump -C | grep "ca fe"`
* [Freakige Befehle](https://www.commandlinefu.com/commands/browse/sort-by-votes)
