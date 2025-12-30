
import re

email_condition = r'^[a-z][a-z0-9]*([._]?[a-z0-9]+)*@[a-z]+\.[a-z]{2,3}$'

user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print("This email is correct")
else:
    print("Invalid Email")
