from tkinter import *
import pyperclip
from tkinter import messagebox
import random




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    #insert the passord in the password entry when the user click on the generate password button
    password_entry.insert(0, password)
    pyperclip.copy(password) #THis adds it to the clipboard as well





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    #Get the entry from the user
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #If are empty, let them know 
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty. ")
    else:
        #Verify information
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        #If verified
        if is_ok:
            with open("data.txt", "a") as data_file: #Open and append
                data_file.write(f"{website} | 3{email} | {password}\n") #This format
                website_entry.delete(0, END) #Clear the entrys
                password_entry.delete(0, END)
    


# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window =Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50, bg="white")

#Add the image
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column= 1) 

#Add the labels
website_lable = Label(text="Website:", bg="white", fg="black")
email_lable = Label(text="Email/Username:", bg="white", fg="black")
password_lable = Label(text="Password:", bg="white", fg="black")

website_lable.grid(column=0, row=1)
email_lable.grid(column=0, row=2)
password_lable.grid(column=0, row=3)


#Add entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column= 1, columnspan= 2)
website_entry.focus() #Where the cursor starts

email_entry = Entry(width=35)
email_entry.insert(0,"mobin@email.com")
email_entry.grid(row=2, column= 1, columnspan= 2)

password_entry = Entry( width=21)
password_entry.grid(row=3, column= 1)


#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row= 3)

add_button= Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan= 2, row=4)







window.mainloop()