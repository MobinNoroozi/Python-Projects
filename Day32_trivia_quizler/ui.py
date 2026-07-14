from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain): #It has to be quiz brain type
        self.quiz_brain = quiz_brain #Ui has quiz brain, window, canvas, lable, and button
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        
        self.canvas.grid(row = 1, column = 0, columnspan=2, pady=50)

        self.score_lable = Label(text=f"Score: {self.quiz_brain.score}", bg= THEME_COLOR, fg="white")
        self.score_lable.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image= true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image= false_img, highlightthickness=0, command=self.false_pressed)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)


        self.get_next_question() #Start

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white") #bg needs to be white
        if self.quiz_brain.still_has_questions(): #As long as we have another question, go to the next question
            self.score_lable.config(text=f"Score: {self.quiz_brain.score}")
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text= next_question)
        else: #No more question, then disable buttons and display the text
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question)
            
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)
            
  