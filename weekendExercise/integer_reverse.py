print("=" * 50)
word = str(input("Enter Word You Want To Reverse: "))
word_str = str(word)
print("=" * 50)

count = " "

for numbers in word_str:

    count = numbers + count

print("\nReversed letter: ",count, end=" ")
print()
