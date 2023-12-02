from email_validator import validate_email, EmailNotValidError

def validate_email_address(email):
    try:
        # Use validate_email from email_validator module
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        # Catch the correct exception and print the error message
        print(f"Error: {str(e)}")
        return False

# Get email address from user input
email_address = input("Enter Your Email Address Here: ")

# Call the validation function and print the result
if validate_email_address(email_address):
    print(f'{email_address} is a valid Email Address.')
else:
    print(f'{email_address} is not a valid Email Address.')
