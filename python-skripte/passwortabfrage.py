#!/usr/bin/env python3
from os import system

name = input("Name: ")
passwort = input("Passwort: ")
if (name == "Ich") and (passwort == "sicher"):
    print("Herzlich willkommen!")
else:
    print ("Du bist nicht ich oder hast dich vertippt.")
