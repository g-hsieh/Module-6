part = int(input("Enter the part number: "))
quantity = int(input("How many units did you order? "))

if part == 10 or part == 55:
    UnitCost = 1.00

elif part == 99:
    UnitCost = 2.00

elif part == 80 or part == 70:
    UnitCost = 3.00

else:
    UnitCost = 5.00

total = quantity * UnitCost

print()
print(f"{'Cost per unit':>15}{'Total amount':>20}")
print(f"${UnitCost:>14.2f}{'$' + format(total, ',.2f'):>20}")