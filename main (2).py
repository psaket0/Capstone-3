import random
import string

usercave = ''

def getUserName ():
  user_name = input("what is your name?")
  return user_name

def printUser():
  
  print("Hello welcome to the dragon cave game " + uname+"!!")

  print("Here are the rules of the game:")
  print("You must choose a cave and a dragon will meet you on the other end.") 
  print("The dragon will give you one good response or two bad respones.")
  print("Pick carefully!")

def chooseCave():
  cave=''
  while cave !='1' and cave!='2' and cave !='3':
    print("pick a cave number.")
    cave = input()
  return cave

def checkCave():
  friendlycave = random.randint(1,3)
  #print ("Debug = friendly" + str(friendlycave) )
  #print ("Debug = userselected:" + usercave)
  
  if(int(usercave) == friendlycave):
    print("Good Job! The Dragon will give you some cookies!")
  else:
    if (int(usercave) == 1 and usercave != friendlycave):
        print ("Dragon will roast you with fire!")
    elif (int(usercave)== 2 and usercave != friendlycave):
        print("Dragon will throw you in dungeon!")
    elif (int(usercave) == 3 and usercave != friendlycave):
        print("Dragon will throw you in dungeon!")

      
playagain = 'y'
while (playagain == 'yes' or playagain == 'y'):
  uname = getUserName()
  printUser()
  usercave = chooseCave()
  checkCave()

  print ('Do you want to play again? (yes or no)')
  playagain = input()

  



