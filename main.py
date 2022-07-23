import os
import random
import smtplib
import datetime as dt
import pandas as pd

my_email = os.getenv("EMAIL_17")  #enter your email
my_password = os.getenv("EMAIL_17_PASSWORD")  #enter google account, security, app password
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


##################### Hard Starting Project ######################

def birthday_message(name, email):
    with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()  # makes connection secure
        connection.login(user=my_email, password=my_password)

        with open("quotes.txt") as data_file:
            all_quotes = data_file.readlines()
            quote = random.choice(all_quotes)

        letter_choice = random.choice(os.listdir("C:/Users/Sean/PycharmProjects/Day32_Automated_Email_SMTP/"
                                                 "letter_templates"))  #this must match your directory to this folder
        with open(f"letter_templates/{letter_choice}") as letter_data:
            letter = letter_data.readlines()
            letter_text = ""
            letter_text = letter_text.join(letter)
            letter_text = letter_text.replace("[NAME]", name)
            letter_text = letter_text.replace("Angela", "Sean")

        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{letter_text}\n\n\n"
                                f"P.S. For some extra inspiration: {quote}")


#Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
for i in birthday_dict:
    if i["month"] == month and i["day"] == day:
        birthday_message(email=i["email"], name=i["name"])
