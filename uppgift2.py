x = "A man, a plan, a canal, Panama"
def palidron(a):
  if a == a[::-1]:
    return True
  else:
    return False
  
print (palidron(x))
