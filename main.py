##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "xyz@gmail.com"
PASSWORD = "your_password"
PLACEHOLDER = "[NAME]"

today = (dt.datetime.now().month, dt.datetime.now().day)
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if today in birthday_dict:
    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    file_parh = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    name = birthday_dict[today]['name']
    email = birthday_dict[today]['email']
    with open(file_parh, 'r') as file:
        read_letter = file.read()
        new_letter = read_letter.replace(PLACEHOLDER, name)

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{new_letter}"
        )
