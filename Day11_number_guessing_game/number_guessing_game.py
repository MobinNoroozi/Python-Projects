import random

# Game logic
def hard_or_easy_game(num):
    attempts = num #Number of attempts
    print(f"Number of attempts: {attempts}")

    """Game logic"""
    while (attempts > 0):
        user_guess = int(input("Guess a number between 0 and 100: "))

        if (user_guess == random_number):
            print("You guessed it correct and you win")
            break
        elif(user_guess > random_number):
            attempts -= 1
            if( attempts == 0):
                print(f"You ran out of attempts. You lost! Correct answer was: {random_number}")
                break
            else:
                print(f"Too high. Attempt remaining: {attempts}")
        elif(user_guess < random_number):
            attempts -= 1
            if( attempts == 0):
                print(f"You ran out of attempts. You lost! Correct answer was: {random_number}")
                break
            else:
                print(f"Too Low. Attempt remaining: {attempts}")
    

# Boolean
game_started = True

while(game_started):
    random_number = random.randint(1,99)

    print("Welcome to the number guessing game!")
    print("I am guessing a number between 0 and 100\n")


    diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if (diff_level == "easy"):

        hard_or_easy_game(10)

        play_again = input("If you would like to play another game type 'y'. Otherwise, press any key: ").lower()
        if(play_again == "y"):
            continue
        else:
            print("Goodbye!")
            game_started = False
    elif(diff_level == "hard"):

        hard_or_easy_game(5)

        play_again = input("If you would like to play another game type 'y'. Otherwise, press any key: ").lower()
        if(play_again == "y"):
            continue
        else:
            print("Goodbye!")
            game_started = False

    else:
        continue

