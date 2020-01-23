number =int(input("Enter a Number: "))

while number != 1:
    if number%2 ==1:
        number = (number *3) + 1
        print(number)
    else:
        number = number//2
        print(number)
    
