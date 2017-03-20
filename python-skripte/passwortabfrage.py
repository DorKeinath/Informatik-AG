#!/usr/bin/env python3
from os import system

name = input("Name: ")
passwort = input("Passwort: ")
system('echo "tr -c '[:digit:]' ' ' < /dev/urandom | dd cbs=$COLUMNS conv=unblock | GREP_COLOR='1;32' grep --color '[^ ]'"')
if (name == "Ich") and (passwort == "sicher"):
    print("Herzlich willkommen!")
else:
    print ("Du bist nicht ich oder hast dich vertippt.")
