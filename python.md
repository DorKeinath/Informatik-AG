# Python

## Links

### Tutorials

[Deutsches Python-Tutorial](http://py-tutorial-de.readthedocs.io/de/python-3.3/)

[Englisches Python-Tutorial](https://learnpythonthehardway.org/book/)

[The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)

[Englisches Buch bzw. pdf](http://greenteapress.com/wp/think-python-2e/)

[Deutsches Einsteigerbuch](https://www.dpunkt.de/buecher/4571/python-kinderleicht%21.html)

### Python auf Android

[QPython](http://qpython.com/)

[Kivy](https://kivy.org/docs/gettingstarted/first_app.html)

## Einstieg in Python

### PL (Basics)

Mit Python kann man Computerprogramme schreiben. Ein Programm ist der Text, der der dummen Hardware sagt, was sie tun soll. Also zum Beispiel soll der Bildschirm "Hallo" schreiben. Das Programm ist dabei nicht nur Code, sondern besteht quasi aus Gedanken.

**Python-Console** starten mit `python` oder `python3` und sie beenden mit Strg+D.

`python3`

`print('Hallo Welt!')`

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

### EA (BMI-Rechner)

Gib den Body-Mass-Index einer Person aus, indem du sie vorher nach den nötigen Variablen fragst.

Du kannst Pi aus dem Paket `math` verwenden

```python
from math import pi
```

### PL (for)

```python
for i in range(10):
  print("Hallo! ", end="")
```

### PL (if-else)

```python
zahl = input("Gib bitte eine gerade Zahl ein: ")
n = int(zahl)
if n % 2 == 1:
    print("ungerade")
else:
    print("gerade")
```

### EA (Passwortabfrage)
Lass dir einen Namen und ein Passwort geben. Wenn beides deine Daten sind, gib "Herzlich willkommen!" aus, a

### EA (BMI v2)
Ergänze das BMI-Skript durch die Interpretation des Body-Mass-Indexes bzgl. Unter-, Normal- und Übergewicht. Man kann übrigens if-Anweisungen auch verschachteln. Und außerdem gibt noch 'elif'.

```python
if ...:
  ...
elif ...:
  ...
elif ...:
  ...
else:
  ...
```

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
  + dict `{'schluessel': wert, 'key': value}`

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

### PL (Listen)

```
a = ['alpha','beta', 'gamma', 'delta']
a[2]
a[-1]
a[0:2]
3*a + ['epsilon']
len(a)
a.append('epsilon')
```

Eine Liste zu kopieren ist mit diesem Slicing zu erklären:
`b = a[:]`

```
a = [0,1,0,1,0,1]
a[0]+1
a[0:2] = []
a.sort()
```

```
from random import shuffle
a = [0,1,0,1,0,1]
shuffle(a)
```

Es gibt viele Methoden, Listen zu erzeugen

`list(range(10))`

`[2*i for i in range(4,9)]`

das letzte nennt man **Comprehensions** und ist eine Spezialität von Python.

### EA (Listen-Übungen)

a) Bilde eine Liste der ersten 1000 Quadratzahlen.

b) Erkläre den folgenden Code

```python
a = "Das sind einge willkürlich lange Wörter"
b = a.split()
for x in b:
    print(x, len(x))
```

<!-- Weiter mit while  und dict (Projekt: Vokabeltrainer)-->

<!-- Später
## Einstieg in Kivy

**Uhrzeit**
-->
