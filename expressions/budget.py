print("This code will calculate your bugdet for the month.")
income = input("How much do you make in a month?\n")
Iincome = int(income)
rent = input("How much do you pay rent in a month?\n")
Irent = int(rent)
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