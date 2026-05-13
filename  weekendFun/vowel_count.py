letter = input("Enter A Letter: ").lower()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

if len(letter) != 1:
    print(" INVALID INPUT !! ")
elif letter in vowels:
    print(" V.O.W.E.L ")
elif letter in consonants:
    print(" C.O.N.S.O.N.A.N.T ")
else:
    print(" INVALID INPUT ")
