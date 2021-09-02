#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random 
import art
print(art.logo)

secret_number = random.randint(1,100)
def guess_compare(guess):
    if guess > secret_number:
        return "Too high."
    elif guess < secret_number:
        return "Too low."
    elif guess == secret_number:
        return False
play_the_game = True
while play_the_game == True:
    print("Welcome to the Number Guessing Gam!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    difficulty_mode = input("Choose a difficulty. Type 'easy'or 'hard':\n")
    if difficulty_mode == 'easy':
        guess_left = 10
    else:
        guess_left = 5
    game_not_over = True
    while game_not_over == True:
        guess_left -= 1
        user_guess = int(input("Make a guess:  "))
        if guess_left == 0:
            print(f"You have run out of guesses, you lose :(\n")
            game_not_over = False
        elif guess_compare(user_guess) != False and user_guess != secret_number:
            print(guess_compare(user_guess))
            print("Guess again.")
            print(f"You have {guess_left} attempts remaining to guess the number.")
        elif guess_compare(user_guess) == False:
            print(f"You win, you guessed the right number of {secret_number}!\n")
            game_not_over = False
        
    want_to_play = input("Type 'y' to play again, type 'n' to stop. \n")
    if want_to_play == 'n':
        play_the_game = False



 