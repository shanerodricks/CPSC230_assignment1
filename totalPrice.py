import math

#prompt user for price and sales tax rate of item
price = float(input("Enter the price of this item: "))
tax = float(input("Enter sales tax rate: "))

#convert sales tax into decimal number
sales_tax = tax / 100

#perform final calculation to find total price
total_price = price * sales_tax + price

print(total_price)
