import sqlite3

print("***** Welcome to the Quiz game *****")

connect = sqlite3.connect("userData.db")
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS userData(name TEXT, surname TEXT, score INT)")
connect.commit()

def openQuestions(questionNumber1):
    with open("Questions.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if (questionNumber1) == l_no:
                return line       
            
def openVariants(variantNumber):
    with open("Variants.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if (variantNumber) == l_no:
                return line   

def openAnswers(answerNumber):
    with open("AnswerText.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if (answerNumber) == l_no:
                return line  

def scoreBoard():
    cursor.execute("SELECT * FROM userData ORDER BY score DESC")
    allGamer = cursor.fetchall()
    convertAllStr=lambda x:[str(y) for y in x]
    for i, j in enumerate(allGamer,1):
            print("{}){}".format(i, " ".join(convertAllStr(j))))


questionNumber = 0
score = 0

while True:
    try:
        print("What do you want?\n1-Play game\n2-Scoreboard\n3-Exit\n")
        playGame = input(">>>").lower()
        if int(playGame) < 1 or int(playGame) > 3:
            print("Please, choose 1, 2 or 3")
        else:
            break
    except ValueError:
        print("Please, choose 1, 2 or 3")


if playGame == "1":
    name = input("Your name:").lower().capitalize()
    surname = input("Your surname:").lower().capitalize()
    while questionNumber < 15:
        print("\n\tYour score: ", score)
        print("\n", openQuestions(questionNumber))
        print(openVariants(questionNumber))
        answer = input("Write your answer: ")
        p = openAnswers(questionNumber)
        p = p.split()
        answer = answer.split()
        if p == answer:
            print("\nCorrect")
            score += 10
        else:
            print("\nWrong answer")
            print("\nYou lost")
            print("Your score: ", score)
            cursor.execute("INSERT INTO userData VALUES('{}','{}',{})".format(name, surname, score))
            connect.commit()
            while True:
                playGame = input("Do you want see the scoreboard?(yes or no): ").lower()
                if playGame == "yes" or playGame == "no":
                    scoreBoard()
                    break
                else:
                    print("Please, write yes or no")
            exit()
        
        questionNumber += 1
    if score == 150:
        print("You won!")
        cursor.execute("INSERT INTO userData VALUES('{}','{}',{})".format(name, surname, score))
        connect.commit()
        while True:
            playGame = input("Do you want see the scoreboard?(yes or no): ").lower()
            if playGame == "yes" or playGame == "no":
                scoreBoard()
            else:
                print("Please, write yes or no")

elif playGame == "2":
    scoreBoard()

elif playGame == "3":
    exit()
