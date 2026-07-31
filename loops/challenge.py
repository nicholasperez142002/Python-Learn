#Check whether any filename appears more than once
#Print"Duplicate found" if a duplicate exist,
#otherwise print "All files are unique"

file_list = ['report.csv',
             'data.xlsx',
             'summary.docx',
             'report.csv',
             'data.csv']
seen = []
for file in file_list:
    if file in seen:
        print("Duplicate Found")
        break
    seen.append(file)
else:
    print('All files are unique')