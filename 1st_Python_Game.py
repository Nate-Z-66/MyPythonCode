import random
Player = int(input("rock,1  paper,2  scissors,3: "))
Computer = random.randint(1, 3)

if((Player == 1 and Computer == 3) or (Player == 2 and Computer == 1) or (Player == 3 and Computer == 2)) :
        print ("Player Wins")
        print(Computer)
elif Player == Computer :
        print ("Tie")

else :
        print ("Computer wins")
        print(Computer)

