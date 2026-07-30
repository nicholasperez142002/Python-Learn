#if-statements
# if condition:
#       do A

score = 100
if score >= 90:
	print('A')

#else-statments
#must come last and after if
score = 85
if score >= 90:
	print('A')
else:
	print('F')

#else-if statements
score = 70
if score >= 90:
	print('A')
elif score >= 80:
	print('B')
elif score >= 70:
	print('C')
elif score >= 60:
	print('D')
else:
	print('F')

#nested-if statments
score = 95
submitted_project = True
if score >= 90:
	if submitted_project:
		print('A+')
	else:
		print('A')
elif score >= 80:
	print('B')
elif score >= 70:
	print('C')
elif score >= 60:
	print('D')
else:
	print('F')

#nested-if with operators
score = 95
submitted_project = True
if score >= 90 and submitted_project:
	print('A+')
elif score >= 90:
	print('A')
elif score >= 80:
	print('B')
elif score >= 70:
	print('C')
elif score >= 60 or submitted_project:
	print('D')
else:
	print('F')

#independent-if statement
score = 50
submitted_project = False

if score >= 90:
	print('High Score')
else:
	print('Low Score')

if submitted_project:
	print('Project is submitted')
else: print('Project is not submitted')

#inline-if statment (ternary)
#used only in simple logic
score = 80
print('A' if score >= 90 else 'F') # can also assign it to variable and print

grade = "A" if score >= 90 else 'B' if score >= 80 else 'C'
print(grade)

#case-match
country = "United States"

match country:
	case "United States" | "USA":
		print("US")
	case "India":
		print("IN")
	case "Egypt":
		print("EG")
	case "Germany":
		print("DE")
	case _: # '_' is known as
		print("Unkown Country")


