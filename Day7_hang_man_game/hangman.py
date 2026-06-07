import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
# Users have 6 lives for the game
lives = 6 

# Randomly choose a word in the word list
chosen_word = random.choice(word_list) 

# A placeholder to tell the user how many letters will be in the word
placeholder = "" 

# Gets the lengh of the word
word_length = len(chosen_word) 

# Creates an _ per letter in the chosen word
for position in range(word_length): 
    placeholder += "_"
    
# Print it
print(placeholder) 

# Creates a list of the correct letters 
correct_letters = []

# Boolean that determine if the game is over.
game_over = False

# Logic of the game continues and they start with 6 lives
while not game_over:
    print(f"**********************{lives}/6 LIVES LEFT**********************")

    # Ask user to guess a letter
    guess = input("Guess a letter in the word: ").lower()

    # If the guessed letter is in the list of correct letters just let then know
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    # This is what we display nd it will get updated further down 
    display = "" 

    # If the guessed letter is in the chosen word add it to the display and the correct letters list
    for letter in chosen_word:
        if(letter == guess):
            display += letter
            correct_letters.append(letter)

        # If the letter already exist in the correct letters add it to the display, because each time the display gets cleared
        elif letter in correct_letters:
            display += letter

        # If guessed letter is not int the chosen word, then keep a _ there
        else:
            display += "_"

    # print the display
    print("Word to guess: " + display)
    

    if guess not in chosen_word:
        lives -= 1
        # Let then know what they guessed
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"**********************IT WAS {chosen_word}! YOU LOSE**********************")
            

    if "_" not in display:
        game_over = True
        print("**********************YOU WIN**********************")


    print(stages[lives])



      
      





