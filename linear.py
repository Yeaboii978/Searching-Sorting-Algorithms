from random import randint

def linear():
  list = []
  y = 0
  
  for i in range(0,100):
    items = randint(1,100)
    list.append(items)
  
  opt = int(input("Press 1 for simple search or 2 for multi search: "))
  
  
  if opt == 1:
    search = int(input("Find a number: "))
    if search == 0:
      print(list)
      search = int(input("Find a number: "))
    while list[y] != search and y <= len(list) and search in list:
      if list[y] != search:
        y += 1
  
    if search in list:
      print(f"{search} was found in postion {y}")
    elif search not in list and search != 0:
      print("Not found")
  elif opt == 2:
  
    search = int(input("Find a number: "))
    if search == 0:
      print(list)
      search = int(input("Find a number: "))
      
    
    for i in range(0,len(list)):
      if list[i] == search:
        print(f"{search} found in postion {i} ")
        i += 1
        y += 1
      else:
        i += 1
  
    if y == 0 and search != 0:
      print("Number not found")
