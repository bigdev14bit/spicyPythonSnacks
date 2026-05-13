print("=" * 50)
word = input("Enter Word You Want To Reverse: ")
print("=" * 50)

count = " "

for words in word:

    count = words + count

print("\nReversed letter: ",count, end=" ")
print()
