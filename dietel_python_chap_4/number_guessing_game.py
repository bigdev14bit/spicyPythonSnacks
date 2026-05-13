import random

def number_guessing_game():
    secret = random.randint(1, 1000)  # pick secret number
    print("Guess my number between 1 and 1000 with the fewest guesses: ")

    while True:
        guess = int(input('Your guess: '))

        if guess < secret:
            print('Too low. Try again.')
        elif guess > secret:
            print('Too high. Try again.')
        else:
            print('Congratulations. You guessed the number!')
            break  # exits the while loop

# Outer loop: ask to play again
while True:
    play_game()
    again = input('Play again? (yes/no): ').strip().lower()
    if again != 'yes':
        print('Thanks for playing!')
        break
