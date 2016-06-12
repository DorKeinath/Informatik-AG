# Microcontroller von Festo
*Die Schüler programmieren einen Microcontroller, der von Firma digiraster GmbH in Stuttgart entwickelt und der Schule von der Hopp-Foundation gesponsert wurde.*

![Festool](files/festool.jpg)

## Erste Schritte
* Programm **EasyKitProgrammierung - EasyLab Starter** starten.
* Unten rechts bei "Hinzufügen" das *Mini Base Board* hinzufügen.
* Bausteine ins Arbeitsfenster ziehen und miteinander verbinden, z. B. einen Joystick und eine LED.
* In den **Code-Erzeugungsmodus** wechseln.
* Bei Codeerzeugung **EasyKit Mini (Standalone)** auswählen.

*Die Schüler bekommen ein Handout mit Erklärungen zu den wichtigsten Bausteinen.*

## Aufgaben
*Lösungen können beim Lehrer eingesehen werden*
1. Ampelschaltung.
	1. Zwei Phasen: Rot und Grün, Grün soll drei Mal so lange dauern wie Rot.
	2. Mit den folgenden Bausteinen: Konstante, $$>=$$, Schrittfunktion, Dreipunktregler, Typumwandlung, Negation, LEDs.
	3. Taster zum vorzeitigen Abbruch hinzufügen. (Joystick, vorderflankengesteuerte T-Kippstufe, Schrittfunktion, Konstante, $$>=$$.)
1. Beschleunigungsanzeige (3 Beschleunigungssensoren, 3 Testschreiber, OLED-Bildschirm).
1. Beschleunigungslinie.
1. Uhr.
1. Trigonometrische Funktion (u.a. Schrittzähler und Oszilloskop).

# Microcontroller Arduino

## Einstiegsaufgaben
* Mindestens Nr. 1 im Plenum.*

1. Lampe blinken lassen.
2. 5 Lampen blinken lassen (for-Schleife).
    1. Alle gleichzeitig
    1. Nacheinander
    1. Night-Rider
    1. Night-Rider mit zwei Lampen

## Zu beachten

 * Bei i=2 beginnen
 * Lampen versetzt ins Steckbrett
 * Vorwiderstände
 * Minuspol schwarz (ground)
 * Pluspol in den richtigen Pin
 * Unter Tools den Port ändern (nicht 6)
