"""
    This file tries to load a default file that contains al the words with all of its transtalations. 
    But as the user practice, they might not need to practice the ones that they already know. Just like quizlet. So that is why
    I need to try and except openning file
"""

from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

#GLobal variables. The reason i need them to be global is because their state changes many times throughout the project
current_card = {}
to_learn = {}


try: #Try to open the file. If it is the first time running this program, then that throws an exception
    data = pandas.read_csv("data/words_to_learn.csv")

except (FileNotFoundError, pandas.errors.EmptyDataError): #If file does not exist or it is empty
    original_data = pandas.read_csv("data/french_words.csv") #read the default file
    to_learn = original_data.to_dict(orient="records") #To learn is a dictionary that holds all the key and values extracted from default

else:
    to_learn = data.to_dict(orient="records") # If The file does exist, and no exception is thrown, then to learn comes from the words to learn


#---------------------------NEXT CARD---------------------------
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer) #cancel the timer. Reason is to eliminate flipping the timer when clicked. Just after they waited for 3 seconds.

    if len(to_learn) == 0: #If all the words are covered and nothing in there to learn
        #Boolean: ask if they want to start again
        restart = messagebox.askyesno( 
            title="Congratulations!",
            message=(
                "You learned all the words!\n\n"
                "Would you like to start again with the full list?"
            )
        )
        if restart: #If restart is true, restart the game
            restart_game()
        else:
            window.destroy()
        return #Do not continue here


    current_card = random.choice(to_learn) #choose a random card

    #This assigns the french word and make it appear in the front
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(
        card_word,
        text=current_card["French"],
        fill="black"
    )
    canvas.itemconfig(
        card_background,
        image=card_front_image
    )

    flip_timer = window.after(3000, func=flip_card) #Wait 3 seconds before flipping it


#---------------------------RESTART GAME---------------------------
def restart_game(): #When restarting. Extract data from the original file
    global to_learn

    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

    pandas.DataFrame(to_learn).to_csv(
        "data/words_to_learn.csv",
        index=False
    )
    #And go to the next card
    next_card()


#---------------------------FLIP CARD---------------------------
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")#Change the card title to english and make the text white
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white") #Change the card word to english word
    canvas.itemconfig(card_background, image = card_back_image) #change the background to back image

    
    
#---------------------------FLIP CARD---------------------------
def is_known():
    #Remove that current card (is a dictionary from the dictionary list) from to learn
    to_learn.remove(current_card)

    #Update the csv file
    data = pandas.DataFrame(to_learn)
    data.to_csv(
        "data/words_to_learn.csv",
        index=False
    )
    #Go to next card
    next_card()


#---------------------------UI DESIGN---------------------------

window = Tk()
window.title("Flashy")
window.config( padx=50,pady=50, bg=BACKGROUND_COLOR) #window has 50 padding

flip_timer = window.after(3000, func = flip_card) #Every 3 seconds flip the card

#Get the images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")


canvas = Canvas(width=800, height=526) #Canvas size is the same size of the image
card_background = canvas.create_image(400,263, image=card_front_image) #Canvas image is the center of the canvas that is why we choose 400, and 263, and the image is the front
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic")) #text at center and top with smaller font
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))#text at center and bottom with bigger font

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
right_button = Button(image= right_image, highlightthickness=0 ,command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image= wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

next_card()#Start with next card


window.mainloop()