#allow up to 3 attempts
#if the user types 'yes', print 'glad we are on the same page'
#otherwise, print '3 strikes, you are out'

attempts = 0 #starting at 0 attempts
while attempts < 3: #condition 
    answer = input("Do you agree? (yes/no): ") #prompts question immediately
    if answer == "yes": #condition 
        print('glad we are on the same page') #print before break if yes
        break
    attempts += 1 #adds one to our attempts counter if not yes
else:
    print('3 Strikes, you are out')

