import random

number = random.randint(0, 100)

while True:
    answer = input("Guess number: ")
    if answer == "" or answer == "exit":
        print("Close program")
        break
    if not answer.isdigit():
        print("Enter number")
        continue

    answer = int(answer)

    if answer == number:
        print("Excatly!")
        break
    elif answer < number:
        print("Incorrect number!")
    else:
        print("Lower")