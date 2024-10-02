import datetime

now=datetime.datetime.now().hour-6

print(now)

if now <= 12:
    print("Good Morning!\n")
elif now <= 18:
    print("Good afternoon!\n")
elif now <= 20:
    print("Good evening!\n")
else:
    print("Good night! GO to bed!")