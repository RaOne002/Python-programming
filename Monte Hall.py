# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:09:21 2022

@author: subhr
"""

# MONTE HALL GAME


import random


doors=[0]*3
goatdoor=[0]*2
swap=0
dont_swap=0
cont=1
while(cont==1):
    cont=int(input('Press 1 to continue and 0 to end = '))
    if(cont==1):    
        x=random.randint(0,2)
        doors[x]='BMW'
        for i in range(0,3):
            if (i==x):
                continue
            else:
                doors[i]="Goat"
                goatdoor.append(i)
        choice=int(input("Enter your choice 0, 1 or 2 = "))
        door_open=random.choice(goatdoor)
        while (door_open==choice):
            door_open=random.choice(goatdoor)
        ch = input("DO you want to swap? y/n = ") 
        if (ch=='y'):
            if (doors[choice]=="Goat"):
                print("You win")
                swap=swap+1
            else:
                 print('You loose')
        else:
            if(doors[choice]=='Goat'):
                print('you loose')
            else:
                print 
                ('You win')
                dont_swap=dont_swap+1
        print(swap)
        print(dont_swap) 

    else:
        print('Thank you for playing this game')
   
        
       









 
    