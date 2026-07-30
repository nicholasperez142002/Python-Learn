#rounding
#built in functions - abs(), round()
#math module functions - ceil(), floor(), trunc()
import math
#measure distance form two points
print(abs(2 - 10)) #absolute value
#rounding numbers
price = 35.583983
print(round(price))#rounds to nearest whole number
print(round(price, 2)) # rounds to two decimal places
print(math.floor(price)) #rounds down to nearest whole number
print(math.ceil(price)) #rounds up to nearest whole number
print(math.trunc(price)) # does not round but only cuts off decimals
print(int(price)) #does the same as trunc but with some nuance
