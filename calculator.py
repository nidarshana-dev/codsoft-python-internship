print("=== 1CR Salary Calculator ===")
monthly_salary = int(input("Your monthly salary in Rs:"))
performance = input("Your performance - Good/Average/Bad:")
annual_salary = monthly_salary*12
if performance == "Good":
    bonus = annual_salary * 0.20
    print("\nVera level performance da! 20% bonus!")
elif performance == "Average":
    bonus = annual_salary * 0.10
    print("\nNot bad. 10% bonus kedaikum.")
else:
    bonus = 0
    print("\nBad performance. Bonus illa. Next time pakkalam.")
total_income = annual_salary + bonus
print(f"\nYour annual salary: Rs{annual_salary}")
print(f"Your bonus: Rs{bonus}")
print(f"Total 1 year income: Rs{total_income}")
if total_income >= 10000000:
    print("\nDei 1CR vandhachu da! Party podu!")
else:
    need_more = 10000000 - total_income
    print(f"\nInnum Rs{need_more} venum. Next year pakkalam")
    
