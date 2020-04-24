import random

# welcome and introductory message
name = input("HI!,What's your name")
print("HI " + name + "," + "WELCOME TO Cee9 GUESS GAME?")

# select a level
print('''
Select a Difficulty level

EASY
MEDIUM
HARD
''')


stage_choice = input('> ').upper()
while stage_choice:

    try:
        if stage_choice == 'EASY':
            print('''
You're in Easy Stage
you have 6 chances to make a random guesses between 1 - 10
        ''')

            secret_number = random.randint(1, 10)
            guess_count = 0
            guess_limit = 6

            while guess_limit:
                guess = int(input("Take a Guess:"))

                if guess != secret_number:
                    guess_limit -= 1
                    print('Guessed wrong, Try again')
                    print('Chances left:' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print('Number cannot be less than 1')

                elif guess > 10:
                    print('Number cannot be greater than 10')

                elif guess == secret_number:
                    print("Good job! You guessed right")
                    break
            else:
                print('Cheers')
# MEDIUM STAGE
        elif stage_choice == 'MEDIUM':
            print('''
Medium Stage Chosen
You have 4 chances to make a random guesses between 1 - 20
        ''')

            secret_number = random.randint(1, 20)
            guess_count = 0
            guess_limit = 4

            while guess_limit:
                guess = int(input("Take a Guess:"))

                if guess != secret_number:
                    guess_limit -= 1
                    print('Guessed wrong, Try again')
                    print('Chances left: ' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print("Number cannot be less than 1")

                elif guess > 20:
                    print('Number cannot be greater than 10')

                elif guess == secret_number:
                    print("Good job! You guessed right")
                    break
            else:
                print('Cheers')

        elif stage_choice == 'HARD':
            print('''
Hard Stage Chosen
You have 3 chances to make a random guesses between 1 - 50
        ''')

            secret_number = random.randint(1, 50)
            guess_count = 0
            guess_limit = 3

            while guess_limit:
                guess = int(input("Take a Guess: "))

                if guess != secret_number:
                    guess_limit -= 1
                    print('Guessed wrong, Try again')
                    print('Chances left: ' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print('Number cannot be less than 1')

                elif guess > 50:
                    print('Number cannot be greater than 10')

                elif guess == secret_number:
                    print("Wow You're amazing!!!")
                    break
            else:
                print('Cheers')
# WANT TO PLAY AGAIN?
        play_again = input('Play Again Y/N? ').upper()
        if play_again.upper() == 'N':
            stage_choice = False
        else:
            stage_choice = True

        print('Thanks for Playing')
    except ValueError:
        print('Invalid Value')