from random import randint

def bubble():
  list = []
  
  for i in range(0,100):
    items = randint(1,100)
    list.append(items)

  print("Unsorted -","\n",list)
  for i in range(len(list)):
    for i in range(len(list)-1):
      if list[i] > list[i+1]:
        swap = list.pop(i)
        list.insert(i+1,swap)
  print("Sorted -","\n",list)
