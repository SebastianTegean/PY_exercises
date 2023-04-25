# ESERCIZIO 1 - Indovina il numero 

import random

def indovina_numero():
    '''Funzione che permette all'utente di indovinare un numero'''
    nome = input('Inserisci il tuo nome: ')
    numero_random = random.randint(0, 100)
    print(f'Ciao {nome} Comincia il giocco!! \n Devi indovinare il numero che ho pensato tra 0 e 100 hai a disposizione 10 tentativi')
    for i in range(10):
        while True:
            try:
                numero_inserito= int(input('Inserisci un numero: '))
            except ValueError:
                print('Non hai inserito un numero: ')
            else:
                break
        
        if numero_inserito < 0 or numero_inserito > 100:
            print('Il numero inserito non è compreso tra 0 e 100')
        if numero_inserito == numero_random:
            print(f'Congratulazioni!!! Hai indovinato il numero al tentativo n.{i+1}')
            break
        if numero_inserito > numero_random:
            print(f'Tentativo n. {i+1} -> Il numero è più piccolo')
            if i == 9:
                print(f'Mi dispiace {nome}! Hai finito i tentativi. Il numero che avevo pensato era {numero_random} ')
        if numero_inserito < numero_random:
            print(f'Tentativo n. {i+1} -> Il numero è più grande')
            if i == 9:
                print(f'Mi dispiace {nome}! Hai finito i tentativi. Il numero che avevo pensato era {numero_random} ')
    return '\n_____________________________________________________________________________'

while True:
    print(indovina_numero())
    risposta = input('Per giocare ancora premi [Enter] \nPer uscire premi [Q]: ')
    if risposta.upper() == 'Q':
        print('Grazie per aver giocato')
        break
