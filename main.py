import time

def afficher_heure(t):
    global heures
    global minutes
    global secondes
    heures = t[0]
    minutes = t[1]
    secondes = t[2]

#regarder .extend pour ajouter éléments a une liste
def alarme(t):
    global heure_actuelle
    liste_alarme=[]
    for i in t:
        liste_alarme +=[i]
    if liste_alarme == heure_actuelle:
        print("Il est l'or mon seignor!")



heures=0
minutes=0
secondes=0
tuple_heure = (15, 40, 30)
tuple_alarme = (15, 40, 35)
affichage = True


afficher_heure(tuple_heure)
while True:
    secondes+=1
    if secondes > 59:
        secondes=0
        minutes+=1
    if minutes > 59:
        minutes=0
        heures+=1
    if heures > 24:
        heures = 0
    heure_actuelle = [heures, minutes, secondes]
    if affichage:
        if heures < 12:
            print(f"{heures:02d}:{minutes:02d}:{secondes:02d} AM", end="\r")
        else:
            print(f"{heures%12:02d}:{minutes:02d}:{secondes:02d} PM", end="\r")
        alarme(tuple_alarme)
    else:
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}", end="\r")
        alarme(tuple_alarme)
    if #touche P préssé:
        while true:
            if # touche r préssé:
                break
    time.sleep(1)
    

