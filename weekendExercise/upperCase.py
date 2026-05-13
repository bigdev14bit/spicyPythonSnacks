#did, upper case and lowercase together
userInput = input("Enter A Letter: ")

upperCase_count = 0
lowerCase_count = 0

for characters in userInput:
    if characters.isupper():
        upperCase_count += 1
    elif characters.islower():
        lowerCase_count += 1

print("\nUpper Case: ",upperCase_count)
print("\nLower Case: ",lowerCase_count)
