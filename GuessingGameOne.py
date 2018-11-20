import random
comp = random.randint(1, 9);
guesses = 1

choice = int(input("Choose a number between from 1 to 9. (Both inclusive): "))
while comp is not choice:
    guesses += 1
    if comp > choice:
        print("Wrong! Your guess is lower than our number.\n")
    else:
        print("Wrong! Your guess is higher than our number.\n")
    choice = int(input("Choose a number between from 1 to 9. (Both inclusive): "))

print(f"Well done! Our number was {comp}. You guessed {guesses} times.")