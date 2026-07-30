#email must not be empty
#email must contain a '.' and '@'
#email must contain exactly one '@' smybol
#email must end with '.com', '.org', or '.net'
#email must not be longer than 254 characters
#email must start and end with a letter or digit

email = "Nicholas@gmail.com "
email = email.strip()

if email == "":
    print("Email must not be empty")
elif not('.' in email and '@' in email):
    print("Email must contain . and  @")
elif email.count('@') != 1:
    print("Email must have one '@' symbol")
elif not email.endswith(('.com','.org','.net')):
    print("Email must end '.com', '.org', or '.net'")
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
elif email[0].isalnum() and email[-1].isdigit():
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")