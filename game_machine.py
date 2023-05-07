import random

#DICHIARO LE COSTANTI
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbols_value = {
    "A": 10,
    "B": 8,
    "C": 4,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines
        
def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
            
        columns.append(column)

    return columns
    
#FUNZIONE PER STAMPARE A SCHERMO LA SLOT MACHINE   
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):            
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
        
    
#FUNZIONE PER IL DEPOSITO
def deposit():
    while True:
        amount = input("Quanto vuoi depositare? €").strip()
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:
                break
            else:
                print("L'importo dev'essere maggiore di €0.")        
        else:
            print("Inserisci un numero perfavore.")
        
    return amount

#FUNZIONE PER IL NUMERO DI LINEE DA BATTERE
def get_numbers_of_lines():
    while True:
        lines = input("Scegli il numero di linee su cui scommettere (1-"+ str(MAX_LINES)+ ")? ").strip()
        if lines.isdigit():
            lines = int(lines)
            
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Inserisci un numero valido.")        
        else:
            print("Inserisci un numero perfavore.")
        
    return lines


#FUNZIONE PER DEFINIRE QUANTO BATTERE PER OGNI LINEA
def get_bet():
    while True:
        bet = input("Quanto vuoi scommettere per ogni linea? €").strip()
        if bet.isdigit():
            bet = int(bet)
            
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"L'importo dev'essere compreso tra €{MIN_BET} e €{MAX_BET}.")        
        else:
            print("Inserisci un numero perfavore.")
        
    return bet

def spin(balance):
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"L'importo della scommessa {total_bet} è superiore al tuo bilancio!")
            print(f"Bilancio: €{balance}")            
        else:
            break
    print(f"Stai scommettendo €{bet} su {lines} linee. Il totale della scommessa è di €{total_bet}.")
    
    slots = get_slot_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"Hai vinto €{winnings} su", *winning_lines)
    return winnings - total_bet

#FUNZIONE MAIN PER AVVIARE IL PROGRAMMA
def main():
    balance = deposit()
    while True:
        if balance == 0:
            print("Credito esaurito.")
            deposita = input("Vuoi depositare? (y/n) ").strip().lower()
            if deposita == "y":
                balance = deposit()
            else:
                break
        print(f"Bilancio corrente: €{balance}")
        game = input("Press enter per giocare - q per uscire").strip().lower()
        if game == "q":
            break
        balance += spin(balance)
        
    print(f"Bilancio finale: €{balance}")
    
main()