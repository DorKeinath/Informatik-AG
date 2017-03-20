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

Weiteres Beispiel: Um den Bildschirm zu löschen, kannst du

```
from os import system
system("clear")
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

### EA: Begrüßung
Schreibe ein Python-Skript, das den Aufrufer nach seinem Namen fragt und ihn dann mit seinem Namen und der aktuellen Uhrzeit begrüßt, z.B. "Hallo Python, es ist 12:45 Uhr."

Um die Uhrzeit schön zu formatieren, kannst du aus dem Modul `time` die Funktion `strftime` verwenden:

```python
from time import strftime
print(strftime("%d %b %Y %H:%M:%S"))

```
[Mehr zur Funktion `strftime`]((https://docs.python.org/2/library/time.html#time.strftime))

### EA: Potenz-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einer Basis und einem Exponenten fragt und dann die Potenz berechnet und ausgibt. Hinweis: `2**3` ergibt 8.

### EA: Kreis-Berechner
Schreibe ein Python-Skript, das den Aufrufer nach einem Radius oder Durchmesser eines Kreises fragt und damit den Umfang und Inhalt des Kreises berechnet und ausgibt. Hinweis: Du kannst Pi aus dem Paket `math` verwenden

```python
from math import pi
```

### EA: BMI-Rechner

Gib den [Body-Mass-Index](https://de.wikipedia.org/wiki/Body-Mass-Index#Berechnung) einer Person aus, indem du sie vorher nach den nötigen Variablen fragst.

### PL: for

```python
for i in range(10):
  print("Hallo! ", end="")
```

### PL: if-else

```python
zahl = input("Gib bitte eine natürliche Zahl ein: ")
n = int(zahl)
if n % 2 == 1:
    print("Deine Zahl ist ungerade.")
else:
    print("Deine Zahl ist gerade.")
```

### EA: Passwortabfrage
Lass dir einen Namen und ein Passwort geben. Wenn beides deine Daten sind, gib "Herzlich willkommen!" aus. Falls die Daten nicht mit deinen Daten übereinstimmen gibt eine Fehlermeldung aus.

### EA: Passwortvirus
Verändere eines deiner obigen Programme zu einem Virus, das heimlich den Namen und das Passwort des Benutzers speichert. So schreibst du in eine Datei:

```python
#!/usr/bin/env python3
# Die Datei namens datei.txt im Modus "append" öffnen, was bedeutet, dass beim Schreiben hinzugefügt und nicht überschrieben wird. Will man überschreiben, kann man `w` verwenden.
geheim = open("datei.txt", "a")
# Etwas in die Datei schreiben:
geheim.write("Text in der Datei.\n")
# Die Datei schließen. Wenn man das nicht macht, kann die Datei beschädigt werden.
geheim.close()
```

[Weitere Informationen zum Umgang mit Dateien](https://www.tutorialspoint.com/python/python_files_io.htm)

Erweiterung: Lies mit dem [os-Modul]((https://docs.python.org/2/library/os.html)) heimlich Daten des Benutzers aus und schreibe sie auch in die Datei.


### EA: BMI v2
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

### EA: Anwesenheitsampel
Programmiere eine Ampel, die anzeigt, ob ein Lehrer im Lehrerzimmer ist. Gib dafür jedem Lehrer eine Zahl vor, damit der Lehrer beim Hineingehen nur seine Zahl eintippen muss.

> 01 DorKeinath
> 02 DorAndre
> ...

### PL: Kollektionen

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

### PL: Listen

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

### EA: Listen-Übungen

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
