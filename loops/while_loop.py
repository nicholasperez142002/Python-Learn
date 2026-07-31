#while-loop

#while-condition loop

i = 1 #must initialize the start
while i < 4:
    print(i)
    i += 1

print('\n')

#task - make a counter that goes from 1-5
count = 1
while count <= 5:
    print(count)
    count += 1

#take user input 
answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank you")

#while true
while True:
    answer = input("Do you agree?(yes/no)")
    if answer == "yes":
        break
print("Thank you")