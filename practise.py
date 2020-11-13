
# parrot = "Norwegian Blue"
# print(parrot[10: 14])
# print(parrot[1:8:3])
# age = 24
# print("My age is {0} years".format(age))
# print("""January: {2}
# February: {0}
# March: {1}
# April: {1}
# May: {2}
# June: {1}
# July: {2}
# August: {2}
# Sepember: {1}
# October: {2}
# November: {1}
# December:{2}""".format(28,30,31))
# #formatting string
# print("Pi is approximately {0:<22.10f}".format(22 / 7))
# print("My Age is %d years" % age) #format deprecated

# for i in range(1,12):
#     print("No. {0:2} squared is {1:<4} and cubed is {2:>4}" .format(i, i**2,i**3))


# name = input("please enter your name: ")
# age = int(input("How old are you, {0}: ".format(name)))
# print(age)

# print("please gueess a number between 1 and 10: ")
# guess = int(input())

# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guess it")
#     else:
#         print("sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
    # print("you get it this time")

# age = int(input("How old are you? "))
# if (age >= 16) and (age <= 65):
#     print("Have a good day at work")
# #range sequence in for loop
# num = 10
# for i in range (num):
#     print(i, end=",")

# word = 'String word'
# print(word[::-1])
# print(word[::-2])
# print(word[0::2])

# numb = "1234567890"
# print(numb[::-1])
# print(numb[::2])
# m = 'hello'
# print("3" + m)
# print(ord('1'))
# print(ord('2'))

# my_str = input('Input a string')
# index_int = 0
# result_str ='1'
# while index_int < (len(my_str) - 1):
#     if my_str[index_int] > my_str[index_int + 1]:
#         result_str = result_str + my_str[index_int]
#     else:
#         result_str = result_str * 2
#     index_int += 1
# print("\n",result_str)

# print('{:>15s} : {:<8.1f}'.format('length',28.875))
# river = 'mississippi'
# len(river)
# for i in range(len(river)):
#     if river[i] == 'p':
#         print(i)
#         break
# else:
#     print('"p" not found')

# for i, letter in enumerate(river):
#     if letter == 'p':
#         print(i, letter)
#         # break
#     else:
#         print('"p" not found')


# s = 'ABC'
# for x in s:
#     for y in s:
#         for z in s:
#             if x != y and x!=z and y!=z:
#                 print(x,y,z)

# mim =1 
# total = 0
# while mim <= 64:
#     lin = mim**2
#     total += lin


#     mim += 1
# print(total)
# wheat_weight = 50 * total
# print(wheat_weight)

# arg1_list = ['a','b','c','d']
# arg2_list = ['hello', 'mother','and','father']
# arg_str = 'sister'


# def func1(list1, list2, str1):
# 	if len(list1) > 3:
# 	    list1 = list1[:3]
# 	list2[0] = 'goodbye'
# 	str1 = ''.join(list2)


# func1(arg1_list, arg2_list, arg_str)

# print(arg1_list)
# print(arg2_list)
# print(arg_str)

# largest = None
# smallest = None
# while True:
#     try:
#         num = input("Enter a number: ")
#     except:
#         num = None
#         break
    
#     if num == "done" : break
#     if num is None:
#         num = int(num)
#         smallest = num
#         largest = num
#     # num = int(num)
#     if num > largest:
#         largest = num
#     elif smallest > num:
#         smallest = num
    

# print("Maximum", largest)
# print("Minimum", smallest)

# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         num = int(num)
#     except:
#         print("Invalid input")
#         continue
#     if largest is None:
#         largest = num
#     elif smallest is None:
#         smallest = num
        
        
#     if smallest > num:
#         smallest = num
#     if largest < num:
#         largest = num
        
        
# print("Maximum is ", largest)
# print("Minimum is ", smallest)


# Recussive function
# def reverse(text):
# 	if len(text) == 1:
# 		return text
# 	else:
# 		return reverse(text[1:]) + text[0]


# def take_step(n):
# 	if n==1:
# 		return "Easy"
# 	else:
# 		this_step = "step(" + str(n) + ")"
# 		previous_step = take_step(n-1)
# 		return this_step + " + " + previous_step



# s = {}
# s['jane'] = 2390485
# s['shile'] = 9834
# s['yemi'] = 546
# s.pop
# print()
# my_list = ['I', 'need', '1', 'month', 'worth', 'of', 'data', 'subscription']
# print(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], my_list[5], my_list[6], my_list[7])
# print()
temp_file = open("yellowCard.txt", 'w')
print("first line", file=temp_file)
print("second line", file=temp_file)
print("This was written to test the efficiency of the right method", file= temp_file)
print("Let’s put these concepts together into a simple line-reversal program", end='\n' "The line is stripped (to remove the carriage return), and then", file=temp_file)
# for line_str in temp_file:
#     print(line_str, end='')
temp_file = open("yellowCard.txt", 'r')
for line_str in temp_file:
    print(line_str, end='')
temp_file.close()

print("\n")
input_file = open("yellowCard.txt", 'r')
output_file = open("yellowCard2.txt", 'w')
for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()
    for char in output_file:
        new_str = char + new_str
    print(new_str, file = output_file)
input_file.close()
output_file.close()

# names = []

# while True:
#     name = input("type your name ").strip().lower()
#     if name == 'quit' or name == 'q':
#         break
#     names.append(name)
# print(names)