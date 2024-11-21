# sets store multiple items in single variable
# they are unordered, unchangeable and unindexed
# sets are written in curly brackets

fruits = {'Apple', 'Banana', 'Carrot', 'Kiwi', 'Grapes', 'Orange', 'Papaya'}
print(fruits)

# we can access sets items by 'for' loop and 'IN' keyword
fruits = {'Apple', 'Banana', 'Carrot', 'Kiwi', 'Grapes', 'Orange', 'Papaya'}
for fruit in fruits :
    print(fruit)

# IN keyword
if 'Apple'  in fruits:
    print('Apple is in the fruits')
else:
    print('Apple is not in the fruits')

# add() - used to add new item to the set 
fruits = {'Apple', 'Banana', 'Carrot', 'Kiwi', 'Grapes', 'Orange', 'Papaya'}
fruits.add("pineapple")
print(fruits)

    
