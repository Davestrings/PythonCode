word = input("Enter an English word ")
vowels = 'aeiou'
volAppend = 'yay'
constAppend = 'ay'

while word != '.':
    for i in word:
        if i not in vowels:  # find consonant
            for j in word:
                if j in vowels:  # get index of consonant
                    jIndex = word.find(j)
            slicedWord = word[: jIndex]  # slice from beginning to index of character
            leftOver = word[jIndex:]
            newWord = leftOver + slicedWord + constAppend  # make new word
            print(newWord)
            break
        elif i in vowels:  # find vowel
            newWord = word + volAppend  # add suffix
            print(newWord)
            break

    word = input("Enter another English word or press '.'(dot) to end program ")
    print()



