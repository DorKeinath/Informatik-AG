# Linux
[distrochooser.de](https://distrochooser.de/?l=1)
[Verzeichnisstruktur](https://wiki.ubuntuusers.de/Verzeichnisstruktur/)

# Terminal
[HO](http://www.321tux.de/wp-content/uploads/2010/03/shell-uebersicht.pdf)
[Kurze Einführung auf ubuntuusers](https://wiki.ubuntuusers.de/Shell/Einf%C3%BChrung/)

## Einführung im Plenum
* `pwd`
* `ls`
* `ls -l`
* `ls -a`
* Tabulator zur Syntaxergänzung
* Pfeiltasten, `history` und Strg+R für bisherige Aufrufe.
* Strg+C zum Beenden eines Prozesses
* `sudo`

Minimalziel der Stunde: Ordner und Datei erstellen und kopieren können.

## Übungen in EA/PA
Wofür sind die folgenden Befehle gut?

Suche mit `--help` oder `man` nach dem Befehl und führe ihn im Terminal so aus, wie sein Aufruf definiert ist. Zum Beispiel steht bei `ls --help`

> Aufruf: ls [OPTION]... [DATEI]...

Das heißt, dass man eine Option oder einen Dateinamen eingeben kann, aber nicht muss.

* `cd`
* `cd ..`
* `mkdir`
* `rmdir`
* `touch`
* `cp`
* `mv`
* `rm`
* `firefox`
* `find`
* `echo`
* `wget`
* `ifconfig`
* `nano`
* `vi`
* `tar`
* `geunzip`
* `cat`
* `apt`
* `df`
* `which`
* `rsync`

## Spielereien
* `curl wttr.in/bretten`
* `time read`
* `tr -c "[:digit:]" " " < /dev/urandom | dd cbs=$COLUMNS conv=unblock | GREP_COLOR="1;32" grep --color "[^ ]"`
* `cat /dev/urandom | hexdump -C | grep "ca fe"`
* [Freakige Befehle](https://www.commandlinefu.com/commands/browse/sort-by-votes)
