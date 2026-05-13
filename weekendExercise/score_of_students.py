pass_Score = 0
fail_Score = 0

for index in range(1, 16):
    userInput = int(input("Enter Score: "))

if userInput > 45:
    pass_Score = pass_Score + 1
elif userInput < 45:
    fail_Score = fail_Score + 1

print("\n" + "=" * 70)
print("Pass :",pass_Score)
print("Fail :",fail_Score)
print("=" * 70)
