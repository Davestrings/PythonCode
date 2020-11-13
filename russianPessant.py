# firstNumber = int(input("Enter your first number: "))
# secondNumber = int(input("Enter your second number: "))
# result = 0
# cont = 1
# while cont > 0:
#     mNumber = firstNumber * 2
#     dNumber = secondNumber/2
#     if (dNumber%2) == 1:
#         result += mNumber 
#     if dNumber == 0:
#         cont -= 1

# print(result)
# THE ABOVE PROGRAM IS'T WORKING

string = 'what is your name'
print(string[::2])
print(string[2:8:-1])

print(string.rjust(30, '.'))
print(string.find('o'))
print(string.find('b'))
print('index', string.index('t'))
print('index', string.index('o'))
s = string.upper()
print (s)
j = s.split(" ")
u=''
for i in j:
    u = u + ' ' + i.capitalize()
print(u) 
print(string[::-1])



