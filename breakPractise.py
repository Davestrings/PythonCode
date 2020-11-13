i =2
print("No. {} squared is {} ".format(i, i**2))
# if program flow
# name = input("please enter your name: ")
# if name == "david":
#     print('good')

# print("please guess a number between 1 - 10")
# guess = int(input())

# if guess < 5:
#     print("please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done!,You guessed correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > 5:
#     guess = int(input("Please guess lower: "))
#     if guess == 5:
#         print("Well done!, you guessed correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print('you guessed it first time')
    
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''

# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
# print(len(number))
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))
# 
# 
ipAddress = input("Enter an IP address: ")
if ipAddress[-1] != '.': 
    ipAddress += '.'
count = 0
check = []

for i in ipAddress:
    if i != '.':
        count +=1
    else:
        check.append(count)
        print(check, end=' ')
        count = 0
        continue
else:
    print("{} is the length of the IP address".format(len(check)))
    dif = 0
    while True:
        print("length of section {} is {}".format(dif+1,  check[dif]))
        dif +=1
        if dif == len(check):
            break
        
# proof that import can be made in the middle of a program in python instead of 
# at the beginning of the program in java
import random
highest =10
answer = random.randint(1, highest)
print(answer)
        

