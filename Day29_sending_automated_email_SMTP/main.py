#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

#Get todays day and month
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv") #Read the csv


"""
👇👇👇 This is the structure of the dictionary
birthdays_dict = { 
    (birthday_month, birthday_day): data_row
}
👇👇👇 This is an example of the dictionary  that is created below
birthdays_dict = {
    (12, 24): Test, test@email.com, 1961,12,21
}
"""
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#If today's date is in the dictionary of birthdays
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple] #Holds the whole row of data

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"]) #Replace the NAME with the person's name


    #Sends the email securely. 
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
