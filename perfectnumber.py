number = int(input ("Enter a number: "))
factor = 1
sum = 0
while factor < number:
    if number%factor==0:
       sum += factor
       
    factor +=1

if sum == number:
    print("This number is a perfect number!")
elif sum < number:
    print("Oohs! This is a deficient number")
        
elif sum > number:
    print("arrgh! This is an abundant number")

else:
    print("Goodbye")
        
