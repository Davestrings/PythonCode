num = int(input("Type in a number: "))

total = 0
for counter in range (1, num):
    if num%counter == 0:
        total += counter

if total == num:
    print("This number is a perfect number!")
elif total < num:
    print("Oohs! This is a deficient number")
        
else:
    print("arrgh! This is an abundant number")
