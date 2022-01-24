from os import remove
from pickle import STOP
import random
import sys
from timeit import repeat

Random_Str = ['1','2','3','4','5','6','7','8','9']
list = {'Slot': '  ', 'Slot2': '  ', 'Slot3': ' '}
list2 = {'Slot4': '  ', 'Slot5': '  ', 'Slot6': ' '}
list3 = {'Slot7': '  ', 'Slot8': '  ', 'Slot9': ' '}

def Gameboard():
    print(list['Slot'], " |", list['Slot2'], " |", list['Slot3'])
    print("---", "|", "---", "|", "---")
    print(list2['Slot4'], " |", list2['Slot5'], " |", list2['Slot6'])
    print("---", "|", "---", "|", "---")
    print(list3['Slot7'], " |", list3['Slot8'], " |", list3['Slot9'])

def Tic_Tac_Toe():

    while True:


        Player = input("Choose your move:")

        #Player

        if Player == '1':
            list['Slot'] = ' X'
            Random_Str.remove('1')
        
        elif Player == '2':
            list['Slot2'] = ' X'
            Random_Str.remove('2')
        
        elif Player == '3':
            list['Slot3'] = ' X'
            Random_Str.remove('3')
        
        elif Player == '4':
            list2['Slot4'] = ' X'
            Random_Str.remove('4')
        
        elif Player == '5':
            list2['Slot5'] = ' X'
            Random_Str.remove('5')
        
        elif Player == '6':
            list2['Slot6'] = ' X'            
            Random_Str.remove('6')
        
        elif Player == '7':
            list3['Slot7'] = ' X'
            Random_Str.remove('7')
        
        elif Player == '8':
            list3['Slot8'] = ' X'
            Random_Str.remove('8')
        
        elif Player == '9':
            list3['Slot9'] = ' X'
            Random_Str.remove('9')

        #Winner Player

        if list['Slot'] == ' X' and list['Slot2'] == ' X' and list['Slot3'] == ' X':
            Gameboard()
            print("You win!")
            break

        elif list2['Slot4'] == ' X' and list2['Slot5'] == ' X' and list2['Slot6'] == ' X':
            Gameboard()
            print("You win!")
            break

        elif list3['Slot7'] == ' X' and list3['Slot8'] == ' X' and list3['Slot9'] == ' X':
            Gameboard()
            print("You win!")
            break

        #Winner Player 2

        if list['Slot'] == ' X' and list2['Slot4'] == ' X' and list3['Slot7'] == ' X':
            Gameboard()
            print("You win!")
            break

        elif list['Slot2'] == ' X' and list2['Slot5'] == ' X' and list3['Slot8'] == ' X':
            Gameboard()
            print("You win!")
            break

        elif list['Slot3'] == ' X' and list2['Slot6'] == ' X' and list3['Slot9'] == ' X':
            Gameboard()
            print("You win!")
            break

        #Winner Player 3

        if list['Slot'] == ' X' and list2['Slot5'] == ' X' and list3['Slot9'] == ' X':
           Gameboard()
           print("You win!")
           break

        elif list3['Slot7'] == ' X' and list2['Slot5'] == ' X' and list['Slot3'] == ' X':
            Gameboard()
            print("You lose!")
            break    

        #Computer

        Computer = random.choice(Random_Str)
        print("Computer chose", Computer)

        if Computer == '1':
            list['Slot'] = ' O'
            Random_Str.remove('1')      
        
        elif Computer == '2':
            list['Slot2'] = ' O'
            Random_Str.remove('2')
        
        elif Computer == '3':
            list['Slot3'] = ' O'
            Random_Str.remove('3')
        
        elif Computer == '4':
            list2['Slot4'] = ' O'
            Random_Str.remove('4')
        
        elif Computer == '5':
            list2['Slot5'] = ' O'
            Random_Str.remove('5')
        
        elif Computer == '6':
            list2['Slot6'] = ' O'
            Random_Str.remove('6')
            
        elif Computer == '7':
            list3['Slot7'] = ' O'
            Random_Str.remove('7')
        
        elif Computer == '8':
            list3['Slot8'] = ' O'
            Random_Str.remove('8')   
        
        elif Computer == '9':
            list3['Slot9'] = ' O'
            Random_Str.remove('9')

        Gameboard()

        
        #Winner Computer

        if list['Slot'] == ' O' and list['Slot2'] == ' O' and list['Slot3'] == 'O':
           print("You lose!")
           break

        elif list2['Slot4'] == ' O' and list2['Slot5'] == ' O' and list2['Slot6'] == ' O':
           print("You lose!")
           break
    

        elif list3['Slot7'] == ' O' and list3['Slot8'] == ' O' and list3['Slot9'] == ' O':
           print("You lose!")
           break

        #Winner Computer 2

        if list['Slot'] == ' O' and list2['Slot4'] == ' O' and list3['Slot7'] == ' O':
           print("You lose!")
           break

        elif list['Slot2'] == ' O' and list2['Slot5'] == ' O' and list3['Slot8'] == ' O':
           print("You lose!")
           break

        elif list['Slot3'] == ' O' and list2['Slot6'] == ' O' and list3['Slot9'] == ' O':
           print("You lose!")
           break

        #Winner Computer 3

        if list['Slot'] == ' O' and list2['Slot5'] == ' O' and list3['Slot9'] == ' O':
            print("You lose!")
            break

        elif list3['Slot7'] == ' O' and list2['Slot5'] == ' O' and list['Slot3'] == ' O':
            print("You lose!")
            break
        
Tic_Tac_Toe()

        



