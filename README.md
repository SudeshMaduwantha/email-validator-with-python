# email-validator-with-python
This is a Email validator in python programming
 
#This is created by sudesh maduwantha.
All right recieved!!!

before the run you need to install these package into your project.

follow these steps to setup :

01 ->   Open a new terminal window 
02 ->   Then type this code " pip install email-validator "
03 ->   Then this package will automatically install your project.
04 ->   Now Run the program.

This is the somekind of other method .This is also work correctly.

-----------------------------------------------------------------------
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-0-9-,]+$'

    match = re.match(pattern,email)

    return bool(match)

email_address =input("Enter Your Email Address Here : ")

if validate_email(email_address):
    print(f'{email_address} is a valid Email Address.')
else:
    print(f'{email_address} is not a validate Email Address')

-----------------------------------------------------------------------
