my_list = []
#b = []
counter = 0
count = 0
while count < 4:
    my_list.append(input("Enter tweets"))
    count += 1  
    
for c in my_list:
    c = c.lower().split()
print(c)
for i in c:
    if i.replace('#', "") == 'hackerrank':
        counter += 1
print(counter)