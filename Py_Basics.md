# Python

<!-- MDTOC maxdepth:6 firsth1:2 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [Python-Basics](#python-basics)   
   - [Python-Konsole](#python-konsole)   
   - [help](#help)   
   - [print, input](#print-input)   
   - [import, asctime, subprocess](#import-asctime-subprocess)   
   - [Python-Skript](#python-skript)   
   - [Typen](#typen)   
- [Arbeitsaufträge](#arbeitsaufträge)   
   - [Begrüßung](#begrüßung)   
   - [Potenz-Berechner](#potenz-berechner)   
   - [Kreis-Berechner](#kreis-berechner)   
   - [Terminal-Programm (Für Fortgeschrittene)](#terminal-programm-für-fortgeschrittene)   

<!-- /MDTOC -->

## Python-Basics

Mit Python kann man Computerprogramme schreiben. Ein Programm ist der Text, der der dummen Hardware sagt, was sie tun soll. Also zum Beispiel soll der Bildschirm "Hallo" schreiben. Das Programm ist dabei nicht nur Code, sondern besteht quasi aus Gedanken.

### Python-Konsole

**Python-Konsole** starten mit `python` oder `python3` und sie beenden mit Strg+D. Den Bildschirm leeren geht mit Strg+L.

`python3`

`print('Hallo Welt!')`

### help

**Hilfe** zu vorhandenen Funktionen erhält man mit `help()`. Beenden der Hilfe mit `q`.

`help(len)`

### print, input

So schreibt man etwas:

`print('Dor' + 'Keinath')`
`print(1000*'DorKeinath ')`

So liest man einen Text in die Variable a ein:

`a = input('Gib etwas ein:')`

### import, asctime, subprocess

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

### Python-Skript

Ein ganzes **Python-Skript** bzw. **Python-Programm** test.py schreiben und mit `python3 test.py` (oder - falls das Shabang vorhanden ist - mit `./test.py`) starten.

```python
#!/usr/bin/env python3

name = input('Wie heißt du? ')
print('Hallo ' + name + '!')
```

### Typen

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

## Arbeitsaufträge

### Begrüßung
Schreibe ein Python-Skript, das den Aufrufer nach seinem Namen fragt und ihn dann mit seinem Namen und der aktuellen Uhrzeit begrüßt, z.B. "Hallo Python, es ist 12:45 Uhr."

Um die Uhrzeit schön zu formatieren, kannst du aus dem Modul `time` die Funktion `strftime` verwenden:

```python
from time import strftime
print(strftime("%d %b %Y %H:%M:%S"))

```
([Mehr zur Funktion `strftime`](https://docs.python.org/2/library/time.html#time.strftime))

### Potenz-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einer Basis und einem Exponenten fragt und dann die Potenz berechnet und ausgibt. Hinweis: `2**3` ergibt 8.

### Kreis-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einem Radius oder Durchmesser eines Kreises fragt und damit den Umfang und Inhalt des Kreises berechnet und ausgibt. Hinweis: Du kannst Pi aus dem Paket `math` verwenden

```python
from math import pi
```

### Terminal-Programm (Für Fortgeschrittene)
Schreibe eines der beiden obigen Programme als [Terminal-Programm](Terminal.md)
