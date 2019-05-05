#! /usr/bin/python3
# shebang line damit man es von command line starten kann 
# "#! python3" 			für Windows
# "#! /usr/bin/env python3" 	für OS X
# Passwort Copy clipboard programm
import sys,pyperclip

#PWs
PASSWORDS = {'email': 'PWfürEmailLOL',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'zugang': '12345'}

#Falls nur Programm geöffnet wird ohne Command line Zusatz
if len(sys.argv) < 2:
	print('Benutze: testCode.py [account] - kopiert Account PW')
	sys.exit()
 
#Command line Übergabe an var account
account = sys.argv[1]

#Hebelt Groß/Kleinschreibung aus
korrekturEingabe = account.lower() 

#check & do
if korrekturEingabe in PASSWORDS:
    print("Password ist in Clipboard!")
    pyperclip.copy(PASSWORDS.get(korrekturEingabe, 0))
else:
    print("Nicht gefunden!")

