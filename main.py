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
def INTROresponse():
    introChoiceInput = input()
    global introChoiceResponse
    introChoiceResponse = int(introChoiceInput)

#Returns user submission
def INTROanswer():
    if introChoiceResponse == 1:
        print('>Master',username,', our box of jewels was stolen. The box is priceless.')
    elif introChoiceResponse == 2:
        print('>Master',username,', the thief was a large dragon.')

#Junks the repeats the process for all info above
INTROresponse()        
INTROanswer()
print('Try other option\n')
INTROresponse()
INTROanswer()
print('\n')











def chooseCave():
     cave = ''
     while cave != '1' and cave != '2' and cave !='3':
          print('Select a cave to go into. (1,2,3)')
          cave = input()
     return cave

chooseCave()








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
