def string_len(string):
    count = 0
    for letters in string:
        count = count + 1
    return count
string = "illinios"

def reverse_string(word):
    reverse_word = ""
    for index in word:
        reverse_word = index + reverse_word
    return reverse_word
word = "Ryan"

def time(minute):
    second = minute * 60
    hour = minute / 60
    return second, hour
minute = 30

def vowel_count(words):
    count = 0
    for letters in words:
        if letters in "aeiou":
            count = count + 1
    return count
words = "hippopotamous"

def prime_number(number):
    if number == 1:
        return False
    num = int (number / 2) + 1
    for count in range(2,num):
        if number % count == 0:
            return False
    return True
number = 213

print("The length of the string is:",string_len(string))
print("The reverse text is:",reverse_string(word))
print("The hours and time is:",time(minute))
print("Vowel found:",vowel_count(words))
print("The prime number is:",prime_number(number))
