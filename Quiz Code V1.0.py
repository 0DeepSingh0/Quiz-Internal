import time


# Asks user for username
name = input("Enter a username: ")
print("\n")
time.sleep(1)

# This code welcomes the user
print(f"Hello {name} Welcome to my Quiz about the movie Whale Rider")
print("\n")
time.sleep(2)

# All Questions

questions = ("Question 1 : Where was the Whale rider filmed?: ",
                       "Question 2 :What year did they start making the movie?: ",
                       "Question 3 :Who was the author of this movie?: ",
                       "Question 4 :Who directed the movie?: ",
                       "Question 5 :Was this movie based on a novel?: ",
                       "Question 6 :What year was the movie released?: ")


# All the options of the quiz questions
options = (("A. New Zealand", "B. Australia", "C. Tonga", "D. Samoa"),
                   ("A. 2001", "B. 2002", "C. 1998", "D. 2007"),
                   ("A. Niki Caro", "B. Witi Ihimaera", "C. Keisha Castles", "D. Paikea Apirana"),
                   ("A. Paikea Apirana", "B. Keisha Castles", "C. Witi Ihaera", "D. Niki Caro,"),
                   ("A. True", "B. False"),
                   ("A. 2005", "B. 2007 ", "C. 2003", "D. 2004"))


# All Correct Answers
answers = ("A", "B", "B", "D", "A", "C")
guesses = []
score = 0
question_num = 0


# This displays all the questions and options 
for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)




# this code displays all inputs with questions and score

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"Correct answer is {answers[question_num]}")

    question_num += 1


#this shows the results at the end
print("\n")
print("       RESULTS        ")
print("\n")

# this prints all inputs of the users
print("Your Inputs: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# prints the correct answers at end
print("Correct Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


time.sleep(2)
# prints score in percentage at end with username
score = int(score / len(questions) * 100)
print(f"{name} you scored: {score}%")
