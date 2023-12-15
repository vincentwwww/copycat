
def huvudfunktion():
  x = int(input("skrive det första numret"))
  y = int(input("skrive dit andra nummer"))
  matte = str(input("skrive vad du vill göra. te.x:*,+..."))
  return x, y, matte

x, y, matte = huvudfunktion()

def funktionplus(x,y):
  resultat = x+y
  return resultat

def funktionkvadrerat(x,y):
  resultat = x**y
  return resultat

def funktiondelat(x,y):
  resultat = x/y
  return resultat

def funktiongånger(x,y):
  resultat = x*y
  return resultat

def funktionminus(x,y):
  resultat = x-y
  return resultat






if x ==0 or y == 0 and matte == "/":
  print("det går inte att dela med 0")
  exit()

if matte == "+":  
  resultat =funktionplus(x,y)
  print (resultat)
elif matte == "-":
  resultat =funktionminus(x,y)
  print (resultat)

elif matte == "*":
  resultat =funktiongånger(x,y)
  print (resultat)
elif matte == "/":
  resultat =funktiondelat(x,y)
  print (resultat)
elif matte == "^":
  resultat =funktionkvadrerat(x,y)
  print (resultat)
else:
  print("det värkar har gåt fel! pröva igen.")
