def prime_number(number):
    if number == 1:
        return False
    num = int (number / 2) + 1
    for count in range(2,num):
        if number % count == 0:
            return False
        return True
number = 15

print("Prime number is:",prime_number(number))
