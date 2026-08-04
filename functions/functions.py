#User defined functions

#Function Declaration
# def function_name(parameter):
#   <line of code>

#Function Call
# function_name(argument)

def make_coffee():
    print("start Machine")
    print('Make coffee')
    print('Add milk')
    print('Enjoy it')
print('Wake up')
make_coffee()
print('Work for a while\n')

import math
#built in
print(len('Python'))
number = 4.2
#import
print(math.ceil(number))
#user-defined
def greet():
    print("hello")
greet()

#Function work
case_rule = 'lower'
def clean_text(name): # parameter = name
    cleaned = name.strip().lower() #local variable
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print('Cleaned Value:', cleaned)
clean_text(' Nicholas  ')

#positional and keyword arguments

def clean_name(first_name, last_name, country='n/a'):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print('Full name:', full_name, 'From' , country)
#positional mapping - order matters
clean_name(" MariA  ", " PereZ  ", "United States")

#keyword mapping - order does not matter
clean_name(country="United States", first_name='  MariA  ', last_name= ' PereZ  ')

#mixed arguments
clean_name(' MariA  ', last_name=' PereZ  ', country="United States")

#Default Parameter 
clean_name(' MariA  ', last_name=' PereZ  ')

# *args - takes on 'n' number of positional arguments 
# use when same type

#calc the total of multiple values
def total(*args):
    print(sum(args))
total(1,2,3)
total(1,2,3,4)
total(1,2,3,4,5)

# **kwargs - takes on 'n' number of keyword arguemnts
# use when different types

#creates a user profile using **kwargs
def create_user(**kwargs):
    print(kwargs)

create_user(first_name='no',
            last_name='Nicholas',
            age=33,
            country='United States')

def cleaned_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned
lo_name, up_name = cleaned_name(' MariA  ')
print(lo_name, up_name)

#task - store applicatio log messages in a file whneever an event occurs

#def write_log(message):
#    with open(r"/Users/nicholasperez/Desktop/Python-Learn/functions/app.txt", "a") as file:
#        file.write(message + '\n')
#write_log('App Started')
#write_log("User logged in")
#write_log("App Stopped")

#task - clean an email and split it into username and domain

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username, domain = cl_email.split('@')
    return {"username": username,
            "domain": domain}

print(clean_and_split_email("   NIchoLas@gmail.coM "))

#validation function

#task - check if a password is valid
def is_valid_password(password):
    return len(password) >= 8
print(is_valid_password("123456"))
print(is_valid_password("12345678"))

#task - check if email has a basic valid format

def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email('Nicholasgmail.com'))
print(is_valid_email('Nicholas@gmailcom'))
print(is_valid_email('Nicholas@gmail.com'))




    



