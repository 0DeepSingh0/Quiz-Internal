import time

score = 0

# Asks user for username
name = input("Enter a username: ")
print()
time.sleep(1)

#This code welcomes the user
print(f"Hello {name} Welcome to my Quiz about the movie Whale Rider")
print()

# List of questions, options, and correct answers
questions = [
    "Where was the movie Whale rider filmed?",
    "What year did they start making the movie?",
    "What year was the movie Whale Rider made?",
    "Who directed the movie?",
    "Who was the author of this movie?",
    "Was Whale rider based on a novel?",
]
# Answers to each questions 
options = [   
    ["A. New Zealand", "B. Australia", "C. Tonga", "D. Samoa"],
    ["A. 2001", "B. 2002", "C. 1998", "D. 2007"],
    ["A. 2002", "B. 2003", "C. 1999", "D. 2008"],
    ["A. Niki Caro", "B. Witi Ihimaera", "C. Keisha Castles", "D. Paikea Apirana"],
    ["A. Niki Caro", "B. Witi Ihimaera", "C. Keisha Castles", "D. Paikea Apirana"],
    ["A. True", "B. False", "C. Maybe", "D. I don't know"]
]

answers = ["A", "B", "B", "A", "B", "A"]

# Loop through each question, options, and check answers
for i in range(len(questions)):
    # Display the questions and options
    print(f"Question {i+1}: {questions[i]}")

    for option in options[i]:
        print(option)

   
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Check if the answer is correct
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()  

# Display user's final score
print(f"Your final score is {score}/{len(questions)}")


