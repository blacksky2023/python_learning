
#CREA UNA LISTA DI NUMERI INTERI E,
#STAMPA SOLO I NUMERI DIVISIBILI PER 3
print("ESERCIZIO 1")
print("crea una lista di 100 numeri interi ed inserisci in una seconda ilsta solo quelli divisibili per 3.\n")
#creo una lista vuota
lista = []
num = 0
#inserisco con un for loop, 100 numeri nella lista
for _ in range(100):
    lista.append(num+1)
    num += 1
#creo la seconda lista
divisibili = []
#per ogni numero divisibile per 3 lo inserisco nella lista "divisibili[]"
for div in lista:
    if div % 3 == 0:
        divisibili.append(div)       
#stampo la lista dei numeri divisibili
print(str(divisibili)+ "\n")

##############################################################################################################

print("ESERCIZIO 2")
print("crea una tupla che contenga dei nomi. Solo se la lunghezza del nome è pari, stampalo a schermo.\n")
#creo una tupla
tupla = ("anna", "marco", "michele", "edoardo", "giacomo", "lorena")
print("Tupla: "+ str(tupla))
#per ogni nome nella tupla, se la lunghezzadel nome diviso 2 è uguale a 0 allora stampala
for nome in tupla:
    if len(nome) % 2 == 0:
        print("Nome dalla lunghezza pari: "+nome)
print("\n")

##############################################################################################################

print("ESERCIZIO 3")
print("creo un set ed una lista. Ogni numero in comune viene aggiunto in una seconda lista e stampato a schermo.\n")
#creo un set
numeri_set = {1,2,4,6,7,8,9,43,20}
#creo una lista
numeri_lista = [2,3,5,6,8,20,30,43,24]
#creo una seconda lista che conterrà i numeri in comune
numeri_comuni = []
#stampo il set e la lista a schermo
print("Numeri nel set: "+str(numeri_set))
print("Numeri nella lista: "+str(numeri_lista))
#per ogni numero in numeri_set, se il numero è in numeri_lista, appendilo in numeri_comuni
for num in numeri_set:
    if num in numeri_lista:
        numeri_comuni.append(num)
#stampo i numeri in comune
print("Numeri in comune: "+ str(numeri_comuni))
print("\n")

##############################################################################################################

print("ESERCIZIO 4")
print("Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi.")
print("Suddividere in base al valore >/< di 18 in 2 ulteriori dizionari, uno conterrà i Maggiorenni e l'altro i Minorenni.\n")

dizionario = {"Mario":15,"Michele":25,"Marco":17,"Maurizio":19}

print("Dizionario: "+ str(dizionario))

diz_minorenni = {}
diz_maggiorenni = {}

for nome, val in dizionario.items():
    if val > 18:
        diz_maggiorenni[nome] = val
    else:
        diz_minorenni[nome] = val
        
print("Minorenni: "+str(diz_minorenni))
print("Maggiorenni: "+str(diz_maggiorenni))
print("\n")
