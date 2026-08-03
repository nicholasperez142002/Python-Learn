# List - ordered by collection of items, changeable, allows duplicates
# format -> variable name = [] <- brackets

#How to create a list

empty = []
letters = ['a','b','c']
numbers = [1,2,3]
mixed_list = [1, 'a', True, None]
print(letters)
print(type(letters))
print(numbers)
print(mixed_list)

empty = list()
print(empty)
letters = list('Python')
print(letters)
numbers = list(range(5))
print(numbers)

matrix = [['a','b','c'],
          ['d','b','f']]
print(matrix)
print(type(matrix))
mixed_matrix = [['a','b'],
                [1,2,3],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))

#access and read lists

lst = ['a','b','c','d']
print(lst[0]) #indexing from front
print(lst[-1]) # indexing from end

matrix = [
    ['a','b','c'],  #row 0
    ['d','e','f'],  #row 1
    ['g','h','i']   #row 2
]
print(matrix) #access the whole matrix
print(matrix[2]) # access the whole row
print(matrix[2][2])
print(matrix[1:]) # splicing
print(matrix[2][:2]) # splicing

#splicing a list (can also do the same for the matrix)
list1 = ['a','b','c','d']
print(list1[:2])
print(list1[2:])

#unpacking a list
person = ['Maria',29,'Data Engineer', 'Spain']
name, age, role, country = person
print(name)
print(country)
name, *details, country = person # using '*details' only unpacks what you name and order matters
print(name)
print(details)
print(country)
*details, country = person
print(country)
*details, role, country = person
print(details)
print(role)
print(country)

#rules of unpacking

#num of variables must match the values exactly
person = ['Maria', 29, 'Data Engineer','Spain']
name, _, role, _ = person # use '_' so you dont have to make a variable for each when the data doesnt matter
print(name)
print(role)

name, *_, country = person # can combine * and _ to remove completely 
print(name)
print(country)

#explore and analyze data

numbers = [1,5,2,4,3,5]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers)) #works only with numbers
print("Length:", len(numbers))

print("All:", all(numbers)) #give True if ALL are True
print("Any:", any([1, None, 2])) #give True if at least one value is true

print("Count:", numbers.count(5))
print("Index:", numbers.index(5))

print(4 in numbers)
print(8 in numbers)
print(8 not in numbers)

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)
print(list is list2) #stored in two different spots in memory so false

#changing the list - append(value), insert(index, value), clear(), remove(value)
letters = ['a','b','c']
letters.append('d') #adds at the end
letters.append('x') #adds at the end
letters.insert(0, 'x') #inserts at index
letters.insert(3, 'y') #inserts at index
print(letters)

matrix = [
    ['a','b','c'],  #row 0
    ['d','e','f'],  #row 1
    ['g','h','i']   #row 2
]
matrix.append(['j','k','l'])
matrix.insert(0,['a','a','a'])
print(matrix)

matrix = [
    ['a','b','c'],  #row 0
    ['d','e','f'],  #row 1
    ['g','h','i']   #row 2
]
matrix[1].append('x') #chooses which matrix and then adds to back
matrix[0].insert(0,'z') # chooses which matrix and then chooses where in specific 
print(matrix)

#Clear()
letters = ['a','b','c']
letters.clear() #destroys whole list
print(letters)

#Remove()
letters = ['a','b','c']
letters.remove('a')
print(letters)

#pop(index)
letters = ['a','b','c','d','e','f']
removed = letters.pop(-2)
print(letters)
print('Removed Items:', removed)

# how to update values
letters = ['a','b','c','d','e','f']
letters[0] = 'x'
print(letters)

#sorting lists - sort() -> this method modifies the original
letters = ['a','d','c','f','e','b']
letters.sort()
print(letters)
letters.sort(reverse = True)
print(letters)

#sorted() -> this function creates a new copy and sorts that to be stored in a new variable.
letters = ['c','a','b']
sorted_list = sorted(letters)
rever_sorted = sorted(letters, reverse = True)
print("Original List:", letters)
print("Sorted List:", sorted_list)
print("Reverse List:", rever_sorted)

# Reversing a List - reverse(), reversed()
letters = ['c','a','b']
letters.reverse()
print(letters)

#reversed() - function that reverses the a new copy of the original list keeping it unchanged.
letters = ['c','a','b']
new_list = list(reversed(letters))
print('Original List:', letters)
print('New List:', new_list)

#How to copy list

#assignmet copy - not safe becasue it chagned all variables (dont do)
letters = ['a','b','c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

# Shallow Copy -> copy() method creates a new list separate from the original list with its own pointer 
letters = ['a','b','c']
letters_copy = letters.copy()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

#Matrix Shallow Copy -> copy() method
matrix = [
    ['a','b'],  #row 0
    ['c','d'],  #row 1
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:', matrix_copy)

#Deep Copy - Import module copy -> deepycopy(), copy() 
import copy
matrix = [
    ['a','b'],  #row 0
    ['c','d'],  #row 1
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:', matrix_copy)

#how to check if two variables refer to the same object
import copy
original = [
    ['a','b'],  #row 0
    ['c','d'],  #row 1
]

#assignment
copy1 = original
print('Same Object?', original is copy1, '\n')

#Shallow Copy
copy2 = original.copy()
print('Same Object?', original is copy2)
print('Sahred Lists?', original[0] is copy2[0], '\n')

#Deep Copy
copy3 = copy.deepcopy(original)
print('Same Object?', original is copy3)
print('Sahred Lists?', original[0] is copy3[0], '\n')

#How to combine lists

#using '+'
letters = ['a','b','c']
numbers = [1,2,3]
combination = [letters, numbers]
print(combination)

#using extend()
letters = ['a','b','c']
numbers = [1,2,3]
numbers.extend(letters)
print(letters)
print(numbers)

# using zip()
letters = ['a','b','c']
numbers = [1,2,3]
combine = list(zip(letters, numbers))
print(combine)

#real example
id = [101,102,103]
names = ['Ali','Sara','John']
combine = list(zip(id, names))
print(combine)

#how to iterate through list
letter = ['a','b','c']
new_list =[]
for l in letters:
    new_list.append(l.upper())
    print(new_list)

#enumerate() -> loops and gets the index and the value pair
letters = ['a','b','c']
for index, value in enumerate(letters):
    print(index, value)

#reversed()
letters = ['a','b','c']
for l in reversed(letters):
    print(l)

#zip()
letters = ['a','b','c']
numbers = [1,2,3]
for n, l in zip(numbers, letters): #order matters in output here 
    print(n, l)

#map(function, iterable)
letters = ['a','b','c']
print(list(map(str.upper, letters)))
numbers = ['1','2','3']
print(list(map(int, numbers)))
names = [' Maria ', 'John ', ' Kumar']
for n in map(str.strip, names):
    print(n)

#filter(function, iterable)
letters = ['a','','b',None,'c', False]
for l in filter(None, letters):
    print(l)

items = ['sql', '123', 'python', '42']
for i in filter(str.isalpha, items):
    print(i)

#lambda function -> 
multiple = lambda x: x*2
print(multiple(2))
addition = lambda x,y: x + y
print(addition(2,3))
check = lambda i: i in 'python'
print(check('n'))

prices = ['$12.50','$9.99','$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))

students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[1] > 70, students)))

#Challene - keep only the students with names starting with 'M'
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[0].startswith('M'), students)))

#List comprehension
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.NICHOLASPEREZ.COM']
cleaned_domains = [
    d.lower().replace('www.', '')
    for d in domains
    if '.' in d
]
print(cleaned_domains)


