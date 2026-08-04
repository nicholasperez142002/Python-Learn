#Loops

#for loop - # range(start, stop, step)
items = [1,2,3,4,"hi"]
for item in items:
    print(f'Round: {item}')

items = "Python"
for item in items:
    print(f'Round: {item}')
for i in range(1,10):
    print(f'Round: {i}')
for i in range(1,10,2):
    print(f'Round: {i}')


scores = [80,60,50,75]
total = 0
for score in scores:
    total += score
    print("Current total: ", total)
print("Final Total:", total)

#cleaning data with for loops
files = [' Report.csv', 'DATA.csv', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('txt','csv')
    print('Processing', file)

#Task1 - Print the 7-times tables for 1 to 10 using a for loop
for i in range(1,11):
    print(f'7 x {i} =', 7 * i)

#Task2 - print a left-aligned pyramid of stars with 6 rows using a for loop
for i in range (1,7):
    print('*'* i)

#for loop with 'break'
names = ['Nicholas','Michael','Ryan','Adam','Norma','Hector']
for name in names:
    if name == 'Adam':
        print("loop ended")
        break
    print(f'name: {name}')

#for loop with 'continue'
names = ['Nicholas','Michael','Ryan','Adam','Norma','Hector']
for name in names:
    if name == "Adam":
        print("Adam found!")
        continue
    print(f'Name: {name}')

#for loop with 'pass' - it is essentially a place holder
names = ['Nicholas','Michael','Ryan','Adam','Norma','Hector']
for name in names:
    if name == "Adam":
        pass # always comment as a reminder to come back and fill in placeholder
    print(f'Name: {name}')

#Task - Skip weeknds in calendar loop
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']
weekends = ['Saturday', 'Sunday']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')

#Task - Scan through emails and block malicious email
emails = [
    'data@gmail.com',
    'Nicholas@error.gg',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print("SQL injection!")
        break
    print(f'Processing Email: {email}')

#for-else loop - This is used to know when the code break due to condition.
# if no else statment, the for loop had a break.
nums = [1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if num == 5:
        break
    print(f'Number: {num}')
else:
    print("Done counting!")

#task
names = ['Kamara', 'Tuba', None, 'Mounika']
for name in names:
    if name is None:
        print("Found a missing name.")
        break
else:
    print("All names are available")

files = ['file.csv',
         'report.pdf',
         'report2.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        break
else:
    print('All files are CSV')

#Nested for-loop

for x in (1,2,3): # outer loop
    for y in (1,2): # inner loop
        print(x,y)

for x in range(3): #outer loop
    for y in range(2): #inner loop
        for z in range(2): #inner inner loop
            print(x,y,z)

colors = ['red','blue','green']
sizes = ['L','M','S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')

years = [2026, 2027]
months = ['Jan','Feb']
days = range(1,29)
for year in years:
    for month in months:
        for day in days:
            print(f'report_{year}_{month}_{day}.csv')

# how to use it for data science
tables = ['customers','orders','products','prices']
columns = ['id','create_date']
for table in tables:
    for column in columns:
        print(f'SELECT count(*) FROM {tables} WHERE {column} IS NULL;')

