import pylab;
list_int = []
for i in range(10):
    list_int.append(i * 2)

print(list_int, len(list_int))
pylab.plot(list_int)
pylab.show()
# graph plotting above

value = int(input("Enter a number "))
pow = int(input("Enter the power "))
result = 1
for i in range(pow):
    result *= value
print(result)
