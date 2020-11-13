correctAnswers = ["A", "C", "A", "A", "D", "B", "C", "A",
                  "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

studentAnswers = ["A", "C", "A", "B", "D", "B", "F", "A",
                  "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "B"]

score = 0
wrong_Answer = []

nfile = open("studentAnswers.txt", 'w')  # open the specified file for writing


def derive_answer(student_answer):
    """function to write student answers to file. Expects a list as argument"""
    for number in range(20):  # since the size of the list is known to be 20, this creates a list from 0-19
        # which can be used as index in the code
        try:
            print(student_answer[number], file=nfile)  # this writes the value at the index "number" to the file
        except TypeError as e:
            print(e)  # in case a type conversion error occur, IOError is a good error to catch here too


derive_answer(studentAnswers)
nfile.close()   # when resources are opened, they must be closed to avoid resource leak

s_answer = open('studentAnswers.txt', 'r')  # reading from the file
choice = []

for num in range(20):

    for line in s_answer:   # this loop goes through each line in the file
        choice.append(line.strip())     # each line is then appended to the a list with any spaces removed.
    if correctAnswers[num].lower() == choice[num].lower():  # checking if correct answer value at the index "num"
        # is equal to choice i.e student answer at the same index

        score = score + 1   # if the condition is true, then student score is increased by one

    else:
        wrong_Answer.append(num + 1)    # if not, the index where the student answer is wrong is stored in this list
        continue

    # print(num+1)

print('score {}'.format(score))
if score >= 15:     # if the student score is above or equal to 15
    print("You passed")
else:   # if not,
    print("You fail... Try again next year")

print("question(s) missed --> ")
for i in wrong_Answer:  # print the indexes where the student is wrong
    print(i, end=' ')

print()
print("Number of correct answers ", len(correctAnswers) - len(wrong_Answer))  # number of correct answers
print("Number of incorrect answers ", len(wrong_Answer))  # number of incorrect answers

s_answer.close()    # close the resources.
