ticket = int(input("How many tickets are you buying for the concert tonight? "))
print()
if ticket >= 25:
    Price = 50.00
elif 10 <= ticket <= 24:
    Price = 60.00
elif 5 <= ticket <= 9:
    Price = 70.00    
else:
    Price = 75.00
    
total = ticket * Price
print(f"{'Tickets':>10}{'Price':>15}{'Total Cost':>15}")
print(f"{ticket:>10}{'$' + format(Price, ',.2f'):>15}{'$' + format(total, ',.2f'):>15}")