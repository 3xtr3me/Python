#importing files
import time
import random
#defining the variables
List=["Rock","Paper","Scissors"]
#Rock = 0
#Paper = 1
#Scissors = 2
#Taking the input from the user
a=input("Choose your weapon Rock,Paper,Scissors\n")
#Making the computer choose the weapon
print("Computer is choosing a weapon")
time.sleep(3)
comp = random.choice(List)
time.sleep(1)
print(f"***{List[0]}***")
time.sleep(1)
print(f"***{List[1]}***")
time.sleep(1)
print(f"***{List[2]}***")
time.sleep(1)
print("SHOOT!")
print(comp)
if a == comp:
    print(f"the User chose {a} and CPU chose {comp} It's a DRAW!")
elif a == "Rock":
    if comp == "Scissors":
        print("YOU WIN!")
    else:
        print("CPU WINS!.")
elif a == "Paper":
    if comp == "Rock":
        print("YOU WIN!")
    else:
        print("CPU WINS.")
elif a == "Scissors":
    if comp == "paper":
        print("YOU WIN!")
    else:
        print("CPU WINS!.")

