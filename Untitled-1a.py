x = int(input("skrive:"))
y = 2
while x % y != 0:
  if y == x:
    print(str(x) + " är ett prime tal")
    exit()
  y += 1
print(str(x) + " är inte ett prime tal")
  
  
  