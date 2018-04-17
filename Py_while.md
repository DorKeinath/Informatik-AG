# Python

## while

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
