# Search - startswidth(), endswith(), in, find()

phone = '+48-176-12345'
print(phone.startswith('+49'))
email = "nicholas@gmail.com"
print(email.endswith('@gmail.com'))
file = 'file_backup.csv'
print(email.endswith('.csv'))
print('@' in email)
url = "https://api.company.com/v1/data"
print('/api' in url)

phone1  = '661-495-4903'
phone2 = '818-302-1234'
print(phone1[phone1.find('-')+1:])
print(phone2[phone2.find('-')+1:])


