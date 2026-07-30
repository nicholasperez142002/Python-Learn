#Boolean
#functions - all(), any(), isinstance(), bool()
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool('Hi'))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

email = ""
phone = "985-540-3291"
username = ""
# Allow registration if any fields is filled
print(any([email, phone, username])) # only one has to be fulfilled
# Allow regisstration only if all fields are filled
print(all([email, phone, username])) #all must be fulfilled

print(isinstance(123, int))
print(isinstance(True, str))
