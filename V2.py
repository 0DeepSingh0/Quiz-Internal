import time
score = 0

# Asks user for username
name = input("Enter a username: ")
print()
time.sleep(1)

#This code welcomes the user
print(f"Hello {name} Welcome to my Quiz about the movie Whale Rider")
print()

#Question 1
print("Question 1 : Where was the Whale rider filmed?: ")
print("""A. New Zealand
B. Australia
C. Tonga
D. Samoa""")
answer = input("Enter A,B,C,D:  ").upper()
if answer == "A":
  score +=1
  print("Correct!")
else:
    score + 0
    print("Incorrect, Correct Answer is A!")
print()

#Question 2
print("Question 2 :What year did they start making the movie?: ")
print("""A. 2001
B. 2002
C. 1998
D. 2007""")
answer = input("Enter A,B,C,D:").upper()
if answer == "B":
  score +=1
  print("Correct!")
else:
    score + 0
    print("Incorrect, Correct Answer is B!")
print()

#Question 3
print("What year was whale rider made?: ")
print("""A. 2002
B. 2003
C. 1999
D. 2008""")
answer = input("Enter A,B,C,D:  ").upper()
if answer == "B":
  score +=1
  print("Correct!")
else:
    score + 0
    print("Incorrect, Correct Answer is A!")
print()

#Question 4
print("Question 4 :Who directed the movie? : ")
print("""A. Niki Caro
B. Witi Ihimaera
C. Keisha Castles
D. Paikea Apirana""")
answer = input("Enter A,B,C,D:").upper()
if answer == "A":
  score +=1
  print("Correct!")
else:
    score + 0
    print("Incorrect, Correct Answer is B!")
print()