print(f"{'Principal':<15}{'Years to Maturity':>20}{'Interest Rate':>15}")

principal = int(input("Enter principal amount: "))
print()
if principal > 100000:
    years = 5
    interest_rate = 6

elif 50000 <= principal <= 100000:
    years = 10
    interest_rate = 5

else:
    years = 5
    interest_rate = 4

YearofInterest = principal * interest_rate

print(f"{'Principal':>10}{'Years to Maturity':>20}{'Interest Rate':>15}")
print(f"${100000:>10,.2f}{5:>10}{6:>20.0f}%")
print(f"${50000:>10,.2f}{10:>10}{5:>20.0f}%")
print(f"${50000:>10,.2f}{5:>10}{4:>20.0f}%")
print(f"${principal:<10,.2f}{years:>10}{interest_rate:>20.0f}%")
print()
print(f"Your first year interest is ${YearofInterest:>10,.2f}")