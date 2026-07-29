#Cleaning - clean whitespaces - lstrip(), rstrip(), strip()
#         - clean cases - lower(), upper()

# lstrip() - 'left strip'
text = " Engineering".lstrip()
print(text)
text = "Engineering ".rstrip()
print(text)
text = "      Engineering  ".strip()
print(text)
text = "###Abc###".strip("#")
print(text)

text = " Engineering"
print(len(text))
print(len(text.strip()))
print(len(text) - len(text.strip()))
num_of_spaces = len(text) - len(text.strip())
print("Number of spaces:", num_of_spaces)
print(len(text) == len(text.strip()))
is_clean = len(text) == len(text.strip())
print("Is my data cleaned?", is_clean)


#case conversion

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

search = "Email".lower().strip()
data = " emAil".lower().strip()

print(search == data)

#Challenge
# Take this messy string "968-Maria, ( D@t@ Engineer );; 27  "
# Clean it to output: "name: maria | role: data engineer | age: 27"
messy = "968-Maria, ( D@t@ Engineer );; 27  "
print(messy.strip().replace("@","a").strip("968-").replace("("," | ").replace(")"," | ").replace(";",""))
print(messy.strip("968-").strip(",").replace("("," | ").replace(")"," | "))

