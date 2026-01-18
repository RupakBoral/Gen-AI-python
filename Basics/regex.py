import re

# Phone Number Validation

phone_regex = '^(\\+91)\\d{10}$'
phone_number = '+919954174459'

def validPhoneNumber():
    res = bool(re.search(pattern=phone_regex, string=phone_number))
    print(f"Phone number: {res}")


validPhoneNumber()

# Email Validation

email_regex = '^[a-zA-Z0-9._%+-]+@gmail\\.com$'
email = 'rupak@gmail.com'

def validEmail():
    res = bool(re.search(pattern=email_regex, string=email))
    print(f"Email address: {res}")

validEmail()


