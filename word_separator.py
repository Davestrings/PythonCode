# sentence = input("Enter a sentence in pascal case")

sentence = "StopAndSmellTheRosesAgainAgainAgain"

alphabeths = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


indexes = []
sentence_characters = list(sentence)

# print(sentence[:4])
# print(sentence[4:7])
# print(sentence[7:12])
# print(sentence[12:15])
# print(sentence[15:20])
# print(sentence[20:])

first_position = sentence_characters.pop(0)
variable = 1

for character in sentence_characters:
    if character in alphabeths:
        indexes.append(sentence_characters.index(character) + variable)
        sentence_characters.remove(character)
        variable += 1

for i in indexes:
    print(i)

for i in range(len(indexes) + 1):
    if i == 0:
        print(sentence[:indexes[i]], end=' ')
    elif 0 < i < len(indexes):
        print(sentence[indexes[i-1]:indexes[i]].lower(), end=' ')
    else:
        print(sentence[indexes[i-1]:].lower())

print(first_position)



