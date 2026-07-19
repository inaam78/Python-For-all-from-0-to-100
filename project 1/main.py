import random
computer=random.choice([1,-1,0])
yourstring=input("Enter your choice : ")
yourdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=yourdict[yourstring]
print(f"you chose {reversedict[you]}\nComputer chose {reversedict[computer]}")
if (computer==you):
    print("its a draw")
else:
    if(computer==1 and you==-1):
        print("you lose")
    elif(computer==-1 and you==1):
        print("you win")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==0 and you==-1):
        print("you win")
    else:
        print("Something went wrong")

    
"""
rules of the game:
| Player 1 | Player 2 | Winner |
| -------- | -------- | ------ |
| Snake    | Water    | Snake  |
| Water    | Snake    | Snake  |
| Snake    | Gun      | Gun    |
| Gun      | Snake    | Gun    |
| Water    | Gun      | Water  |
| Gun      | Water    | Water  |
| Same     | Same     | Draw   |

"""