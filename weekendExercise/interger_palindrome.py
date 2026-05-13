print("=" * 50)

word = 11111111

#word = str(input("Enter Word You Want To Reverse: "))
word_str = str(word)
print()

print("=" * 50)

reversed_word = ""

for numbers in word_str:

    reversed_word = numbers + reversed_word

if word_str == reversed_word:
    print(">> It is a palindrome")
else:
    print(">> It is not a palindrome")

#print("\nReversed letter: ",reversed_word, end=" ")
