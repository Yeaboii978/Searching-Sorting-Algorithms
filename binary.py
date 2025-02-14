from random import randint

def binary():
  list =[]
  
  for i in range(0,100):
    items = randint(1,100)
    list.append(items)

  list.sort()
  y = len(list)//2
  i = 0
  found = True
  
  search = int(input("Find a number: "))
  
  if search == 0 :
    print(list)
    search = int(input("Find a number: "))
  
  while search != list[y]: 
    if search > list[y]:
      list = list[y+1:]
      i += y
    else:
      list = list[:y]
    if len(list) == 0:
      found = False
      break
    y = len(list)//2
    
  if found == True:   
    print(f"{search} found in postion {y+i}")
  else:
    print("Not found")



