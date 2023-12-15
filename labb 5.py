import statistics
def reader():
  with open('tempraturdata.txt', encoding='utf-8') as file:
    rea = file.readlines()
    listan = []
    for x in rea:
      y = x.strip()
      listan.append(y)
    return listan
listan = reader()

def fix(x):
  b =[]
  for k in x:
    a = k.split(",") 
    print(a)
    b.append(a)
  return(b)

b= fix(listan)

print(b)