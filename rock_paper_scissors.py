import random

print("WELOCOME TO CARTA FORBICE O SASSO!\n")
start = ""

while start != "y":
    start = input("Vuoi giocare? ").strip().lower()
    if start == "y":
        print("Si comincia!\n")
    else:
        quit()
        
mosse = ["carta",
         "forbice",
         "sasso"
         ]

score1 = 0
score2 = 0

for i in range(1,4):
    guest1 = random.choice(mosse)
    guest2 = input("Fai la tua mossa: ").strip().lower()
    
    if guest2 == guest1:
        print("PAREGGIO!")
    #FORBICE-SASSO
    elif guest1 == "sasso" and guest2 == "forbice":
        print("Hai perso..")
        score1 += 1
    elif guest1 == "forbice" and guest2 == "sasso":
        print("Hai Vinto!")
        score2 += 1
    #CARTA-FORBICE
    elif guest1 == "forbice" and guest2 == "carta":
        print("Hai perso..")
        score1 += 1
    elif guest1 == "carta" and guest2 == "forbice":
        print("Hai Hai Vinto!")
        score2 += 1
    #CARTA-SASSO
    elif guest1 == "carta" and guest2 == "sasso":
        print("Hai perso..")
        score1 += 1
    elif guest1 == "sasso" and guest2 == "carta":
        print("Hai Hai Vinto!")
        score2 += 1
        
print("\n")
if score1 == score2:
    print("PATTA! Bella partita!\n")
elif score1 < score2:
    print("Complimenti! Hai vinto la partita con {} punti!\n".format(score2))
else:
    print("Che peccato... Hai perso la partita..\n")