principal = float(input("What is the principal amount? "))
years = int(input("How many years to maturity? "))

if principal > 100000:
    interest_rate = 6

elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 5

elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 4

else:
    interest_rate = 2

# Calculate first year's interest
YearofInterest = principal * (interest_rate / 100)
print()
print(f"{'Principal':>18}{'Years':>10}{'Interest Rate':>18}{'Interest Amount':>22}")
print(f"${principal:>17,.2f}{years:>10}{interest_rate:>17.2f}%{'$' + format(YearofInterest, ',.2f'):>22}")