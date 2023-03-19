#NBA guessing game quiz
import os
import time

#Questions Dictionary
questions = {
    "Question 1": {
        "question" : "What is the name of the team that won 2022 NBA Finals?",
        "answer" : [
            "a) Boston Celtics",
            "b) Milwaukee Bucks",
            "c) Dallas Maverics",
            "d) Golden State Warriors"
        ],
        "correct answer" : "d"
    },
    "Question 2" : {
        "question" : "Who was the regular-season MVP of the 2021/2022 season?",
        "answer" : [
            "a) Giannis Antetokounmpo",
            "b) Joel Embiid",
            "c) Nikola Jokic",
            "d) Luka Doncic"
        ],
        "correct answer" : "c"
    },
     "Question 3" : {
        "question" : "Who has the most regular-season MVPs in the NBA history?",
        "answer" : [
            "a) Michael Jordan",
            "b) Bill Russell",
            "c) Kareem Abdul-Jabbar",
            "d) LeBron James"
        ],
        "correct answer" : "c"
    },
     "Question 4" : {
        "question" : "Which one of these four teams has the worst Finals winning percentage (According to Wikipedia)?",
        "answer" : [
            "a) Houston Rockets",
            "b) Cleveland Cavaliers",
            "c) OKC/Seattle SuperSonics",
            "d) New York Knicks"
        ],
        "correct answer" : "b"
    },
     "Question 5" : {
        "question" : "Which one of these four finals matchups was played the most?",
        "answer" : [
            "a) Chicago Bulls vs Utah Jazz",
            "b) Detroit Pistons vs Los Angeles Lakers",
            "c) Boston Celtics vs Houston Rockets",
            "d) Seattle SuperSonics vs Washington Bullets"
        ],
        "correct answer" : "b"
    },
     "Question 6" : {
        "question" : "Who, out of these four players, has the most finals MVPs?",
        "answer" : [
            "a) Tim Duncan",
            "b) Willis Reed",
            "c) Larry Bird",
            "d) Kareem Abdul-Jabbar"
        ],
        "correct answer" : "a"
    },
     "Question 7" : {
        "question" : "Who, out of these four players, has the most assists (All Time: Regular Season by nba.com/stats/alltime)?",
        "answer" : [
            "a) Steve Nash",
            "b) Mark Jackson",
            "c) Oscar Robertson",
            "d) Magic Johnson"
        ],
        "correct answer" : "a"
    },
     "Question 8" : {
        "question" : "Which one of these four teams has the most DPOY winners?",
        "answer" : [
            "a) Phoenix Suns",
            "b) Denver Nuggets",
            "c) Milwaukee Bucks",
            "d) Detroit Pistons"
        ],
        "correct answer" : "d"
    },
     "Question 9" : {
        "question" : "What team the Lakers played against in the 2000 NBA Finals?",
        "answer" : [
            "a) Detroit Pistons",
            "b) New Jersey Nets",
            "c) New York Knicks",
            "d) Indiana Pacers"
        ],
        "correct answer" : "d"

    },
     "Question 10" : {
        "question" : "Who was the Points Leader in the 2014 Playoffs?",
        "answer" : [
            "a) LeBron James",
            "b) Russell Westbrook",
            "c) Kevin Durant",
            "d) Tony Parker"
        ],
        "correct answer" : "c"
    },
}

#list of possible answers to each question
possibleAnswers = ["a", "b", "c", "d"]
#quiz score
score = 0

for key, value in questions.items():
    print(value['question'])
    for ans in value['answer']:
        print(ans)

    while True: 
        userAnswer = input("Answer: ")

        if userAnswer.lower() not in possibleAnswers:
            print("Invalid input. Please enter a valid answer (a, b, c or d).")
        
        else:
            if userAnswer.lower() == value["correct answer"].lower():
                print("\n Correct!")
                score += 1
                time.sleep(2)
                #clears the terminal window before the next question
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("\n Incorrect.")
                time.sleep(2)
                #clears the terminal window before the next question
                os.system('cls' if os.name == 'nt' else 'clear')
                
            break    

#printing final score to the user    
print("Final Score: {0} out of 10. That's {1} %".format(score, int(score/10 * 100)) )

if score == 10 :
    print("YOU ROCK!")
elif score < 10 and score >= 7:
    print("You are pretty good at this.")
else:
    print("Next time will be better!\n ^_^ ")

print("Thank You for playing my NBA QUIZ")
print("Closing")
time.sleep(2)
