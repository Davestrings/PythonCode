import random

number = random.randint(0, 100)

print("Hi-Lo Number Guessing Game: between 0 and 100")
print()

guess = int(input("Guess a Number. "))

while 0<= guess <=100:
    if guess > number:
        print("Guess is too high ")
    elif guess < number:
        print("Guess is too low")
    else:
        print("Yes! you got it right")
        break
    guess = int(input("Guess a Number. "))

else:
    print("You quit too early, the number was: ", number)