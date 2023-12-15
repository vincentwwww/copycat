#x = 10
#while x >= 1:
  #print(x)
  #x -= 1

#x = 2
#y = 0
#while x < 1000:
#  print(x)
#  x *= 2
#  y += 1
#print(y)
x = int(input("Skrive ett tal:"))
while True:
  try:
    if x == 0:
      x = z
    z = x
    y = int(input("Skrive ett tal:"))
    x *= y
    print(x)
  except ValueError:
    print("Invalid input. Please enter a valid number or 0 to exit.")

# = 1
#while x <= 10:
  #print(x)
  #x += 1

#import random
#while True:
  #x = random.randint(0,20)
  #y = int(input("gissa:"))
  #while x != y:
    #y = int(input("gissa:"))
  #print("du hade rätt")