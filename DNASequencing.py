from sys import *


def find(some_thing, substring, start, end):
    some_thing = some_thing.lower()
    substring = substring.lower()
    word_slice = some_thing[start: end]
    print(word_slice)
    if substring in word_slice:
        return word_slice.index(substring)
    else:
        return -1


def multi_find(some_thing, substring, start, end):
    index = -1
    some_thing = some_thing.lower()
    substring = substring.lower()
    word_slice = some_thing[start: end]  # slice the portion specified by user
    word_slice.strip()  # strip spaces from both ends
    # in a loop, check for the word,
    # if present, get the index and continue with iteration from after the last iteration.
    try:
        while True:
            if substring in word_slice:
                index = word_slice.index(substring, index + 1, len(word_slice))
                print(index, end=", ")
            if index == -1:
                break
    except:
        print("")
        exit()  # from module sys. This use is due to the type of import that was used instead of 'import sys'
        # which will require i prefix the exit method like this, sys.exit().


word = "The name the of the best the the player is messi "
subString = 'THE'
print("result for find", find(word, subString, 11, len(word)))

multi_find(word, subString, 0, len(word))
