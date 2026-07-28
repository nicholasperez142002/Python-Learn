#Transformations - repalce(), 'H' + 'i', f{}, split(), 'ha' * 2
#                - extraction - 'cat'[0], 'cat'[1:3]


price = "323,564"
print(price.replace(",", "."))
phone = "165-3213-90"
print(phone.replace("-",""))
price = "$1234,56"
print(price.replace("$", "").replace(",",".")) #muliple replace
phone = "+49 (176) 123-4567"
print(phone.replace("+","00").replace("(","").replace(")","").replace(" ", "").replace("-",""))
