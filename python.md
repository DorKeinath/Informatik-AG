# Inhalt
<!-- MDTOC maxdepth:6 firsth1:0 numbering:1 flatten:1 bullets:0 updateOnSave:1 -->

1. [Links](#links)   
1.1. [Tutorials](#tutorials)   
1.2. [Python auf Android](#python-auf-android)   
2. [Einstieg in Python](#einstieg-in-python)   
2.1. [PL: Basics](#pl-basics)   
2.2. [EA: Begrüßung](#ea-begrüßung)   
2.3. [EA: Potenz-Berechner](#ea-potenz-berechner)   
2.4. [EA: Kreis-Berechner](#ea-kreis-berechner)   
2.5. [PL: for](#pl-for)   
2.6. [PL: if-else](#pl-if-else)   
2.7. [EA: Passwortabfrage](#ea-passwortabfrage)   
2.8. [EA: Passwortvirus](#ea-passwortvirus)   
2.9. [EA: BMI](#ea-bmi)   
2.10. [PL: while](#pl-while)   
2.11. [EA: Passwortabfrage mit Brute-Force-Defence](#ea-passwortabfrage-mit-brute-force-defence)   
2.12. [PL: Kollektionen](#pl-kollektionen)   
2.13. [PL: Exkurs zu den Bytsequenzen](#pl-exkurs-zu-den-bytsequenzen)   
2.14. [PL: list](#pl-list)   
2.15. [EA: Quadratzahlen](#ea-quadratzahlen)   
2.16. [EA: Schere-Stein-Papier](#ea-schere-stein-papier)   
2.17. [EA: Satz-Statistik](#ea-satz-statistik)   
2.18. [EA: Telefonnummern-Suche](#ea-telefonnummern-suche)   
2.19. [PL: dict](#pl-dict)   
2.20. [EA: Anwesenheitsampel](#ea-anwesenheitsampel)   
3. [Einstieg in Kivy (GUI)](#einstieg-in-kivy-gui)   
3.1. [Widgets und ihr Layout](#widgets-und-ihr-layout)   
3.2. [Übergabe von Objekten zwischen Python- und Kivy-Code](#übergabe-von-objekten-zwischen-python-und-kivy-code)   
3.3. [EA: BMI-Rechner](#ea-bmi-rechner)   
3.4. [EA: Vertiefung](#ea-vertiefung)   

<!-- /MDTOC -->

# Python
## Links

### Tutorials

[Deutsches Python-Tutorial](http://py-tutorial-de.readthedocs.io/de/python-3.3/)

[Noch ein Deutsches Python-Tutorial](http://pythonbuch.com/index.html)

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

<!-- h2 -->

### PL: for

```python
for i in range(10):
  print("Hallo! ", end="")
```

`range(10)` entspricht `[0,1,2,3,4,5,6,7,8,9]`
Was das `end=""` bewirkt, kannst du selbst herausfinden: lösche und vergleiche.

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
Verändere die Passwortabfrage zu einem Virus, der heimlich die eingegebenen Namen und das versuchten Passwörter der Benutzer speichert. So schreibst du in eine Datei:

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

### EA: BMI
Gib den [Body-Mass-Index](https://de.wikipedia.org/wiki/Body-Mass-Index#Berechnung) einer Person aus, indem du sie vorher nach den nötigen Variablen fragst.

Ergänze das BMI-Skript dann durch die Interpretation des Body-Mass-Indexes bzgl. Unter-, Normal- und Übergewicht. Man kann übrigens if-Anweisungen auch verschachteln. Und außerdem gibt noch `elif`.

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

Und ja, man kann das Programm über eine Suchmaschine suchen, aber wenn du den gefundenen Code verwendest, solltest du die Zeilen löschen, mit denen du nichts anfangen kannst (`def ...`), und deine Ausgabe selbst programmieren.

<!-- h3 -->

### PL: while

```python
#!/usr/bin/env python3
i = 1
while i in range(3):
    wunsch = input("Willst du ein I? (J/N)")
    if wunsch == "J":
        print("Du hast jetzt " + str(i) + " I.")
        i += 1
    elif wunsch == "N":
        print ("Dann halt nicht.")
        exit()
    else:
        print("Blödsinn eingeben bedeutet Nein.")
        exit()
```

### EA: Passwortabfrage mit Brute-Force-Defence

Erweitere deine Passwortabfrage so, dass sie gegen eine [Brute-Force](https://de.wikipedia.org/wiki/Brute-Force-Methode)-Attacke geschützt ist.

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

### PL: Exkurs zu den Bytsequenzen
*Mögliches GFS-Thema*
Es gibt verschiedene Zeichentabellen. Die älteste heißt **ASCII**; sie enthält nur 128 Zeichen. Die größte Zeichentabelle heißt **Unicode** und ihre bekannteste Kodierung (engl. "encoding") heißt **UTF-8**. Python3 definiert Strings (`str`) als Unicode-Text.

`text = bytes('Blöde Buchstaben wie äöüß', 'utf-8')`

Das "b" bei der Ausgabe von `text` bedeutet, dass das Folgende als ein Bytestring ist.

`re = text.decode("utf-8")`

### PL: list

```
a = ['alpha','beta', 'gamma', 'delta']
a[2]
a[-1]
a[0:2]
3*a + ['epsilon']
len(a)
a.append('epsilon')
```

Das folgende Slicing ist etwas Besonderes:
`b = a[:]`
Die Liste wird kopiert.

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

das Letzte nennt man **Comprehensions** und ist eine Spezialität von Python.

### EA: Quadratzahlen

Bilde eine Liste der ersten 1000 Quadratzahlen.

### EA: Schere-Stein-Papier
Programmiere "Schere-Stein-Papier"

### EA: Satz-Statistik
Erkläre den folgenden Code

```python
a = "Das sind einige willkürlich lange Wörter"
b = a.split()
for x in b:
    print(x, len(x))
```
### EA: Telefonnummern-Suche
 TODO.
 <!--Siehe Screenshot vom 2017-01-25-10-50-23 -->


### PL: dict
TODO
EA Vokabeltrainer
EA Anwesenheitsampel
<!-- Weiter mit while  und dict (Projekt: Vokabeltrainer)

Dictionaries, auch Maps genannt sind Kollektionen, in denen jedem Schlüssel (key) ein Wert (value) zugeordnet ist.


### EA: Anwesenheitsampel
Programmiere eine Ampel, die anzeigt, ob ein Lehrer in einem kleinen Lehrerzimmer (mit ca. fünf Lehrern) ist. Gib dafür jedem Lehrer eine Zahl vor, damit er beim Hin- und Hinausgehen nur seine Zahl eintippen muss, um seinen Status zu ändern.

> 01 DorKeinath
> 02 DorAndre
> 03 DorDritte

Von außen sehen die Schüler nur die anwesenden Lehrer.

> DorKeinath
-->

## Einstieg in Kivy (GUI)
Es gibt mehrere Möglichkeiten, für dein Python-Programm eine graphische Oberfläche (GUI - Graphical User Interface) zu programmieren. Als Standard ist [Tkinter](https://wiki.python.org/moin/GuiProgramming) vorinstalliert. [appJar](http://appjar.info/) klingt für einen leichten Einstieg richtig attraktiv, muss ich bei Gelegenheit ausprobieren. Im Folgenden beschreibe ich [Kivy](https://kivy.org/), was den Vorteil hat, dass es mit dem [Kivy-Launcher](https://kivy.org/#download) direkt auf dem (Android-)Handy ausgeführt werden kann.

Das **Hallo-Welt-Programm** auf der Kivy-Homepage sieht so aus:

```python
#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hallo Welt')

TestApp().run()
```

Wie du von der Programmierung von Internetseiten bereits weißt, hat es Vorteile, den Inhalt von der Form zu trennen. Dem HTML-Code entspricht hier der Python-Code in einer Datei der Form `*.py`, und dem CSS-Code der Kivy-Code in einer Datei der Form `*.kv`.

Das Hallo-Welt-Programm sieht dann so aus: In der py-Datei steht:

```python
#!/usr/bin/env python3
import kivy
from kivy.app import App

class HalloApp(App):
    pass

if __name__ == '__main__':
    HalloApp().run()
```
Und in der Datei `hallo.kv` steht:

```python
Button:
    text: 'Hallo Welt'
```
Damit das funktioniert, muss der Dateiname der kv-Datei so heißen wie das Wort vor "App" in der py-Datei.

### Widgets und ihr Layout

Will man in einem Fenster etwas erscheinen lassen, spricht man davon, ein Widget hinzuzufügen. Jedes Programm hat ein *root widget*, dem du Kinder-Widgets hinzufügen kannst. Die Zugehörigkeiten der Widgets zueinander kann man in einem hierarchischen Baumdiagramm aufzeichnen. Abhängig davon wie die Kinder-Widgets angeordnet sein sollen, entscheidest du dich für ein **Layout** ([1](https://kivy.org/docs/gettingstarted/layouts.html), [2](https://kivy.org/docs/guide/widgets.html#organize-with-layouts)). Im Folgenden wird das BoxLayout verwendet, damit alle Widgets schön untereinander sind. Im *KivyCatalog* ([1](https://kivy.org/docs/examples/gen__demo__kivycatalog__main__py.html) , [2](https://github.com/kivy/kivy/tree/master/examples/demo/kivycatalog)) kann man die verschiedenen Layouts ausprobieren.

Das Hallo-Welt-Programm kann dann so aussehen:

kivy_hallo_welt_3.py
```python
#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class WurzelWidget(BoxLayout):
    pass

class HalloWidgetApp(App):
    def build(self):
        return WurzelWidget()

if __name__ == '__main__':
    HalloWidgetApp().run()
```
hallowidget.kv
```python
<WurzelWidget>:
    # Mit canvas kann man einen Hintergrund zeichnen
    canvas.before:
        Color:
            rgba: 1, 1, 0.5,0.5
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        Label:
            text: 'Hallo Welt!'
            font_size: '24sp'
            color: 1,1,0,0.5
```

### Übergabe von Objekten zwischen Python- und Kivy-Code

Um eine Aktion des Anwenders deines Programms in deinem Python-Code verarbeiten zu können, muss dein Python-Code auf die Widgets in deinem Kivy-Code zugreifen können. Wenn der Anwender z.B. auf einen Button klickt, soll der Python-Code etwas tun.

**Zugriff auf Text** kann man auf mehreren Wegen kriegen. Um einer Funktion `funktion(self, etwas)` etwas aus einem Widget zu übergeben, verwendet man bei einem Event `root.funktion(etwas)`. Will man wiederum einen damit kreierten Output in einem Widget anzeigen, muss man entweder eine `StringProperty()` definieren oder den Output dem Widget über seine `id` zuweisen. Aus dem folgenden Beispiel kannst du beide Methoden ablesen. (Du solltest allerdings nicht beide Methoden vermischen, sonst funktioniert das was du willst vielleicht nur bei der ersten Ausführung, da die Variable mit einem konkreten Wert überschrieben wird.)

kivy_widget-access.py
```python
#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Login(BoxLayout):
    outpt = StringProperty('Fülle bitte beide Felder aus.') # 1. Weg: Um durch access_widget_1 den text des Labels zu ändern, wird hier eine Variable definiert, auf die der Python- und Kivy-Code dieser Klasse ("Plugin") Zugriff haben.

    def access_widget_1(self,inpt_name,inpt_pwd):
        print('Dein Name ist: {x}'.format(x = inpt_name)) # Erste Möglichkeit etwas Übergebenes im Terminal auszugeben.
        print('Dein Passwort ist: ' + inpt_pwd) # Zweite Möglichkeit etwas Übergebenes im Terminal auszugeben.
        self.outpt = 'Dein Name ist: ' + inpt_name

    def access_widget_2(self,inpt_pwd):
        self.ids["ausgabelabel"].text = 'Dein Passwort ist: ' + inpt_pwd # 2. Weg: Wenn man im Kivy-Code dem Label eine id gegeben hat, kann man auf sie zugreifen. Dieser Weg ist praktisch, aber als "best practice" wird der erste Weg angesehen. Der Vorteil ist hier, dass man im Kivy-Code sehen kann, was im Label-Text ausgegeben wird.

class WidgetAccessApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    WidgetAccessApp().run()
```

widgetaccess.kv
```python
<Login>:
    BoxLayout:
        orientation: 'vertical'
        padding: 100
        spacing: 20

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Name:'
            TextInput:
                id: inpt_name
                text: ''
                focus: True
                multiline: False

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Passwort:'
            TextInput:
                id: inpt_pwd
                text: ''
                password: True
                multiline: False

        Button:
            text: "Los!"
            size_hint: 1, 3
            background_color:  .5, .6, .8, 1
            on_press: root.access_widget_1(inpt_name.text,inpt_pwd.text) # So werden drei Dinge übergeben: Die eigene Instanz und zwei Texte.
            on_release: root.access_widget_2(inpt_pwd.text)

        Label:
            id: ausgabelabel # Um durch access_widget_2 den text dieses Labels ändern zu können.
            text: root.outpt # Wenn im Python-Code festgelegt wurde, dass diese Variable im Besitz ("Property") der Widget ("Login") ist, kann ihr Wert hier angezeigt werden.
            size_hint: 1, 3
            bold: True
            color: .8, .8, 0, 1
```

Bemerkungen zu **self**, **root** und **app**:
Verwendet man eine Variable, muss man sagen, wo sie verwaltet wird. Das `outpt` und die Widget-IDs sind im Mutter-Widget `Login` definiert. Will man in der Funktion `access_widget_1` darauf zugreifen, muss man das mit `self` tun, weil das *aktuelle Widget* beim Ausführen der Funktion das Widget `Login` ist. Im Kivy-Code muss man hingegen mit `root` darauf zugreifen, weil `self` das Label-Widget wäre und man auf die *erste Instanz* in der Hierarchie schauen muss. Definiert man in der App-Klasse (hier `WidgetAccessApp(App)`) etwas, auf das man im Kivy-Code zugreifen will (z.B. `def funktion(self)`), dann macht man das mit `app.funktion()`. [Mehr zu Werten von Properties.](https://kivy.org/docs/api-kivy.lang.html#value-expressions-on-property-expressions-ids-and-reserved-keywords)

Um auf andere Dinge als Text zuzugreifen, z.B. auf den Zustand eines Buttons, ob er gerade gedrückt ist oder nicht, verwendet man andere Properties wie `ObjectProperty`, `ListProperty` oder `RecycleView`. [Mehr zu Properties](https://kivy.org/docs/guide/lang.html#accessing-widgets-defined-inside-kv-lang-in-your-python-code)

### EA: BMI-Rechner
Erweitere deinen BMI-Rechner zu einer App mit graphischer Oberfläche.

### EA: Vertiefung
Um eine App mit mehreren Fenstern zu programmieren, bietet sich der [Screen Manager](https://kivy.org/docs/api-kivy.uix.screenmanager.html) an. Weitere Möglichkeiten von Python und Kivy erfährst du, wenn du die [Examples](https://kivy.org/docs/gettingstarted/intro.html#)
studierst. Hilfe kannst du dir bei [stackoverflow.com](http://stackoverflow.com/questions/tagged/kivy?sort=votes&pageSize=15) holen.
