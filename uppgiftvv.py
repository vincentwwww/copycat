
data = []
with open('1d.txt') as file:
  for line in file:
    data.append(line.strip())
bokstäv = "qwertyuiopasdfghjklöäzxcvbnm"
bokstäv1 = "one two three four five six seven eight nine"

data1 = []

for str in data:
  str1 = ""
  for char in str:
    if char not in bokstäv:
      str1 += char
  data1.append(str1)

y= 0
for str in data1:
  x = str[0] + str[len(str)-1]
  y += int(x)
  print(x)
print(y)