#check if the users name is not empty and the age is greater than or equal to 18
name = "nicholas"
age = 19
print(name != "" and age >= 18)

#check if the password is at least 8 characters long and does not contain spaces
password = '123456789'
print(len(password) >= 8 and password != '')
#check if the users email is not empty, contain '@', and ends with '.com'
email = "nicholas@gmail.com"
print(email != '' and '@' in email and email.endswith('.com'))
#check if a username is a string, is not None, and is longer than 5 characters
username = 'nicholasperez1402'
print(username is not None and len(username) > 5)
#check if the user is either an admin or a moderator, and either they're not banned or they've verified their email
