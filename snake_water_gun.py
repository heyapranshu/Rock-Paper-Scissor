import random

print("welcome to the game")

# Dictinoary 

dic = {"r":1,"p":2,"s":3}
reverse_dic = {1:"Rock",2:"Paper",3:"Scissors"}  
choices = {1,2,3}

# choice made by computer

choice_computer = random.choice(list(choices))

# choice made by you

you = input("chosse:\nR for rock\nP for paper\nS for scissors\n").lower()

choice_you = dic[you]

# Printing the Choice

print(f"you choose: {reverse_dic[choice_you]}")
print(f"computer choose: {reverse_dic[choice_computer]}")

# All the conditional statements

if(choice_computer==choice_you):
  print("match is draw")
else:
  if(choice_computer==1) and (choice_you==2):
    print("you win")
    print("You are a genius")

  elif(choice_computer==1) and (choice_you==3):
    print("you loose")
    print("better luck next time")
    
  elif(choice_computer==2) and (choice_you==1):
    print("you loose")
    print("better luck next time")
    
  elif(choice_computer==2) and (choice_you==3):
    print("you win")
    print("You are a genius")

  elif(choice_computer==3) and (choice_you==1):
    print("you win")
    print("You are a genius")

  elif(choice_computer==3) and (choice_you==2):
    print("you loose")
    print("better luck next time")
    
  else:
    print("something went wrong")

