# these are operations that can be performed by all sequence types
#  x in s   True if an item of s is equal x, else false

#ipAddress = input('Please enter an IP address: ')
#print(ipAddress.count('.'))

#*******************************************************************
# parrotList = ["non pinin'", "no more", "a stiff", "bereft of live"]

# parrotList.append("A Norwegian Blue")
# for state in parrotList:
#     print("This parrot is {}".format(state))

# even = [2, 4, 6, 8]
odd = [1,3,5,7,9]

# number = even + odd 
# # this is concatenation as in string sequence
# print(id(number))
# print(number)
# number.sort() 

# # this sort method does not create a new list object in the namespace. it only rearrange the already created list

# print(number)
# print(id(number))

# # on the other hand, the sorted function creates a new object of the list then sorts it. this is revealed by the id of the object in the namespace

# numberInOrder = sorted(number)
# print(numberInOrder)
# print(id(numberInOrder))

even = [2, 4, 6, 8]
print(id(even))
anotherEven = even
print(id(anotherEven))
anotherEven.append(10)
print(even)
print(id(even))
print(id(anotherEven))

#using the equals operator on two lists checks if the contents of the lists are the same
#whereas using "is" as the basis of comparism checks if both lists are pointing to the same variable in the namespace
# an example is seen below

# create an object of list even (list() is a list constructor)
# another_Even = list(even)

# print(another_Even is even) # should return false cos a different object of even was created
# print(another_Even == even)# should return true since the content is the same

# print(anotherEven is even) # should return true

# numberSet = [even, odd] # this creates a list of two separate lists even and odd
# print(numberSet)

# for num in numberSet:
#     print(num)
#     for val in numberSet:
#         print(val)

menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam',  'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

# for meal in menu:
#     if not 'spam' in meal:
#         print(meal)
#         for i in meal:
#             print(i)


Iterator = iter(menu)
for n in range(0, len(menu)):
    print(next(Iterator))
    
print()
print(menu[6][2])


print("="*60)

peom = ''' All exceptions derive from class Throwable, which has a printStackTrace method that
outputs to the standard error stream the stack trace (discussed in Section 11.2). Often this
is helpful in testing and debugging. Class Throwable also provides a getStackTrace method that retrieves the stack-trace information that might be printed by printStackTrace.
Class Throwable’s getMessage method returns the descriptive string stored in an exception'''

poem = '   All exceptions derive from class Throwable, which has a printStackTrace method that outputs to the standard error stream'
print(poem[: 40])
print(poem[::-1])
print(poem.split())


print('='*78)
# lists are mutable objects and are identified by the '[]'
# Turples are immutable objects and are delimited by '()'

names = 'exceptions', 'getMessage', 'Throwable', 'debugging'
print(names)
print(type(names))
print(id(names))
name = ('debugging', 'immutable', 'delimited')
print(type(name))
print(name)
print(name[1])
# immutables types cannot be changed but a new object can be assigned to the same variable
# as in names, i have created a new object 'names' below.
# this is evident because the id point to a different namespace.
# 
names = names[0], names[1], names[2], 'complete', names[3]
print(names)
print(id(names))

print('=' * 90)
print(names.index('complete'))
print(names.count('complete'))
print(names.__getitem__(4)) # returns the value of the index given
print(names.__add__(name)) # this method adds a turple to another turple

# A turple should be used when an item in a list should not be changed
# List should be used to store data that you may want to change at will
# turples can be unpacked using the technique below

print('=' * 90)
imelda = 'More Mayhem', 'Imelda May', 2011,((1, 'pulling the Rug'),(2, 'Psycho'), (3, 'Mayhem'),(4,'Kentish Town Waltz'))
title, artist, year, tracks = imelda  #contents of imelda turple was assigned to these variables
print(title)
print(artist)
print(year, tracks)
# print(tracks)

for i in imelda:
    print(i)
for track in imelda[3]:
    print(track)
