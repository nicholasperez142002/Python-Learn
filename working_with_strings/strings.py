#String functions, methods, and  to know

#Types - type(), str()
#Math - len(), count()
#Transformations - repalce(), 'H' + 'i', f{}, split(), 'ha' * 2
#                - extraction - 'cat'[0], 'cat'[1:3]
#Cleaning - whitespaces - lstrip(), rstrip(), strip()
#         - clean cases - lower(), upper()
#Search - startswith(), endswith(), find(), 'a' in 'cat'
#Validation - isalpha(), isnumeric()

#Types
name = "Nicholas"
print(type(name))

age = 24
print(type(age))
print("Your age is:" + str(age))

#Math

password = "123a"
print(len(password))

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
print(text.count("Python")) #method

#Transformers

price = "323,564"
print(price.replace(",", "."))
phone = "165-3213-90"
print(phone.replace("-",""))
price = "$1234,56"
print(price.replace("$", "").replace(",",".")) #muliple replace
phone = "+49 (176) 123-4567"
print(phone.replace("+","00").replace("(","").replace(")","").replace(" ", "").replace("-",""))
