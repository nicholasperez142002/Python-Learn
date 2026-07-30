#membership operators - in, not in
# using 'in'
print('o' in 'Python')
# using 'not in'
print(3 not in [1,2,3])

#Task - Validate that the domain is not on the banned list.
domain = 'gmail.com'
is_banned = ['yahoo.com', 'spam.com','fake.org']
print(domain not in is_banned)