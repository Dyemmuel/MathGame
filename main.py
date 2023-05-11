# the "Programiz calculator" was used as a reference to create this game.
# the link for the reference code is "https://www.programiz.com/python-programming/examples/calculator"

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
import random

score = 0
name = input("Enter your name: ")
while True:
    print("Hello " + name + " would you like to play?")
    playing = str.casefold(input("(yes/no) "))
    if playing == "no":
        quit()
    elif playing == "yes":
        while True:
            print("Basic Arithmetic Game")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            play = input("Select game type:(1/2/3/4/5) ")
            if play in ("1", "2", "3", "4", "5"):
                while True:
                    print(name + "'s score: " + str(score))
                    x = int(random.randint(0, 100))
                    y = int(random.randint(0, 100))
                    if play == "1":
                        print(x, "+", y)
                        sum = str(add(x, y))
                        suman = input("Enter the sum of the two numbers or Enter E to exit: ")
                        if suman in ("E", "e"):
                            break
                        elif suman == sum:
                            print("Correct!")
                            score += 1
                        else:
                            print("Wrong!")
                            print("The correct answer is ", add(x, y))
                            score -= 1
                            break
                    elif play == "2":
                        print(x, "-", y)
                        dif = str(subtract(x, y))
                        difan = input("Enter the difference of the two numbers or Enter E to exit: ")
                        if difan in ("E", "e"):
                            break
                        elif difan == dif:
                            print("Correct!")
                            score += 1
                        else:
                            print("Wrong!")
                            print("The correct answer is ", subtract(x, y))
                            score -= 1
                            break
                    elif play == "3":
                        x = int(random.randint(0, 10))
                        y = int(random.randint(0, 10))
                        print(x, "*", y)
                        pro = str(multiply(x, y))
                        proan = input("Enter the product of the two numbers or Enter E to exit: ")
                        if proan in ("E", "e"):
                            break
                        elif proan == pro:
                            print("Correct!")
                            score += 1
                        else:
                            print("Wrong!")
                            print("The correct answer is ", multiply(x, y))
                            score -= 1
                            break
                    elif play == "4":
                        print(x, "/", y)
                        quo = str(round(divide(x, y), ndigits=2))
                        quoan = input("Enter the Quotient of the two numbers or Enter E to exit: ")
                        if quoan in ("E", "e"):
                            break
                        elif quoan == quo:
                            print("Correct!")
                            score += 1
                        else:
                            print("Wrong!")
                            print("The correct answer is ", quo)
                            score -= 1
                            break
                    elif play == "5":
                        print("Congratulations ", name, "your final score is ", str(score))
                        quit()
            else:
                        print("Please choose among the four game types or enter 5 to quit game")
    else:
        print("Please answer properly!")
