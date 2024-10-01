age = int(input("How old are you?\n"))
voter = "yes"
if age == 999:
    print("How are you still alive?")
elif age >= 18 and voter == "yes":
    print("You are able to vote!\n")
elif age >= 16:
    print("You are old enough to drive\n")
elif age >= 15:
    print("You are old enough to get a learners permit!\n")
elif age >= 5:
    print("You are old enough to go to school!\n")
else:
    print("You are to young to go to school :(\n")



