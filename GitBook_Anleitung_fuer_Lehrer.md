Anleitung zu GitBook (für Lehrer)
==================================
## Vorbereitung
* GitBook anlegen (s.u.)
* Piratenpad anlegen
* Die folgenden Links in einem Tausch- oder Projektordner für die Schüler bereit stellen.
	* https://www.piratenpad.de/
	* https://www.gitbook.com/
	* Link zum GitBook https://www.gitbook.com/book/mgb-klasse-9/merkheft-der-klasse-9c/details

## Erste Stunde
Als Handout und Datei im Projektordner bereit stellen: [GitBook_HO_Erste_Stunde.md](GitBook_HO_Erste_Stunde.md)

Die Schüler gehen nach dieser Anleitung vor.

Das **Mergen der Branches** funktioniert nur, wenn die im Master vorhandenen Dateien nicht verändert wurden. Haben die Schüler eine Datei über das Inhaltsverzeichnis hinzugefügt, müssen sie vor dem Mergen die SUMMARY.md händisch bearbeiten: Ihre Einträge löschen. (Am Ende sind zwei Leerzeilen.). Es bietet sich daher an, dass die Schüler von Anfang an ihre Dateien per Rechtsklick auf *Files Tree* erstellen (wie in der Anleitung zu GitBook (für Schüler) beschrieben).

Die **Rechtschreibprüfung** kann man oben rechts auf Deutsch umstellen, indem man direkt auf das Einstell-Rad klickt und zum Tab Proofreader geht.



______________________________________________________________________________

Anhang
==========
### Beispiel für die Beschreibung eines GitBooks
Das bewundernswerte Merkheft der Klasse 9c
=======

Hier trägt die Klasse wichtige Erkenntnisse zusammen.


Hinweise für die Klasse 9c
---------------------------

1. Der Text muss in Markdown formatiert sein. Dazu kann man die Buttons oben links verwenden. Für speziellere Formatierungen kann man in der Hilfe (oben rechts beim Einstellungs-Rad) schauen oder nach Markdown im Internet suchen.
2. Formeln muss man programmieren. Siehe unter der Hilfe beim Stichwort *Math & TeX*. [Befehlsliste auf Wikipedia](https://de.wikipedia.org/wiki/Hilfe:TeX).

    Zum Beispiel gilt die Mitternachtsformel für $$a \ne 0$$:
    
    $$ax^2 + bx + c = 0 \; \Leftrightarrow \; x_{1, 2} = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

______________________________________________________________________________
### Text des GitBook_HO_Erste-Stunde
Liebster Schüler, liebste Schülerin,

um einen Beitrag für euer GitBook zu schreiben, musst du wie folgt vorgehen. **Kein Schritt darf übersprungen werden!** Sonst funktioniert's am Ende nicht.

Verwende für alle Internetseiten am besten Firefox und nicht den Internet-Explorer.

1. Erfinde für dich ein [Pseudonym] und trägt ihn auf dem **Piratenpad** ein. (Den Link zum Piratenpad findest du im Projekt-Ordner.)
* Suche dir einen Partner. 
* Entscheidet euch, zu welchem **Thema/Teilkapitel** ihr einen Beitrag schreiben wollt. Ergänzt im Piratenpad hinter euren Pseudonymen euer Thema.
* Gehe auf [https://www.gitbook.com] und **registriere** dich wie folgt: 
	+ Als *username* nimmst du dein Pseudonym, 
	+ als *email address*nimmst du deine eigene E-Mail-Adresse oder psyeudonym@instant-mail.de 
	+ und als *password* nimmst du ein eigenes Passwort, das du dir am besten merkst und aufschreibst.
* Gehe danach in dein WebMail oder auf [http://www.instant-mail.de] und checke deine bzw. die E-Mails von psyeudonym@instant-mail.de. In der confirm-Mail kopierst du den **confirm-Link** ("http..." ohne den letzten ".", der den Satz beendet) und öffnest ihn in einem neuen Tab, um dich damit bei gitbook zu registrieren. In der E-Mail klickst du danach am besten auf "Löschen".
* Der Lehrer fügt dich inzwischen mit Hilfe der Liste auf dem Piratenpad als Collaborator beim GitBook hinzu.
* Dann kannst du den **Link zum GitBook** aufrufen, den du im Projekt-Ordner findest. Hier klickst du auf **"Edit"**. *Dann erst mal nichts tun! Erst den nächsten Punkt beachten!*
* Bevor du irgend wo drauf klickst oder etwas schreibst, musst du *immer* zuerst einen **New Branch** erstellen, z.B. mit dem Kapitelnamen. Einen Branch erstellst du oben rechts bei "master".
* Jetzt könnt ihr mit dem Schreiben loslegen. Unten links findet ihr eine **Anleitung zu GitBook (für Schüler)**

[Pseudonym]: https://de.wikipedia.org/wiki/Pseudonym
[http://www.instant-mail.de]: http://www.instant-mail.de/
[https://www.gitbook.com]:  https://www.gitbook.com/
