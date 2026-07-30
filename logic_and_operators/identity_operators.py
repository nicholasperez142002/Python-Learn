#identity operators - is, is not
# checks if two variables point to the same spot in memeory

a = [1,2,3]
b = [1,2,3]
print(a is b)

#they are stored as the same object so True
a = 4
b = 4
print(a is b)

a = [1,2,3]
b = a
print(a is b)

#task - make sure the email exists, and it's not empty
email = None
print(email is not None and email != '')
