
def inp(type):
    input("How much is your "+type+"?\n")
    return f"How much is your "+type+"?\n"

def percent(type, amount):
    per = amount/income*100
    print("Your"+type+"is"+per+"% of your income.\n")

print("This code will calculate your bugdet for the month.")
income = inp("income")
rent = inp("rent")
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
print("Your income is: $", income)
print("Your expenses are: $", expenses)
print("Your savings are: $", savings)
print("Your total left to spend is: $", total)
print("Your rent payment is: ", prent, "percent of your expenses")
print("Your utilities payment is: ", putilities, " percent of your expenses")
print("Your groceries payment is: ", pgroceries, " percent of your expenses")
print("Your transportation payment is: ", ptranspotation, " percent of your expenses")