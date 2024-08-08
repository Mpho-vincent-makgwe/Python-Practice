import random

# create a greeting
print("welcome to Hangman!")
# create your word list.
words = ["hacker", "Software Developer", "programmer", "bounty", "random"]
# randomly choose a word from list you have created
secret_word = random.choice(words)
# ask the user to guess a letter
guess = input("Guess a letter").lower()
print(guess)
# check if the letter is int the word
for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")