
print("Lets play Stone, Paper and Scissor")

def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print('Draw')
    elif(player_one[p1]=='Stone' and player_two[p2]=='Paper'):
        print(Player_two,'you win')
    elif(player_one[p1]=='Stone' and player_two[p2]=='Scissor'):
        print(Player_one,'you win')
    elif(player_one[p1]=='Paper' and player_two[p2]=='Stone'):
        print(Player_one,'you win')
    elif(player_one[p1]=='Paper' and player_two[p2]=='Scissor'):
        print(Player_two,'you win')
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Paper'):
        print(Player_one,'you win')
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Stone'):
        print(Player_two,'you win')



Player_one=input('Player one please enter your name = ')
Player_two=input('Player two please enter your name = ')
player_one={0:'Stone', 1:'Paper', 2:'Scissor'}
player_two={0:'Scissor', 1:'Stone', 2:'Paper'}
while(1):
    num1=input('player_one, Please enter your choice = ')
    num2=input('player_two, Please enter your choice = ')
    bit1=int(input('player_one, Please enter your secret bit number = '))
    bit2=int(input('player_two, Please enter your secret bit number = '))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input('DO you want to continue? y/n ')
    if(ch=='n'):
        print('Thank you for playing this game')
        break


















