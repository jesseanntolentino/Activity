"""
    Activity 2: Python Programming - Math Tutor
    Submitted by: ADOR, Angelo
                  HASHIM, Elizabeth Ann
                  TOLENTINO, Jesse Ann
    Year & Section: BSIS-2AB-M
"""

#imports the random and os module.
import random 
import os

"""
    The code is a calculator that can add, subtract, multiply, and divide two numbers.
    
    :param x: the first number
    :param y: the second number
    :return: the result of the operation.
"""
def add (x, y):
    return x + y

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

score = 0

# Asking the user to input a number between 1 and 4. If the user inputs a number between 1 and 4, it
# will ask the user a question. If the user inputs a number that is not between 1 and 4, it will print
# "Invalid Input".
while True:
    os.system("cls")
    print ("MATH TUTOR")
    print("1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
    choice = input("Enter your choice: ")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            os.system("cls")
            print("=== Addition ===")
            # Asking the user how many problems they want to answer.
            probNum = int (input("\nHow many problems?: "))
            i = 0
            score = 0
            while i < probNum:
                # Generating random numbers from 0 to 9 and 2 to 10. Then it is adding the two
                # numbers.
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10))
                num3 = add(num1, num2)
                print("\nWhat is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                # Checking if the user's answer is correct. If it is correct, it will print "Correct"
                # and add 1 to the score. If it is wrong, it will print "Wrong! The correct answer is"
                # and the correct answer.
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! The correct answer is", num3)
                i += 1

        elif choice == '2':
            os.system("cls")
            print("=== Subtraction ===")
            probNum = int (input("How many problems?: "))
            i = 0
            while i < probNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10))
                num3 = subtract(num1, num2)
                print("\nWhat is the difference of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! The correct answer is", num3)
                i += 1

        elif choice == '3':
            os.system("cls")
            print("=== Multiplication ===")
            probNum = int (input("How many problems?: "))
            i = 0
            while i < probNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10))
                num3 = multiply(num1, num2)
                print("\nWhat is the product of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! The correct answer is", num3)
                i += 1

        elif choice == '4':
            os.system("cls")
            print("=== Division ===")
            probNum = int (input("How many problems?: "))
            i = 0
            while i < probNum:
                num1 = round(float(random.randint(0, 9)),2)
                num2 = round(float(random.randrange(2, 10)),2)
                num3 = divide(num1, num2)
                print("\nWhat is the quotient of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! The correct answer is", num3)
                i += 1

        # Printing the user's score.
        print("\nChallenge Done!! Your score is " + str(score) + "/" + str(probNum))
    
    # Asking the user if they want to try again. If the user inputs "no", it will break the loop.
    try_again = input("\nWant to try again? (Yes/No):")
    decision = try_again.upper()
    if decision == "NO":
        break
else:
    print("Invalid Input")