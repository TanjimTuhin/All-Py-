"""
variable[index]=new_value          -> mutability(changeable)
variable.append(value)             -> add item in list at last
variable.extend(2nd list variable) -> joining two list
variable.pop()         -> remove last item from list
variable.pop(index)    -> remove index item from list 
variable.remove(value) -> remove that value from the list
variable.clear()       -> remove all item from list shows a empty list
del variable[index]    -> remove index item from list 
del variable           -> delete full list 
insert(index, value)   -> add item in list at specific index
delete(index)          -> remove item in list at specific index
variable.copy()        -> copy a list in another variable
list[start:end:step]   -> list slicing
"""
my_list=[]
colors=['White', 'Black', 'Yellow', 'green', 'red', 'purple', 'gray']
cars=['mustang', 'ford', 'ferrari', 'audi', 'BMW', 'mercedes',
      'Koinigsegg', 'BYD', 'mazda', 'toyota', 'dodge', 'jaguar', 'porshea']
number=[1,2,3,4,5,6]
mixed=['helloo', 2, 3, 8.4, 3.4]


colors[2]='brown'
print(colors)

colors.append('yellow')
print(colors)

colors2= colors[1:5]
print(colors2)

num2=number.copy()
print("copied list from number:",num2)

number.insert(2, 2.5)
print(number)

mixed.pop()
print(mixed)

mixed.pop(1)
print(mixed)

colors.remove('red')
print(colors)

del colors[2]
print(colors)

# del  colors
# print(colors)

number.clear()
print(number)

print(cars)
print(colors)
cars.extend(colors)
print(cars)

