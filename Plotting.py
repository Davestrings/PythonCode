import math
import pylab

x_values = []
y_values = []
count = 0.0

while count < math.pi * 4:
    x_values.append(count)
    y_values.append(math.sin(count))
    count += 0.1
    
pylab.plot(x_values, y_values, 'k.')
# pylab.show() 

j=0
for i in range(6):
    j+=i
if j%5 == 0:
    print(j)

a = 1
b = 10
c =''
d =''
for i in range(a,b):
    c = c+str(i)
    d = d + str(b-i)
    print(c + ' * 8 + ' + str(i) + ' = ' + str(d))
    
    
m=9
j=''
t=8
l=m-1
n=''    
for i in range(m, 1, -1):
    j= j+ str(i)
    l -= 1
    n= n+ str(t)
    print(j + ' * 9 + ' + str(l) + ' = ' + n)
    
sentence = 'that car is really fast'
i = 1
while i > 0:
    for character in sentence:
        if character == 't':
            print('found a \'t\' in sentence')
        else:
            print('maybe the next character?')
    i -= 1
