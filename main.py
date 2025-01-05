import random

difficult = ""

print("Welcome to numberGuessGame!\nI'm choise a number between 1 to 100\n")
print("Please select the difficult:\nE: Easy (10 chances)\nN: Normal (7 chances)\nH: Hard (4 chances)")

while difficult.lower() not in ["e", "n", "h", "easy", "normal", "hard"]:
    difficult = input("[E/N/H]: ").lower()

match difficult:
    case "e":
        difficult = "easy"
    case "n":
        difficult = "normal"
    case "h":
        difficult = "hard"

match difficult:
    case "easy":
        chances_last = 10
    case "normal":
        chances_last = 7
    case "hard":
        chances_last = 4

guessNumber = random.randint(1, 100)

print(f"\nGood luck!\nChances last: {chances_last}")

while chances_last > 0:
    ans = int(input("Your answer: "))
    if ans == guessNumber:
        print("Right! You guessed it right!")
        break
    elif ans < guessNumber:
        print("Wrong! The hidden number is greater!")
    elif ans > guessNumber:
        print("Wrong! The hidden number is less!")
    chances_last -= 1
    if chances_last == 0:
        print("Oh.. Your attempts are over!")
        print(f"Right answer: {guessNumber}")
        break
    print(f"Chances last: {chances_last}")
