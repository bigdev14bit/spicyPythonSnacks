#collect first number
#collect operator
#collect second number
#run the calculation and display it to users

#e.g: first number: 20
#operator: +
#second number: 20
#result: 40.

print("=" * 70)
print(" \t====SIMPLE CALCULATOR==== ")
print("A simple calculator for simple arithmetic calculation, enter 'QUIT' to 'QUIT'")
print("=" * 70)

while True:
    first_number = input("\nEnter First Number, or 'quit' to quit: ")
    if first_number == "quit":
        print("T e r m i n a t e d")
        break

    operator = input("\nEnter Operator, (+, -, /, //, *, **, %): ")

    second_number = input("\nEnter Second Number: ")

    if operator == "+":
        print("\nResult: ", int(first_number) + int(second_number))

    elif operator == "-":
        print("\nResult: ", int(first_number) - int(second_number))

    elif operator == "/":
        if int(second_number) == 0:
            print("\nError Division By Zero")
        else:
            print("\nResult: ", int(first_number) / int(second_number))

    elif operator == "//":
        if int(second_number) == 0:
            print("\nError Division By Zero")
        else:
            print("\nResult: ", int(first_number) // int(second_number))

    elif operator == "*":
        print("\nResult: ", int(first_number) * int(second_number))

    elif operator == "**":
        print("\nResult: ", int(first_number) ** int(second_number))

    elif operator == "%":
        print("\nResult: ", int(first_number) % int(second_number))
        
        if int(first_number) % 2 == 0 and int(second_number) % 2 == 0:
            print(first_number, " and", second_number, " are even numbers")
        elif int(first_number) % 2 != 0 and int(second_number) % 2 != 0:
            print(first_number, " and", second_number, " are Odd numbers")
        else:
            print("One is even, One is Odd")
    else:
        print("\nInvalid operators, try 1 + 1")
