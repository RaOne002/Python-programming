# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:48:22 2022

@author: subhr
"""


import random


movies= ["deadpool" ,"avengers" ,"jungleBook" ,"pushpa" ,"enemy" ,"avenger" ,"tadap" ,"ironman" ,"hulk" ,"war"
          ,"endgame" ,"kgf"]

def play():
    p1name =input("Player 1 please enter your name: ")
    p2name =input("Player 2 please enter your name: ")
    pp1 =0
    pp2 =0
    turn =0
    cont =True
    while cont:
        if turn % 2==0:
            # Player 1
            print(p1name ,"your turn")
            picked_movie=random.choice(movies)
            qn =create_question(picked)
            print (qn)
            modified_qn=qn
            not_said =True
            while not_said:
                letter =input("Your letter : ")
                if (is_present(letter ,picked_movie)):                   
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,ch)
                    print(modified_qn)
                    d=input("press 1 to guess the  or 2 to unlock another letter : ")
                    if d== 1:
                       ans=input('Your answer : ')
                       if ans==picked_movie:
                           pp1=pp1+1
                           print('Correct')
                           not_said=False
                           print(p1name,'Your score is : ',pp1)
                       else:
                            print('Wrong ans, Try again')
                        
                else:
                    print(letter ,'not found')
            c=input('Press 1 to continue or 0 to quit')
            if c==0:
                print(p1name, ' Your score is : ',pp1)
                print(p2name,' Your score is : ', pp2)
                print('Thanks for playing')
                cont=False
                
        else:
            #Player 2
            print(p2name ,"your turn")
            picked_movie =random.choice(movies)
            qn =create_question(picked)
            print (qn)
            modified_qn=qn
            not_said =True
            while not_said:
                letter =input("Your letter : ")
                if (is_present(letter ,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,ch)
                    print(modified_qn)
                    d=input("press 1 to guess the  or 2 to unlock another letter : ")
                    if d== 1:
                       ans=input('Your answer : ')
                       if ans==picked_movie:
                           pp1=pp1+1
                           print('Correct')
                           not_said=False
                           print(p1name,'Your score is : ',pp1)
                       else:
                            print('Wrong ans, Try again')
                        
                else:
                    print(letter ,'not found')
            c=input('Press 1 to continue or 0 to quit')
            if c==0:
                print(p1name, ' Your score is : ',pp1)
                print(p2name,' Your score is : ', pp2)
                print('Thanks for playing')
                cont=False
            
        turn=turn + 1