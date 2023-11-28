import time

def afficher_heure(t):
    global h
    global m 
    global s
    h = t[0]
    m = t[1]
    s = t[2]

def alarme(t):
    global heure_actuelle
    liste_alarme=[]
    for i in t:
        liste_alarme +=[i]
    if liste_alarme == heure_actuelle:
        print("Il est l'or mon seignor!")



h=0
m=0
s=0
tuple_heure = (15, 40, 30)
tuple_alarme = (15, 40, 35)


afficher_heure(tuple_heure)
while True:
    s+=1
    if s > 59:
        s=0
        m+=1
    if m > 59:
        m=0
        h+=1
    if h > 24:
        h = 0
    heure_actuelle = [h, m, s]
    print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")
    alarme(tuple_alarme)
    time.sleep(1)

