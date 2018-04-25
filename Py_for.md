# Python

<!-- MDTOC maxdepth:4 firsth1:3 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [for, if else, elif, range, Dateien](#for-if-else-elif-range-dateien)   
      - [sdas](#sdas)   
   - [for](#for)   
   - [if-else](#if-else)   
   - [EA: Nerv-Virus](#ea-nerv-virus)   
   - [EA: Passwortabfrage](#ea-passwortabfrage)   
   - [EA: Passwortvirus](#ea-passwortvirus)   
   - [EA: BMI](#ea-bmi)   

<!-- /MDTOC -->

## for, if else, elif, range, Dateien

teste2wer
#### sdas

### for

```python
for i in range(10):
  print("Hallo! ", end="")
```

`range(10)` entspricht `[0,1,2,3,4,5,6,7,8,9]`
Was das `end=""` bewirkt, kannst du selbst herausfinden: lösche und vergleiche.

### if-else

```python
zahl = input("Gib bitte eine natürliche Zahl ein: ")
n = int(zahl)
if n % 2 == 1:
    print("Deine Zahl ist ungerade.")
else:
    print("Deine Zahl ist gerade.")
```

### EA: Nerv-Virus
Schreibe ein Programm, bei dessen Aufruf nervig viele Fenster eines Programms geöffnet werden.
Tipp: [`subprocess`](#import-asctime-subprocess), [`disown`](terminal.md)

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

Erweiterung: Lies mit dem [`subprocess`]()-Modul heimlich Daten des Benutzers aus und schreibe sie auch in die Datei.

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
