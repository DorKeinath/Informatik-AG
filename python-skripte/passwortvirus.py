#!/usr/bin/env python3
# Die Datei namens datei.txt im Modus "append" öffnen, was bedeutet, dass beim Schreiben hinzugefügt und nicht überschrieben wird. Will man überschreiben, kann man `w` verwenden.
geheim = open("datei.txt", "a")
# Etwas in die Datei schreiben:
geheim.write("Text in der Datei.\n")
# Die Datei schließen. Wenn man das nicht macht, kann die Datei beschädigt werden. Das `\n` bedeutet, dass ein Zeilenumbruch eingefügt werden soll.
geheim.close()
