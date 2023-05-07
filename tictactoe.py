import random

#CREO IL TAVOLO DA GIOCO
board = [" " for i in range(9)]

#FUNZIONE PER STAMPARE IL TAVOLO DA GIOCO
def print_board():
    riga1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    riga2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    riga3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(riga1)
    print(riga2)
    print(riga3)
    print()
    
#FUNZIONE MULTIPLAYER
def multi_player(icon):
    if icon == "X":
        player = player1
    else:
        player = player2
    
    mossa = int(input(player+", fai la tua mossa(1-9): ".strip()))
    mossa -= 1
    while True:
        if  mossa > 8 or mossa == -1:
            mossa = int(input("Mossa non valida. Inserisci una mossa valida: ".strip()))
            mossa -= 1
        else:
            if board[mossa] == " ":
                board[mossa] = icon
                break
            else:
                mossa = int(input("Posizione occupata. Inserisci una mossa valida: ".strip()))
                mossa -= 1

#FUNZIONE SINGLE PLAYER
def single_player(icon):
        if icon == "X":
            player = player1
            mossa = int(input(player+", fai la tua mossa(1-9): ".strip()))
            mossa -= 1
            while True:
                if  mossa > 8 or mossa == -1:
                    mossa = int(input("Mossa non valida. Inserisci una mossa valida: ".strip()))
                    mossa -= 1
                else:
                    if board[mossa] == " ":
                        board[mossa] = icon
                        break
                    else:
                        mossa = int(input("Posizione occupata. Inserisci una mossa valida: ".strip()))
                        mossa -= 1
        else:
            mossa = int(random.randint(0,8))
            while True:
                mossa = int(random.randint(0,8))
                if board[mossa] == " ":
                    board[mossa] = icon
                    print(f"PC fa la sua mossa:{str(mossa+1)}")
                    break
                else:
                    mossa = int(random.randint(0,8))
            
            
            
#FUNZIONE PER STABILIRE CHI HA VINTO
def victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
    else:
        return False    

#FUNZIONE PER PARITA'
def patta():
    if " " not in board:
        return True
    else:
        return False


#GAMEPLAY
while True:
    mode = input("Inserisci la modalità di gioco(m/s/q): ")
    if mode not in ["m","s","q"]:
        print("Modalità non valida")
    elif mode == "q":
        quit()
    else:
        if mode == "m":
            player1 = input("Player_1: ").strip().capitalize()
            player2 = input("Player_2: ").strip().capitalize()
            while True:
                print_board()
                multi_player("X")
                if victory("X"):
                    print("X VINCE!")
                    print_board()
                    quit()
                elif patta():
                    print("PATTA!")
                    print_board()
                    quit()
                                
                print_board()
                multi_player("O")
                if victory("O"):
                    print("O VINCE!")
                    print_board()
                    quit()
                elif patta():
                        print("PATTA!")
                        print_board()
                        quit()
        elif mode == "s":
            player1 = input("Player_1: ").strip().capitalize()
            while True:
                print_board()
                single_player("X")
                if victory("X"):
                    print("X VINCE!")
                    print_board()
                    quit()
                elif patta():
                    print("PATTA!")
                    print_board()
                    quit()
                                
                print_board()
                single_player("O")
                if victory("O"):
                    print("O VINCE!")
                    print_board()
                    quit()
                elif patta():
                        print("PATTA!")
                        print_board()
                        quit()