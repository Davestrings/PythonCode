# import math
from math import sqrt
number = int(input("Enter a number greater than Two: "))
counter = 1
# validation to number > 2
while number <= 2:
    number = int(input("Enter a number greater than 2 pls"))

# calculate square root and count number of iterations
while number > 2:
    number = sqrt(number)
    print("square root is {:.3f}".format(number)) 
    counter +=1
print(counter)