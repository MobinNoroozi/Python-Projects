from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN =  20
reps = 0 #Global variables
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): #Reset the timer
    window.after_cancel(timer) #Stops the timer and reset everything
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if (reps % 8 == 0): #Every 8 reps long break
        count_down(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    elif(reps % 2 == 0): #Every 2 reps short break
        count_down(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60) # I need these in terms of seconds
    count_sec = count % 60
    if count_sec < 10: #This makes the seconds to be in the proper format
        count_sec = f"0{count_sec}"

    #Proper fomat for the timer text lable on the canvas
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    #as long as it is not 0, run count_down with 1 less count every 1 second
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)   
    else: #If 0, start it
        start_timer()
        mark = "" #For every 2 reps, add a check mark
        for _ in range(math.floor(reps/2)):
            mark += "✔️"
        check_marks.config(text=mark)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk() # #Assigning the window 
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW) #makes the window padd this amount on each side



#Creates the Timer lable in the beginning and is at the center top because we are using the grid system
title_lable = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg= YELLOW)
title_lable.grid(column=1, row=0)

canvas = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0) #Size of the tomato pic
tomato_img = PhotoImage(file="tomato.png") #Canvas needs us to convert this before we can show pics
canvas.create_image(100, 112, image = tomato_img) #Add the image

timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_buttom = Button(text="Start", highlightthickness=0, command= start_timer)
start_buttom.grid(column=0, row=2)

reset_buttom = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset_buttom.grid(column=2, row=2)


check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)



window.mainloop() #Makes the window to show up


