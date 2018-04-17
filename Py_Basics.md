# Python

## Python-Console und -Skripte + print, help, input, import, type

### PL: Basics

Mit Python kann man Computerprogramme schreiben. Ein Programm ist der Text, der der dummen Hardware sagt, was sie tun soll. Also zum Beispiel soll der Bildschirm "Hallo" schreiben. Das Programm ist dabei nicht nur Code, sondern besteht quasi aus Gedanken.

**Python-Console** starten mit `python` oder `python3` und sie beenden mit Strg+D. Den Bildschirm leeren geht mit Strg+L.

`python3`

`print('Hallo Welt!')`

**Hilfe** zu vorhandenen Funktionen erhält man mit `help()`. Beenden der Hilfe mit `q`.

`help(len)`

**Ausgeben und Abfragen**

`print('Dor' + 'Keinath')`
`print(1000*'DorKeinath ')`

`a = input('Gib etwas ein:')`


**Importieren** weiterer Funktionen aus noch nicht geladenen Pakten

```
import time
print(time.asctime())
```

oder für einzelne Funktionen:

```
from time import asctime
print(asctime())
```

Weiteres Beispiel: Um den Bildschirm zu löschen, kannst du den folgenden Code verwenden:

```
from subprocess import call
call("clear")
```

(Früher hat man `from os import system` und `system("clear")` oder `os.popen` verwendet. Weitere Informationen zu [subprocess](http://www.admin-magazin.de/Das-Heft/2012/05/Kommandos-mit-dem-Subprocess-Modul-aufrufen), [weitere Methoden](https://stackoverflow.com/questions/89228/calling-an-external-command-in-python/92395#92395) Terminal-Befehle durch Python auszuführen.)

Ein ganzes **Python-Skript** bzw. **Python-Programm** test.py schreiben und mit `python3 test.py` (oder - falls das Shabang vorhanden ist - mit `./test.py`) starten.

```python
#!/usr/bin/env python3

name = input('Wie heißt du? ')
print('Hallo ' + name + '!')
```

**Typen** benötigen manchmal besondere Aufmerksamkeit: Versuche, die Summe aus zwei abgefragten Zahlen ausgeben zu lassen.

`type(3.2)`

```python
#!/usr/bin/env python3

erste_eingabe = input('Erster Summand: ')
zweite_eingabe = input('Zweiter Summand: ')
a = float(erste_eingabe)
b = float(zweite_eingabe)
s = a + b
print('Die Summe ist: ' + str(s))
```

### EA: Begrüßung
Schreibe ein Python-Skript, das den Aufrufer nach seinem Namen fragt und ihn dann mit seinem Namen und der aktuellen Uhrzeit begrüßt, z.B. "Hallo Python, es ist 12:45 Uhr."

Um die Uhrzeit schön zu formatieren, kannst du aus dem Modul `time` die Funktion `strftime` verwenden:

```python
from time import strftime
print(strftime("%d %b %Y %H:%M:%S"))

```
([Mehr zur Funktion `strftime`](https://docs.python.org/2/library/time.html#time.strftime))

### EA: Potenz-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einer Basis und einem Exponenten fragt und dann die Potenz berechnet und ausgibt. Hinweis: `2**3` ergibt 8.

### EA: Kreis-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einem Radius oder Durchmesser eines Kreises fragt und damit den Umfang und Inhalt des Kreises berechnet und ausgibt. Hinweis: Du kannst Pi aus dem Paket `math` verwenden

```python
from math import pi
```

### EA: Terminal-Programm (Für Fortgeschrittene)

Mit Python kann man Terminal-Skripte schreiben, die man mit Argumenten (z.B. `-h`) oder *positional arguements* (z.B. `less datei.txt`) aufrufen kann. Will man sie schön schreiben, verwendet man das Modul `argparse`. Das Modul erzeugt dann auch automatisch eine Hilfe, die der Benutzer des Programms mit dem üblichen `-h` aufrufen kann.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from subprocess import call
from shlex import split

def eine_funktion(argument_eins, positionsargument):
    print('Der Funktion namens eine_funktion wurde die Argumente ' + argument_eins + ' und ' + positionsargument + ' übergeben.')
    call(split('echo Terminalbefehle kann man auch aufrufen.'))

if __name__ == '__main__':
    # Eine Beschreibung des Programms, die beim Aufruf der Hilfe (-h) angezeigt wird.
    parser = argparse.ArgumentParser(description='Dieses Programm erläutert die Funktionsweise von argparse.')
    # Ein klassisches Argument
    parser.add_argument('-a', dest='argument_eins', type=str, help='Irgend ein Text, den der Benutzer eingeben kann.')
    # Ein Positionsargument
    parser.add_argument('positionsargument', metavar='positionsargument', type=str, help='Irgend ein Text, den der Benutzer hinter dem Dateiname des Programms eingeben muss.')
    # Ein Argument das einen bestimmten Wert speichert
    parser.add_argument('-v', dest='variable', action='store_const', const=True, default=False, help='Speichert in der Variablen args.variable den Wert True.')

    args = parser.parse_args()

    if args.argument_eins is None:
        args.argument_eins = raw_input("Argument: ")

    eine_funktion(args.argument_eins, args.positionsargument)

```
