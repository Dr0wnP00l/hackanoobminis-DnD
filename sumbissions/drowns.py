import random
import time
import re

#Players can create their name
def newName():
    print('>>>Please create a name for your player.<<<')
    global username
    username=input()
    print('Change name to',username,'? (yes or no)')
    nameCheck = input()
    if nameCheck != 'yes':
      return newName()
      
    print('***Name changed to >', username,'<***')
    print('\n\n')
    #time.sleep(3) for game
newName()

def notMade():
  print('\n\nYou have ventured as far as the game allows.\n More In Development!')
  




#Intro scene one        Note: Add  more stories/levels
def introScene():
    print('>Welcome Master', username,'.')
    # time.sleep(2) for game
    print('\n')
    print('>We are glad you have decided to set out on this quest.')
    print('>You are our last hope to reclaim what was righteously ours.')
    #time.sleep(5) for game
introScene()

#Prompt that asks for special replies
def selectReply():
    print('\n')
    print('>>>Please reply by typing one of the numbered options<<<')
    #time.sleep(1) for game
selectReply()

#Unlassicied- Prompts for Scene one
introChoiceOne = ' 1 | What was stolen?'
introChoiceTwo = '2 | Who stole what was yours?'
print(introChoiceOne,'\n',introChoiceTwo)

#Compares user input with prompts
introChoiceInput = input()
introChoiceResponse = int(introChoiceInput)

if introChoiceResponse == 1:
    print('>Master', username, ', our box of jewels was stolen. The box is priceless.')
elif introChoiceResponse == 2:
    print('>Master', username, ', the thief was a large dragon.')
choice = introChoiceResponse
#time.sleep(0.5) for game

print('Try other option\n')

introChoiceInput = input()
introChoiceResponse = int(introChoiceInput)
if choice == introChoiceResponse:
    print("You have already chosen that... Choosing other option")
   # time.sleep(1) for game
    if choice == 1:
        print('>Master', username, ', the thief was a large dragon.')
    else:
        print('>Master', username, ', our box of jewels was stolen. The box is priceless.')
else:
    if choice == 1:
        print('>Master', username, ', the thief was a large dragon.')
    else:
        print('>Master', username, ', our box of jewels was stolen. The box is priceless.')
print('\n')



#scenario
def explainScenario():
  #time.sleep(1.5) for game
  print('>You have already learned that a large  dragon has stolen our possesions.\n'
      +'>The beast lives in Mount Kotrel Kham\n')
 # time.sleep(0.5) for game
  print('>To get to Mount Kotrel Kham, you must pass several obstacle.\n'
      +'>You first need to take the right side road to leave town.\n'
      +'>Keep traveling until you meet the waters edge. Cross over a narrow bridge.\n'
      +'>After a days worth of traveling, you will come to a village, stay clear.\n'
      +'>Travel to Struk Kotrel until you come across the large Mount Kotrel Kham.\n'
      +'>Travel up the mountain. You will then have to decide which cave to enter')
 # time.sleep(15) for game
  print('\n>Good Luck Master',username,'. May you be strong and cunnning!')
  
  
  
def playerReady():
  print('>>>Are you ready to take on the quest? (yes or no)<<<')
  ready = input()
  if ready == "yes":
    print('>>>Good...<<<\n')
    explainScenario()
  elif ready == "no":
    print('>>>You will travel anywys.<<<\n')
    explainScenario()
  else:
    print('Please select yes or no')
    print('\n')
    return playerReady()
playerReady()


# prompts user to type next
def NEXT():
  print('\n')
  print('>>>Type Next to continue...')
  print('\n')
NEXT()


# Game step one -Right road out of town
def stepOneStoryOne():
  ready = input()
  if ready == 'next':
    time.sleep(1)
    print('\n\nAfter talking to the slaves, you decide to continue through town.\n'
          +'You passed by several banks and a gambling palace. You notice that the palace was filled with people.\n'
          +'Contining, you meet the outskirts of town.\n'
          +'You are greeted with two roads.\n'
          #Add a function that asks what do you see for each path
          +'The first road goes straight. The second road goes to the right.')
  else:
     NEXT()
stepOneStoryOne()

def stepOneStoryTwo():
  print('\n\nWhich road should you take?')
  StepOneChoiceOne = ' 1 | Straight'
  StepOneChoiceTwo = '2 | To the right'
  print(StepOneChoiceOne,'\n',StepOneChoiceTwo)
  choiceInput = input()
  choice = int(choiceInput)
  
  if choice == 1:
    #To be made-Long Path -(EASTER EGG)
     notMade()
  elif choice == 2:
    #To be made-Right path
     notMade()
  else:
    print('\n>>>Invalid Response. TRY AGAIN')
    return stepOneStoryTwo()
stepOneStoryTwo()







#def chooseCave():
 #    cave = ''
  #   while cave != '1' and cave != '2' and cave !='3':
   #       print('Select a cave to go into. (1,2,3)')
    #      cave = input()
     #return cave

#chooseCave()
### I'll work on this later when I figure out the story. Kinda Lame ATM
#def checkCave():
  #  global userName
    #print(str(username),' approaches the cave...')
    #time.sleep(2)
    #print('It is dark and spooky...')
    #time.sleep(2)
   # print('A large dragon jumps out in front of ',str(userName),'! He opens his jaws and...')
   # print()
   # time.sleep(2)
#checkCave()

  #  friendlyCave = random.randint(1,3)

    #if chooseCave == str(friendlyCave):
      #  print('Gives ',str(userName),' his treasure!')
   # else:
     #   print('Gobbles ',str(userName),' down in one bite!')

#caveNumber = chooseCave()
#checkCave(caveNumber)