#allow up to 3 attempts
#if the user types 'yes', print 'glad we are on the same page'
#otherwise, print '3 strikes, you are out'
count = 0
while count < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print('glad we are on the same page')
        break
    count += 1
else:
    print('3 Strikes, you are out')

