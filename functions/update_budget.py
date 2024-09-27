def inp(type):
    var = float(input("What is your{type}?"))
    return var


print("This code will calculate your bugdet for the month.")
inp("income")
inp("rent")
utilities = input("How much do you pay in utilities in a month?\n")
Iutil = int(utilities)
groceries = input("How much do you pay in groceries in a month?\n")
Igroc = int(groceries)
transportation = input("How much do you pay in transportation in a month?\n")
Itrans = int(transportation)
expenses = Irent + Iutil + Igroc + Itrans
Iexp = int(expenses)
savings = Iincome *0.2
Fsav = float(savings)
total = Iincome-Iexp+Fsav
prent = Irent/Iincome
putilities = Iutil/Iincome
pgroceries = Igroc/Iincome
ptranspotation = Itrans/Iincome
pexpenses = Iexp/Iincome

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