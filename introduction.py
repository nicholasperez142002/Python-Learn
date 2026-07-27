# This is how you comment
# Multi-line comments
# Use the same hash

print("Hello, this is my first python code.")  # built-in function
print('Hello, this is my first python code.')  # Single quotes
print('\t Hello')  # inserts tab
print("Hello 'Nicholas' how are you")  # using quote within a quote
print("Message1\nMessage2")  # \n creates new line
print("\nMessage3")


# Creating multiline print statment with special characters
print("""Your Learning Path:
\t - Python Basics
\t - Data Engineering
\t - AI""")

#variable assignment
x=1
print(x)
x=2 #variable overwritten
print(x)
y=x+3 # will take 2 because the first x was overwritten
print(y)


print("My name is Nicholas ")
print("Nicholas is learning python")
print("Nicholas wants to be a data science expert.")

name = "Steven"
language = "Python"
print("My name is", name)
print(name, "is learning", language)
print(name, "wants to be a", language, "expert.")

name = "Nicholas" # this will not do anything because python executes line by line

email = "nicholas.com"
print("info@", email)
print("support@", email)
print("www.", email)

name = input("Enter Your Name:") #dynamic value
country = "United States" # hard code value
print(name, "comes from", country)