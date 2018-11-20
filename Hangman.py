import PickWord as pw
import GuessLetters as gl

chances = 6
print("Welcome to Hangman!")
print(f"You have only {chances} chances to guess wrongly.")
print("Good luck.\n")

gl.guessWord(pw.randomWord(), chances)