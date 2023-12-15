längd = 3
bred = 4
def area_rectangle(b, l):
  return (b*l)/2

print(area_rectangle(bred, längd))

def is_even(x):
  if x%2 == 0:
    return "even"
  else:
    return "odd"
  
print(is_even(7))

a = ["q", "e", "d",]
def reverse_list(list1):
  list1.reverse()
  return list1

print(reverse_list(a))
