# Git mit GitHub

[GitHub](https://github.com/) bietet die Möglichkeit an, eine Internetseite unter einer Domain der Form *username.github.io* zu veröffentlichen. Dazu kann man wie folgt vorgehen.

Was hier verwendet wird ist das Programm namens [Git](https://de.wikipedia.org/wiki/Git). Es ist ein Standardprogramm zum Arbeiten mit Versionskontrolle und dem Terminal.
GitHub ist eine Plattform, auf der Code gehostet werden kann. Extrem viele OpenSource-Programme nutzen GitHub.

1. Sich auf der Internetseite von GitHub einloggen
1. Auf `New repository` klicken.
1. Unter `Repository name` seinen Benutzernamen verwenden, um **username.github.io** anzulegen.
1. Auf dem PC in das Verzeichnis gehen, in dem die `index.html` liegt.
1. Hier das Terminal öffnen und die auf der GitHub-Seite vorgeschlagenen Befehle eingeben, z.B.

```bash
git init
git add --all
git commit -m "bla"
git remote add origin https://github.com/DorKeinath/username.github.io.git
git push -u origin master
```

Eine gute vertiefende Anleitung für Git: [https://githowto.com/](https://githowto.com/)

## Workflow

```bash
git add *
git commit -m "Nachricht"
git push

```

## Weitere nützliche Git-Befehle

```
# Status
git status

# Datei vom Server zurückholen
git checkout -- <filename>

# Alle Änderungen und Löschungen updaten
git add -u

# Datei löschen
git rm test.md

# Alle gelöschten Dateien löschen
git ls-files --deleted -z | xargs -0 git rm

# Änderung in einer Datei verwerfen
git checkout -- folder/file.md

# Repository hinzufügen
git clone https....git

# Falls ein 'Merge conflict' auftritt
git mergetool

```
