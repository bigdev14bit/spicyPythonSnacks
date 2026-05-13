firstInput = int(input("Enter X Number: "))
secondInput = int(input("Enter Y Number: "))

if firstInput > 0 and secondInput > 0:
    print("\nQ1!")
elif firstInput < 0 and secondInput > 0:
    print("\nQ2!")
elif firstInput < 0 and secondInput < 0:
    print("\nQ3!")
elif firstInput > 0 and secondInput < 0:
    print("\nQ4!")
elif firstInput == 0 and secondInput == 0:
    print("\nO R I G I N A L")
elif firstInput != 0 and secondInput == 0:
    print(" \nX------A.X.I.S ")
elif firstInput == 0 and secondInput != 0:
    print(" \nY------A.X.I.S ")
else:
    print("\nInvalid Inputs")
