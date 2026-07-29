#Transformations - repalce(), 'H' + 'i', f{}, split(), 'ha' * 2
#                - extraction - 'cat'[0], 'cat'[1:3]

price = "323,564"
print(price.replace(",", "."))
phone = "165-3213-90"
print(phone.replace("-",""))
price = "$1234,56"
print(price.replace("$", "").replace(",",".")) #muliple replace
phone = "+49 (176) 123-4567"
print(phone.replace("+","00").replace("(","").replace(")","").replace(" ", "").replace("-",""))

first_name = "Michael"
last_name = "Perez"
full_name = first_name + " " + last_name
print(full_name)

folder = "C:/users/Nicholas/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

#f-string
name = "Sam"
age= 34
is_student = False
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")
print(f"2 + 3 = {2 + 3}")
print(f"{{This is me}}")

#split()
stamp = "2026-07-28 14:30"
print(stamp.split(" "))
stamp = "2026-07-28"
print(stamp.split("-"))
csv_file = "1234,Nicholas,USA, 1970-10-05,M"
print(csv_file.split(","))

#String Repetition
print("Glad" * 3)
print("===" * 4)

#Exctraction - "string"[start:end]
print("batcatratsat"[1]) #finds char at index
print("batcatratsat"[3:8])
print("batcatratsat"[0:-8]) #when using negative, it counts right to left
print("batcatratsat"[1:]) # if not specified, it will go to end of string
print("ABCDEFGHIJ"[1:8:2]) # "string'[start:end:step] 'step' is 'skip every x'
#indexes & slicing
text = "Python"
#extract first character
print(text[0])
print(text[-6])
#extract the last character
print(text[5])
print(text[-1])
#extract the char 'h'
print(text[3])
print(text[-3])
# extract only the year
date = "2026-07-28"
print(date[0:4])
print(date[0:-6])
#extract the month
print(date[5:7])
print(date[-5:-3])
#extract the day
print(date[8:])
print(date[-2:])