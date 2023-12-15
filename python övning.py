x = int(input("skrive ditt number:"))
y = 1
while y <= x:
  print("*"*y)
  y = y+1

import random

v = 0
f = 0
m = 0
while True:
  m = m + 1
  x = input("skrive:")
  y = ["sten","sax","påse"]
  bot = (random.randint(-1,2))
  bot = y[bot]
  print(bot)
  if x == bot:
    print("det bliv jämnt")

  elif x == "påse" and bot == "sax":
    print("du förlorade")
    f = f + 1
  elif x == "sax" and bot == "sten":
    print("du förlorade")
    f = f + 1
  elif x == "sten" and bot == "påse":
    print("du förlorade")
    f = f + 1

  else:
    print("du van")
    v = v + 1

  print (str(v)+"/"+str(f))