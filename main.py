import random

c = random.randint(1,10)
ud = False
u = 0
while(ud == False):
  un= int(input("what number do u think the computer got?"))
  #if...
  #if the userNumberGuess guess is less than the computernum then print out "The number is higher!"
  if(un < c):
    print("the number is higher!")
    u += 1
  #elif
  #elif the userNumberGuess guess is more than computernum then print out "The number is lower!"
  elif(un > c):
    print("The number is lower!")
    u += 1
  #else
  #print out "You won the game the computer number was" +
  else:
    print("You won the game the computer number was" + str(c))
    print("u took "+ str(u) +" tries"    )
    break
