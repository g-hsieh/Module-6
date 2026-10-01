quantity = float(input("Enter the quantity of widgets you ordered: "))
print()
if quantity < 5000:
    Price = 30.00
elif quantity <= 10000:
    Price = 20.00
else:
    Price = 10.00
    
extPrice = quantity * Price
tax = extPrice * 0.07
total = extPrice + tax
print(f"{'Extended Price':<15}${extPrice:10.2f}")
print(f"{'Tax Amount':<15}${tax:10.2f}")
print(f"{'Total Amount':<15}${total:10.2f}")