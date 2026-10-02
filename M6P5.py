LastName = str(input("What's your last name? ")) 
JobLevel = float(input("What is your job level? ")) 
Salary = int(input("What's your salary? ")) 
print() 
if JobLevel >= 10:
    BonusRate = 0.25
elif 5 <= JobLevel <= 9:
    BonusRate = 0.20
else:
    BonusRate = 0.10
    
Bonus = Salary * BonusRate
print(f"{'Last Name':<15}{'Salary':>15}{'Bonus':>15}")
print(f"{LastName:<15}{'$' + format(Salary, ',.2f'):>15}{'$' + format(Bonus, ',.2f'):>15}")