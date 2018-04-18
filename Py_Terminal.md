# Python

## Terminal-Skripte

Mit Python kann man Terminal-Skripte schreiben, die man mit Argumenten (z.B. `-h`) oder *positional arguments* (z.B. `less datei.txt`) aufrufen kann. Will man sie schön schreiben, verwendet man das Modul `argparse`. Das Modul erzeugt dann auch automatisch eine Hilfe, die der Benutzer des Programms mit dem üblichen `-h` aufrufen kann.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from subprocess import call
from shlex import split

def eine_funktion(argument_eins, positionsargument):
    print('Der Funktion namens eine_funktion wurde die Argumente ' + argument_eins + ' und ' + positionsargument + ' übergeben.')
    call(split('echo Terminalbefehle kann man auch aufrufen.'))

if __name__ == '__main__':
    # Eine Beschreibung des Programms, die beim Aufruf der Hilfe (-h) angezeigt wird.
    parser = argparse.ArgumentParser(description='Dieses Programm erläutert die Funktionsweise von argparse.')
    # Ein klassisches Argument
    parser.add_argument('-a',
                            dest='argument_eins',
                            type=str,
                            help='Irgend ein Text, den der Benutzer eingeben kann.')
    # Ein Positionsargument
    parser.add_argument('positionsargument',
                            metavar='positionsargument',
                            type=str,
                            help='Irgend ein Text, den der Benutzer hinter dem Dateiname des Programms eingeben muss.')
    # Ein Argument das einen bestimmten Wert speichert
    parser.add_argument('-v',
                            dest='variable',
                            action='store_const',
                            const=True,
                            default=False,
                            help='Speichert in der Variablen args.variable den Wert True.')

    args = parser.parse_args()

    if args.argument_eins is None:
        args.argument_eins = raw_input("Argument: ")

    eine_funktion(args.argument_eins, args.positionsargument)

```
