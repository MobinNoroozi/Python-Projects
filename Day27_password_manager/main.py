from tkinter import *
import pyperclip
from tkinter import messagebox
import random
import json



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



# ---------------------------- SEARCH ------------------------------- #
def search_website():
    website = website_entry.get() #Hold onto the entry that the user entered

    if  len(website) == 0: #If empty, show an error and return
        messagebox.showinfo(title="Oops", message="Make sure that the website field is not empty.")
        return
    
    try: #try to open the json data, and get the data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError: #If the file does not exist, let them know in a messagebox
        messagebox.showinfo(title="No Database", message= "Database does not exist.")
    
    except json.JSONDecodeError: #If the database is empty, let them know.There is nothing in there, so search cannot happen
        messagebox.showinfo(title="Invalid Database", message= "The database is empty.")
    
    else:
        email_found = None
        password_found = None

        for key, value in data.items():
            if(key == website): #if the website is in the json file. get the email and the password and assign them
                email_found = value["email"]
                password_found = value["password"]                    

                #Once we get them, show them in a messagebox
                messagebox.showinfo(title="Searched Website",
                                    message=(
                                        f"Website: {website}\n"
                                        f"Email: {email_found}\n"
                                        f"Password: {password_found}"
                                    )
                )
        #If both email, and password are None, it means that the website was not in the database
        if(email_found == None and password_found == None):
            messagebox.showinfo(title="Not In Database", message="Website entered is not in database.")

    finally:
        website_entry.delete(0, END) #No matter what after each search, remove the data in the entry
            


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    #Get the entry from the user
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    new_data = {
        website:{
            "email" : email,
            "password" : password,
        },
    }


    #If are empty, let them know 
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty. ")
        website_entry.delete(0, END) #Clear the entrys
        password_entry.delete(0, END)
        return
   
   
    else:
        try: #Try to open and hold onto the data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                
        
        except: #if there is an exception, create a file, and add the new data into it
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else: #If not error, update the json data, and write it in the json file
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally: #No matter what, clear the fields
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
website_entry = Entry(width=21)
website_entry.grid(row=1, column= 1)
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

search_button = Button(text="Search", command=search_website, width=13)
search_button.grid(column=2, row=1)






window.mainloop()