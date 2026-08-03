#List, Tuples, Set, and Dict 
# This file will go over each of the data structures and
# will go over; ordered, duplicates, indexed, mutable.

#list[] - ordered, indexed, duplicates, mutable
my_list = [10,30,20,10]
print(my_list) # ordered and allows duplicates
print(my_list[1]) # indexed
my_list[3] = 40
print(my_list)  #mutable

#tuples() - ordered, indexed, duplicates, immutable
my_tuple = (10,30,20,10)
print(my_tuple) # ordered and allows duplicates
print(my_tuple[1]) # indexed
#my_tuple[3]=40 # immutable

#set{} - unordered, non-indexed, no duplicates, mutable
my_set = {10,30,20,10}
print(my_set)
my_set.remove(20)
print(my_set)

#methods of sets - discard(), add(), update(), |=
a = {10,20,30,40}
a.add(50)
print(a)
#a.update({1,2})
a |= {1,2}
a.discard(10) # safe to use over remove()
print(a)

#set math operands - union(), interesection(), difference(), symmetric_difference()

#union
b = {30,40,50,60}
print(a.union(b))
print(a | b)

#intersection
print(a.intersection(b))
print(a & b)

#difference
print(a.difference(b))
print(a - b)
print(a - b)

#symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

#set qustion method
a = {30,40}
b = {30,40,50,60}
print(a.issubset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))