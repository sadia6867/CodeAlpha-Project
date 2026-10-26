import random

words = ["apple" , "tiger" , "pizza" , "guitar", "planet"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters.You can make a maximum of", max_wrong_guesses, "wrong guesses.")

while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)

    if "_" not in display_word:
        print("You won! The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1
            print("You have", max_wrong_guesses - wrong_guesses, "wrong guesses left.")

if wrong_guesses == max_wrong_guesses and "_" in display_word:
    print("\nYou lost! The word was:", word)     

