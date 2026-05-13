print("=" * 70)
print(" PASSWORD STRETGHT CHECKER ")
print("=" * 70)

userInput = input("Enter Password: ")

#symbols = "~!@#$%^&*(){}|:<>?/'`=+-_"

if len(userInput) >= 10:
    print("STRONG!!!")
elif len(userInput) >= 6:
    print("MEDIUM!")
elif len(userInput) < 1:
    print("WEAK")
else:
    print("Invalid")
