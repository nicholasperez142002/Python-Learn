#Action Function
#Task - store application log messages in a file
def write_log(message):
    with open(r"/Users/nicholasperez/Desktop/Python-Learn/functions/app.txt", "a") as file:
        file.write(message + '\n')

#Validate Function
def is_valid_email(email):
    return '@' in email and '.' in email
#Transformation Function
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username, domain = cl_email.split('@')
    return {"username": username,
            "domain": domain}

#Orchestrator function 
def processing_user_email(email):
    write_log("Process Started.")
#Check if it is a valid email
    is_valid_email(email)
#If it is not valid, we log the problem
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    else:
        clean_and_split_email(email)
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("process Stopped.")
#If it is valid, we clean it and store structured information
#And we log what happened

#Recieve email from user
email = input("Please enter your email: ")
processing_user_email(email)