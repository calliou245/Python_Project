user_response = 0

#- This function is what starts the entire story/game
def begin_story():
  print("You were in a private plane flying over the jungles in africa when all of a sudden your pilot has a heart attack. The plane is rapidly dropping.")
  print("What do you do?")
  user_response= int(input("1.Call over the radio asking for help. \n 2.Push the pilot out of the way and try to fly the plane yourself."))
  decision1(user_response)
  
#aperson2nice - fixed the problem with this function
def decision1(user_response):
  print("select 1 or 2")
  if user_response == 1:
    print("No one replied in time. The plane went down and unfortunatley you did not survive.")
    user_response = int(input())
    loser()
  elif user_response == 2:
    print("The pilot was strapped down in seatbelts.")
    print("What do you do?")
    user_response = int(input())
    decision2()
    
def decision2():
  print("1.Cut the seatbelts with a knife you have strapped to your belt \n 2. Press the button to release the seatbelts like a normal person")
  if (user_response == 1):
    decision3a()
  elif(user_response == 2):
    decision3b()
    
    user_response = int(input())
def decision3a():
  print("You cut the strap and the pilot is now on the floor but while doing so you slashed your arm.")
  print("1.Apply first aid to the wound \n 2. Try and fly the plane.")
  decision4a()
  
  user_response = int(input())
def decision4a():
  if(user_response == 1):
    decision4ab()
  elif(user_response == 2):
    decision4aa()
    
    user_response = int(input())
def decision4aa():
  print("The plane is going down you grab the yoke")
  print("what do you do?")
  print("1.Push the yoke down.\n 2.Pull yoke up.")
  decision5()
  
  user_response = int(input())
def decision5():
  if(user_response == 1 ):
    print("The plane crashes down too fast and you die in a horrible crash")
    loser()
  elif(user_response == 2):
    flying()  

  user_response = int(input())
def flying():
  print("The plane is now steady and you notice the fuel is running low")
  print("1.Call over radio for any help. \n 2.Try and look for a place to land \n 3.Look for a place to crash land.")
  decision6()
  
  user_response = int(input())
def decision6():
  if (user_response == 1):
    print("No one replies and you lost hope so you crash nose down into the earth.")
    loser()
  elif(user_response == 2):
    print("You are around nothing but jungles you see no safe place to land and the fuel runs out causing the plane to drop 10000 to your death.")
    loser()
  elif(user_response == 3):
    crash()

def crash():
  print("The plane crashed down and you survived.")
  print("what do you do ?")
  print("1. Scavage plane for any materials \n 2. Get out of the plane.")
  decision7()

  user_response = int(input())
def decision7():
  if(user_response == 1):
    print("The plane blows up while you are in it. You die.")
    loser()
  elif(user_response == 2):
    woods()
    
def woods():
  print("You get out of the plane but you are hungry and thirsty")
  print("1.Leave crash site and look for food and water. \n 2. Stay put and hope to be found.")
  decision8()
  
  user_response = int(input())
def decision8():
  if(user_response == 1):
    food()
  elif(user_response == 2):
    print("A plane passes by 20 minutes later they save you and now you are back safe at home.")
    print("YOU WIN")
    
def food():
  print("you leave site and find easy to reach berries on a bush and some coconuts high up in a tree. \n what do you do? ")
  print("1.Get the berries and eat them. \n 2.Try and climb the tree.")
  decision9()
  
  user_response = int(input())
def decision9():
  if(user_response ==1):
    print("The berries were ended up poisonus you were found by a rescue helicopter but unfortuanitly they were not able to deal with the poison in time.")
    loser()
  elif(user_response == 2):
    print("Your mother told you never to climb trees as a child and due to that you had no experience. You tried climbing the tree but fell and broke your head. Your body was never found.")
  loser()

  

def decision4ab():
  print("The plane goes down and you die because you forget the plane was falling.")
  loser()


def decision3b():
  print("You ejected the seatbelts and now the piolt lays on the ground. ")
  print("1.Try and fly the plane. \n 2. Try to save the piolt.")
  decision4b()

  user_response = int(input())
def decision4b():
  if(user_response == 1):
    decision4aa()
  elif(user_response == 2):
    decision4ab()


def loser():
  print("YOU LOSE")

#This is what runs the code
begin_story()
