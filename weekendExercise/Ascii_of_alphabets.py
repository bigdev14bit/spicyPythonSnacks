print("=" * 70)
print("=" * 70)
print("Enter A Character To Check The Ascii Value")

while True:
  userInput = input("\nEnter A Character: ")
  if userInput == "quit":
      print("\nTERMINATED")
      break

  ascii_value = ord(userInput)

  print("\nThe Ascii Value of: ",userInput," = ",ascii_value)

print("=" * 70)
print("=" * 70)
