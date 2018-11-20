def guessWord(word, chances):
    allGuesses = []
    wrongCount = 0
    print("_ " * len(word))
    print()
    while True:
        inp = str.upper(input("Guess a letter: "))
        if inp in allGuesses:
            print("You've made that guess before. Guess again.\n")
            continue
        allGuesses.append(inp)
        if inp not in word:
            wrongCount += 1
            if wrongCount == chances:
                print(f"Sorry. That was your {chances}th wrong guess. Game over.")
                print(f"The word was {word}.")
                break
            print(f"Wrong guess! You have {chances - wrongCount} chances left. Try again\n")
            continue
        print("Guess correct!")
        complete = True
        for i in word:
            if i in allGuesses:
                print(i, end=" ")
            else:
                print("_", end=" ")
                complete = False
        print()
        if complete:
            print("Well done! You've guessed the word completely!")
            break
        else:
            print("Good job. Try again.\n")
