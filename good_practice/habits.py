# This file is to check for good habits on coding style
# PEP8

#bad fucntion styling.
#def DiscPrint(p, r):
#    print("calculating discount")
#    p = p - (p * r/100)
#    print(p)
#DiscPrint(80,20)


# correct pep8
def calculate_discount(price: float, rate: float)-> float:
    """
    Calculate the final price after applying a discount.
    Args:
        price (float): Original Product Price.
        rate (float): Discount Rate as numbers (e.g 20 for 20%)
    Returns:
        final_price (float): Final Price after applying discount.
    """
    final_price = price - (price * rate/100)
    return final_price

print(calculate_discount(80,20))

