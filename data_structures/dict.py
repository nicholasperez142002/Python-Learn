# dictionary - ordered, no duplicates keys, duplicate values, indexable by key access, mutable
#Methods - keys(), values(), items(), get(), update(), popitem()
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 40
}
#difference
print(my_dict) 
print(my_dict['b']) #indexed but by key access
my_dict['c'] = 80 #mutable
print(my_dict)


user = {
    'id':1,
    'age':30,
    'city': 'berlin'
}

#access
#print(user['city'])
print(user.get('name', "Unkown")) #safest way to access data of dict

#checks
print('age' in user)
print('name' not in user)

#view objects
print(user.keys())
print(user.values())
print(user.items())

#looping
for key, value in user.items():
    print(key, value)

#add

user['name'] = 'John' # add new pair
print(user)
user['age'] = 35 # update
user.update({'age':40, 'city':'paris'})
print(user)

age = user.pop('salary', 'not found')
print(user)
print('Removed Item:', age)

user.popitem()
print(user)

#creation
user = {'id': None,
        'name': None,
        'age': None,
        'city': None
        }

# better way than above ^
user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
print(user)

#challenge
# create a new dictionary
#keep only pairs with strings values
#convert values to uppercase

user = {'id': 1, 'name': 'John', 'age': 30, 'city': 'Berlin'}
new_dict = {
    k: v.upper() #expression for transforming
    for k, v in user.items() #loop
    if isinstance(v, str) # filter
}
print(new_dict)