# append()- helps to add item to a list
Devices = ['mobile', 'watch', 'airpods', 'laptop',]
Devices.append('television')
print(Devices)

# insert()- adds item at specific index in a list
Devices = ['mobile', 'watch', 'airpods', 'laptop']
Devices.insert(1,'television')
print(Devices)

# extend()- add elements from another list to current list
fruits = ['apple', 'banana', 'carrot', 'grapes', 'pineapple']
vegetables = ['tomato', 'onion', 'spinach', 'potato', 'mushroom']
fruits.extend(vegetables)
print(fruits)

# remove()- eliminates specific item from list
Devices = ['mobile', 'watch', 'airpods', 'laptop',]
Devices.remove('airpods')
print(Devices)

# pop() - removes item at specific index and if no index is specified removes the last item 
fruits = ['apple', 'banana', 'carrot', 'grapes', 'pineapple']
fruits.pop(1)
print(fruits)

# del keyword deletes the list completely 
fruits = ['apple', 'banana', 'carrot', 'grapes', 'pineapple']
del fruits





