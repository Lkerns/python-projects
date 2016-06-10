#inventory.py
stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
  print("Inventory:")
  item_total=0
  for k, v in inventory.items():
    print(v, k)
    myList=[]
    myList.append(v)
    item_total=sum(myList)
  print("Total number of items: " + str(item_total))
