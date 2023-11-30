import time
import keyboard

def afficher_heure(t):
    global heures
    global minutes
    global secondes
    heures = t[0]
    minutes = t[1]
    secondes = t[2]

def alarme(t):
    global heure_actuelle
    liste_alarme=list(t)
    if liste_alarme == heure_actuelle:
        print("Il est l'or mon seignor!")

while True:                                                                                          # boucle pour continuer le programme si l'input n'est pas bon

    heures=0
    minutes=0
    secondes=0
    affichage_12 = False

    print("pour mettre l'horloge en pause appuyez sur espace, pour la relancer appuyez sur 'p'")
    try:
        tuple_heure = tuple(map(int, input("entrer une heure: heures minutes secondes ").split())) # convertir les inputs en int avec la fonction map et int, puis les convertir en tuple
        tuple_alarme = tuple(map(int, input("entrer une heure pour l'alarme ").split()))             # syntaxe de map : map(fonction, iterable) applique la fonction à tout les iterables
    except:
        tuple_heure =()                                                                              # condition pour ne pas lancer l'horloge

    if tuple_heure != ():
        afficher_heure(tuple_heure)
        while True:
            secondes+=1
            if secondes > 59:
                secondes=0
                minutes+=1
            if minutes > 59:
                minutes=0
                heures+=1
            if heures > 23:
                heures = 0
            heure_actuelle = [heures, minutes, secondes]
            if affichage_12:
                if heures < 12:
                    print(f"{heures:02d}:{minutes:02d}:{secondes:02d} AM", end="\r")
                else:
                    print(f"{heures%12:02d}:{minutes:02d}:{secondes:02d} PM", end="\r")
                alarme(tuple_alarme)
            else:
                print(f"{heures:02d}:{minutes:02d}:{secondes:02d}", end="\r")
                alarme(tuple_alarme)
            if keyboard.is_pressed(" "):            # verifie chaque seconde si espace est pressé ou non
                keyboard.wait("p")                  # attend juqu'a ce que p soit pressé pour continuer la boucle
            time.sleep(1)
    else:
        print("Entrer une heure valide")

