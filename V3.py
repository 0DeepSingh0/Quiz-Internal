import time

score = 0

# Asks user for username
name = input("Enter a username: ")
print()
time.sleep(1)

# Welcome message
print(f"Hello {name}! Welcome to my Quiz about the movie Whale Rider")
print()

# List of questions, options, and correct answers
questions = [
    "Where was the movie Whale Rider filmed?",
    "What year did they start making the movie?",
    "What year was the movie Whale Rider made?",
    "Who directed the movie?",
    "Who was the author of this movie?",
    "Was Whale Rider based on a novel?",
]

# Answers to each question
options = [
    ["A. New Zealand", "B. Australia", "C. Tonga", "D. Samoa"],
    ["A. 2001", "B. 2002", "C. 1998", "D. 2007"],
    ["A. 2002", "B. 2003", "C. 1999", "D. 2008"],
    ["A. Niki Caro", "B. Witi Ihimaera", "C. Keisha Castle-Hughes", "D. Paikea Apirana"],
    ["A. Niki Caro", "B. Witi Ihimaera", "C. Keisha Castle-Hughes", "D. Paikea Apirana"],
    ["A. True", "B. False", "C. Maybe", "D. I don't know"]
]

answers = ["A", "B", "B", "A", "B", "A"]

# Loop through each question, options, and check answers
for i in range(len(questions)):
    # Display the question
    print(f"Question {i + 1}: {questions[i]}")

    # Display options
    for option in options[i]:
        print(option)

    # Validate user input for answer
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    # Check if the answer is correct
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()

# Determine grade based on score
percentage = (score / len(questions)) * 100

if percentage == 100:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Display user's final score and grade
print(f"Your final score is {score}/{len(questions)}")
print(f"You earned a grade {grade}")
