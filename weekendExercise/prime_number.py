print("Prime Number")

for numbers in range(1, 101):
    prime_count = 0
    for index in range(1, numbers, +1):
      if numbers % index == 0:
          prime_count = prime_count + 1
    if prime_count == 2:#prime number has 2 divisors
      print(numbers)
print()
