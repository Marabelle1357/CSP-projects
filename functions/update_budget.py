def inp(type):
    var = float(input("What is your "+ type + "?"))
    return var


print("This code will calculate your bugdet for the month.")
income = inp("income")
rent = inp("rent")
utilities = inp("utilities")
groceries = inp("groceries")
transportation = inp("transportation")
expenses = rent+utilities+groceries+transportation
Iexp = int(expenses)
savings = income *0.2
Fsav = float(savings)
total = income-Iexp+Fsav


def percent(type, amount):
    per = amount/income*100

    return f"Your {type} is {per}% income."

print("Your income is: $", income)
print("Your expenses are: $", expenses)
print("Your savings are: $", savings)
print("Your total left to spend is: $", total)
print(percent("rent",rent))
print(percent("utilities",utilities))
print(percent("groceries",groceries))
print(percent("transportation",transportation))
print(percent("savings",savings))
print(percent("expenses",expenses))