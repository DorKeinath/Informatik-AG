#!/usr/bin/env python3
i = 1
while i in range(3):
    wunsch = input("Willst du ein I? (J/N)")
    if wunsch == "J":
        print("Du hast jetzt " + str(i) + " I.")
        i += 1
    elif wunsch == "N":
        print ("Dann halt nicht.")
        # Zum Abbrechen der While-Schleife:
        break
    else:
        print("Blödsinn eingeben bedeutet Nein.")
        # Zum Beenden der Ausführung des Skripts:
        exit()
