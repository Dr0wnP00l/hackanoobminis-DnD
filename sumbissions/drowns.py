import random
import time

#Players can create their name
def newName():
    print('>>>Please create a name for your player.<<<')
    global username
    username=input()
    print('***Name changed to >', username,'<***')
    print('\n\n')
    time.sleep(3)
newName()


#Intro scene one        Note: Add  more stories/levels
def introScene():
    print('>Welcome Master', username,'.')
    time.sleep(2)
    print('\n')
    print('>We are glad you have decided to set out on this quest.')
    print('>You are our last hope to reclaim what was righteously ours.')
    time.sleep(5)
introScene()

#Prompt that asks for special replies
def selectReply():
    print('\n')
    print('>>>Please reply by typing one of the numbered options<<<')
    time.sleep(1)
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
time.sleep(0.5)

print('Try other option\n')

introChoiceInput = input()
introChoiceResponse = int(introChoiceInput)
if choice == introChoiceResponse:
    print("You have already chosen that... Choosing other option")
    time.sleep(1)
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
  time.sleep(1.5)
  print('>You have already learned that a large  dragon has stolen our possesions.\n'
      +'>The beast lives in Mount Kotrel Kham\n')
  time.sleep(0.5)
  print('>To get to Mount Kotrel Kham, you must pass several obstackles.\n'
      +'>You first need to take the right side road to leave town.\n'
      +'>Keep traveling until you meet the waters edge. Cross over a narrow bridge.\n'
      +'>After a days worth of traveling, you will come to a village, stay clear.\n'
      +'>Travel to Struk Kotrel until you come across the large Mount Kotrel Kham.\n'
      +'>Travel up the mountain. You will then have to decide which cave to enter')
  time.sleep(15)
  print('\n>Good Luck Master',username,'. May you be strong and cunnning!')
  
  
  

print('>>>Are you ready to take on the quest?<<<')
ready = input()
ruready = str(ready)
  
if ruready == 'ready' or 'I am ready' or 'I\'m ready' or 'im ready' or 'yes':
  print('>>>Good...<<<\n')
  explainScenario()
else:
  print('>>>You will travel anywys.<<<\n')
  explainScenario()








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