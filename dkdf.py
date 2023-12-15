def read_file():
    data = []
    with open('tempraturdata.txt', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

def medel(data, x):
    for i in data[1:]:
      city = i[0]
      print(city)
      if city == x:
        temperatur = list(map(int, i[1:]))
        medeltemperatur = sum(temperatur) / len(temperatur)
        print("medel tempraturen",city, medeltemperatur)

def maxomin(data,x):
  for x in data[1:]:
    city = x[0]
    if city == x:
      temperatur = list(map(int, x[1:]))
      print(city,"lägsta:", min(temperatur),"högsta:", max(temperatur))

def fahrenheit(data,x):
  for x in data[1:]:
    city = x[0]
    if city == x:
      temperatur = [int(temp) * 9/5 + 32 for temp in x[1:]]
      print (city, temperatur)

def q(w,x):
  for x in w[1:]:
    city = x[0]
    if city == x:
      temp = list(map(int, x[1:]))
      if max(temp) <= min(temp)+3:
        print(city, x)

def start():
  while True:
    data = read_file()
    x = input("vad du vill göra:")
    if x == "medel":
      x = input("välj stad:")
      medel(data,x)
    elif x == "maxomin":
      x = input("välj stad:")
      maxomin(data,x)
    elif x == "far":
      x = input("välj stad:")
      fahrenheit(data,x)
    elif x == "q":
      x = input("välj stad:")
      q(data,x)
  
start()