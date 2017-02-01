# Python

## Links

### Tutorials

[Deutsches Python-Tutorial](http://py-tutorial-de.readthedocs.io/de/python-3.3/)

[Englisches Python-Tutorial](https://learnpythonthehardway.org/book/)

[Englisches Buch bzw. pdf](http://greenteapress.com/wp/think-python-2e/)

[Deutsches Einsteigerbuch](https://www.dpunkt.de/buecher/4571/python-kinderleicht%21.html)

### Python auf Android

[QPython](http://qpython.com/)

[Kivy](https://kivy.org/docs/gettingstarted/first_app.html)

## Einstieg in Python

### PL (Basics)

**Python-Console** starten mit `python` oder `python3` und sie beenden mit Strg+D.

`python3`

**Hilfe** zu vorhandenen Funktionen erhält man mit `help()`. Beenden derselben mit `q`.

`help(len)`

**Ausgeben und Abfragen**

`print(1000*'DorKeinath ')`

`a = input('Gib etwas ein:')`


**Importieren** weiterer Funktionen aus noch nicht geladenen Pakten

```
import time
print(time.asctime())
```

oder

```
from time import asctime
print(asctime())
```

Ein ganzes **Python-Skript** bzw. **Python-Programm** test.py schreiben und mit `python3 test.py` (oder - falls das Shabang vorhanden ist - mit `./test.py`) starten.

```
#!/usr/bin/env python3

name = input('Wie heißt du? ')
print('Hallo ' + name + '!')
```

**Typen** benötigen manchmal besondere Aufmerksamkeit: Versuche, die Summe aus zwei abgefragten Zahlen ausgeben zu lassen.

`type(3.2)`

```
#!/usr/bin/env python3

erste_eingabe = input('Erster Summand: ')
zweite_eingabe = input('Zweiter Summand: ')
a = float(erste_eingabe)
b = float(zweite_eingabe)
s = a + b
print('Die Summe ist: ' + str(s))
```

### EA (BMI-Rechner)

Gib den Body-Mass-Index einer Person aus, indem du sie vorher nach den nötigen Variablen fragst.

Du kannst Pi aus dem Paket `math` verwenden

`from math import pi`

### PL (Kollektionen)

Strings sind nicht die wichtigste Objekte, die beim Programmieren verwendet werden, Listen sind z.B. wichtiger; sie werden in eckige Klammern geschrieben. Man hat die folgenden Möglichkeiten:

* Sequenzen, bei denen die Reihenfolge eine Rolle spielt
  + list `['Haus', 'Katze', 'Maus']`
  + tuple `(1, 2, 3)`
  + str `'Hallo'`
  + byte `b'Bl\xc3\xb6de Buchstaben'`
* Und Kollektionen, bei denen die Reihenfolge keine Rolle spielt
  + Mengen
    * set `{1, 2, 3}`
    * frozenset `frozenset{1, 2, 3}`
  + dict `{'schluessel': wert, 'schluessel2': wert2}`

Eine wichtige Eigenschaft von Kollektionen ist ihre (Un-)Veränderbarkeit.

Unveränderbar
 * tuple
 * str
 * bytes
 * frozenset

 Veränderbar
 * list
 * set
 * dict

#### Kurzer Exkurs zu den Bytsequenzen
*Mögliches GFS-Thema*
Es gibt verschiedene Zeichentabellen. Die älteste heißt **ASCII**; sie enthält nur 128 Zeichen. Die größte Zeichentabelle heißt **Unicode** und ihre bekannteste Kodierung (engl. "encoding") heißt **UTF-8**. Python3 definiert Strings (`str`) als Unicode-Text.

`text = bytes('Blöde Buchstaben wie äöüß', 'utf-8')`

Das "b" bei der Ausgabe von `text` bedeutet, dass das Folgende als ein Bytestring ist.

`re = text.decode("utf-8")`


<!-- Später
## Einstieg in Kivy

**Uhrzeit**
-->
