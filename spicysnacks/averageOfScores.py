firstScore = int(input("Enter First Score: "));
secondScore = int(input("Enter Second Score: "));
thirdScore = int(input("Enter Third Score: "));

averageScore = (firstScore + secondScore + thirdScore) / 3

if averageScore >= 90:
    grade = 'A'
elif averageScore >= 80:
    grade = 'B'
elif averageScore >= 70:
    grade = 'C'
elif averageScore >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\nLetter Grade: ",grade);
print("Score Grade: ",averageScore);
