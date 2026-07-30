#logical operators - and, or, not
# 'and' has priority over 'or'
# parenthesis will prioritize  'or' if within
print(3 < 5 and 5 == 5) # all expressions must be true for True
print(3 > 5 and 5 == 5)

cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)
#check if user creditials work before login
email = True
password = True 
print(email and password)
# use not to flip the result
print(not 3 > 2)
print(not True)

name = ''
print(not name)
print(not 0)
#show normal priority of 'and' over 'or'
print(5 == 5 or 8 > 5 and 6 < 4 ) # and executes first then or and shows True
#show parenthesis 'or' priority
print((5 == 5 or 8>5) and 6 < 4) # shows False

#task - Allow acces only if the user is logged in or they are guest but they must not be banned
is_logged_in = True
is_guest = True
is_banned = False
print((is_logged_in or is_guest) and not is_banned)