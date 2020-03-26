import random
import time

#Einleitung
print("****************************") ; time.sleep(0.5)
print("* Schere | Stein | Papier |*") ; time.sleep(0.5)
print("****************************\n\n") ; time.sleep(0.5)

#Variablen
figuren = ("Schere", "Stein", "Papier")
spielen = True

while spielen:
    
    #Spielerfigurauswählen
    spielerauswahl = 0
    while spielerauswahl not in (1,2,3):
        spielerauswahl = int(input("[1]Schere [2]Stein [3]Papier\n"))
    Spielerfigur = figuren[spielerauswahl - 1]
    
    #Computerauswahl
    computerfigur = figuren[random.randint(0,2)]
    
    #Siegerermittelung
    if Spielerfigur == computerfigur:
        print("Unentschieden! Computer wählte", computerfigur)
    else :
        
        if Spielerfigur == "Schere":
            if computerfigur == "Stein":
                print("Verloren! Computer wählte", computerfigur)
            else:
                print("Gewonnen! Computer wählte", computerfigur)
                
        if Spielerfigur == "Stein":
            if computerfigur == "Schere":
                print("Gewonnen! Computer wählte", computerfigur)
            else:
                print("Verloren! Computer wählte", computerfigur)
                
        if Spielerfigur == "Papier":
            if computerfigur == "Schere":
                print("Verloren! Computer wählte", computerfigur)
            else:
                print("Gewonnen! Computer wählte", computerfigur)
                
    #Restart
    time.sleep(1)
    entscheidung = ""
    while entscheidung not in ("y", "n"):
        entscheidung = input("\nNochmal spielen? [y]Ja [n]Nein")
    if(entscheidung == "n"):
        spielen = False
    