print("This code will calculate your bugdet for the month.")
income = input("How much do you make in a month?\n")
rent = input("How much do you pay rent in a month?\n")
utilities = input("How much do you pay in utilities in a month?\n")
groceries = input("How much do you pay in groceries in a month?\n")
transportation = input("How much do you pay in transportation in a month?\n")
expenses = rent + utilities + groceries + transportation
savings = income + 1*0.2/1
total = income-expenses-savings
prent = rent/income
putilities = utilities/income
pgroceries = groceries/income
ptranspotation = transportation/income
pexpenses = expenses/income
print("Your income is: $%.2f\n", income)
print("Your expenses are: $%.2f\n", expenses)
print("Your savings are: $%.2f\n", savings)
print("Your total left to spend is: $%.2f\n", total)
print("Your rent payment is: %.2f", prent, "of your expenses")
print("Your utilities payment is: %.2f", putilities, "of your expenses")
print("Your groceries payment is: %.2f", pgroceries, "of your expenses")
print("Your transportation payment is: %.2f", ptranspotation, "of your expenses")