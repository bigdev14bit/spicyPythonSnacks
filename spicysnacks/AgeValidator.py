#Get input from user
#calculate the target year
#calculate age difference 
#ensure the result is positive.
fatherAge = int(input("Enter Current Father Year: "));
sonAge = int(input("Enter Current Son Age: "));

ageGap = fatherAge - sonAge

yearsDifferents = ageGap - sonAge

if yearsDifferents < 0:
    years = yearsDifferents * -1
else:
    years = yearsDifferents
print(years)

#The Logic: The father is only twice as old as the son when the son's age is equals the difference between them. If the gap is 20 years, the father will be 40 when the son is 20.
