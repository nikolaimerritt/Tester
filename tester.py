import random as rn
import os

def SpecificTopic():
    correct = 0
    wrong = 0
    while (True):
        print("Type the question's number that you want. If you want to quit, type anything other than a number")
        for i in range(0, len(allQuestions)):
            print("[" + str(i + 1) + "]"   + allQuestions[i][0], end="") #doing end="" because there are \ns in the headers anyway

        userI = (int(input("")) - 1)

        toAsk = allQuestions[userI][1:] #getting the ones that arent the header, which is at index 0
        rn.shuffle(toAsk)
        for e in toAsk:
            print(e)
            v = input("correct? n if no, otherwise yes")
            if (v != "n"): correct += 1
            else: wrong += 1
        print("\nYou got", correct, "out of", (wrong + correct), ":", (100 * correct / (wrong + correct + 0.0)), "%" )

def AllTopics():
    goAgain = ""
    correct = 0
    wrong = 0
    while("n" not in goAgain):
        questionsToAsk = []
        for i in range(0, len(allQuestions)):
            for j in range(1, len(allQuestions[i])):
                questionsToAsk.append(allQuestions[i][j])
        rn.shuffle(questionsToAsk)
        for e in questionsToAsk:
            print(e)
            v = input("correct? n if no, otherwise yes")
            if (v != "n"): correct += 1
            else: wrong += 1
        print("\nYou got", correct, "out of", (wrong + correct), ":", (100 * correct / (wrong + correct + 0.0)), "%" )
        goAgain = str(input("\nGo again?"))


mainDir = os.path.split(os.path.abspath(__file__))[0]
data = open(os.path.join(mainDir, "questions.txt"), "r")
dataRead = data.read()
data.close()

questionSets = dataRead.split("#")
del questionSets[0] #doing this because the first one will be empty

allQuestions = []
for qSet in questionSets:
    qList = qSet.split(" - ")
    allQuestions.append(qList)

userFunct = int(input("Type the number for whichever function you want\n\n[1] Random questions from a specific subtopic\n[2] Random questions out of all subtopics\n"))
if (userFunct == 1): SpecificTopic()
else: AllTopics()
