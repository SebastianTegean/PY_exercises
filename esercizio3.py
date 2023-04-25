# ESERCIZIO 2 - TodoApp
# Per poter utillizare il programma bisona installare le seguente librerie: 
#    pip install pyfiglet
#    pip install termcolor

import pyfiglet
import termcolor

attivita = []
nome_app = 'TodoApp'


def vedi_le_attivita():
    '''Funzione che visualizza le attivita'''
    if len(attivita) == 0:
        termcolor.cprint('          Non hai ancora inserito nessuna attivita', 'red')
    else:
        termcolor.cprint('Le tue attivita sono: ', 'green')
        for i in range(len(attivita)):
            termcolor.cprint(f'    {i+1} - {attivita[i]}', 'magenta')


def crea_nuova_attivita():    
    '''Funzione che crea le attivita'''
    attivita.append(input('Inserisci il nome dell\'attivita: '))
    termcolor.cprint('Ho inserito le programma l\'attivita inserita', 'green')


def completa_attivita():
    '''Funzione che completa le attivita'''
    vedi_le_attivita()
    numero_attivita = int(input('Inserisci il numero dell\'attivita da completare: '))
    if numero_attivita > len(attivita):
        termcolor.cprint('Non hai inserito un numero valido', 'red')
    else:
        attivita[numero_attivita-1] = f'{attivita[numero_attivita-1]} - COMPLETATA'
        termcolor.cprint('L\'attivita indicata é stata consegnato come \'COMPETATA\'', 'green')


def elimina_attivita():
    '''Funzione per eliminare le attivita'''
    vedi_le_attivita()
    numero_attivita = int(input('Inserisci il numero dell\'attivita da eliminare: '))
    if numero_attivita > len(attivita):
        termcolor.cprint('Non hai inserito un numero valido', 'red')
    else:
        attivita.pop(numero_attivita-1)
        termcolor.cprint('L\'attivita indicata é elimminata dalla tua lista', 'green')


def esci():
    '''Funzione che mi fa escire dal programma'''
    termcolor.cprint('                                 Grazie per averci giocato                   ', 'red', 'on_yellow', attrs=['bold'])


def main():
    '''funzione principale del gioco TodoApp'''
    termcolor.cprint('_____________________________________________________________________________','green')
    print('\n                     Benvenuto nel programma di gestione delle attivita:')
    termcolor.cprint('_____________________________________________________________________________','green')
    termcolor.cprint(pyfiglet.figlet_format(f'  - {nome_app} -', font = 'slant'), 'blue')
    termcolor.cprint('_____________________________________________________________________________','green')
    while True:
        termcolor.cprint('_____________________________________________________________________________\n','green')
        termcolor.cprint('                    1 - Visualizza le tue attivita', 'blue')
        termcolor.cprint('                    2 - Crea una nuova attivita', 'blue')
        termcolor.cprint('                    3 - Completa un\'attivita', 'blue')
        termcolor.cprint('                    4 - Elimina un\'attivita', 'blue')
        termcolor.cprint('                    5 - Esci dal programma', 'blue')
        termcolor.cprint('_____________________________________________________________________________','green')
        scelta = int(input('Inserisci il numero dell\'azione che vuoi eseguire: '))
        if scelta == 1:
            vedi_le_attivita()
        elif scelta == 2:
            crea_nuova_attivita()
        elif scelta == 3:
            completa_attivita()
        elif scelta == 4:
            elimina_attivita()
        elif scelta == 5:
            esci()
            break
        else:
            print('Non hai inserito un numero valido')

print (main())
