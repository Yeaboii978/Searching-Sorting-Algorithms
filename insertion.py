from random import randint

def insertion():
  list = []
  for x in range(0,100):
    items = randint(1,100)
    list.append(items)
    
  y = 1
  print(list)
  
  for y in range(len(list)-1):
    w = True
    i = y
    while  i >= 0 and w:
      if list[i] > list[i+1]:
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
        i -= 1
      else:
        w = False
    
  print(list)
