# 1. Ask for user weight
print("=" * 70)
print("B M I Weight Calculator")
print("=" * 70)

weight = float(input("\nEnter Weight: "))
height = float(input("Enter Height: "))

result = weight / (height * height)

if result >= 30:
    print("\nWEIGHT : OBESE!")
elif result >= 25 and result <= 29.9:
    print("\nWEIGHT : OVER WEIGHT!!")
elif result >= 18.5 and result <= 24.9:
    print("\nWEIGHT : NORMAL")
else:
    print("\n WEIGHT : UNDER WEIGHT!!!")
