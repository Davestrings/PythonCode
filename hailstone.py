import pylab
number_str = input("Enter a positive number")
number = int(number_str)
count = 0

while number > 1:
    if number%2:
        number = number*3 + 1
    else:
        number = number /2
    print(number, ',', end=' ')
    count += 1

else:
    print()
    print('Sequence is', count, 'numbers long')
print()
print()


list_of_ints = []
for counter in range(10):
    list_of_ints.append(counter*2)

print(list_of_ints)
print(counter)

#pylab.plot(list_of_ints)
#pylab.show()

import Math

y_values = []
x_values = []
number = 0.0

while number < Math.pi * 4:
    y_values.append(Math.sine(number))
    x_values.append(number)

    number += 0.1

pylab.plot(x_values, y_values, 'ro')
pylab.show


    
