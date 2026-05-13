#print("  D.I.V.I.S.O.R--OF--A--N.U.M.B.E.R  ")

#for numbers in range(1, 101):
    #print("Divisor of:",numbers)

    #for index in range(1, numbers, +1):
      #  if numbers % index == 0:
     #       print(index)
    #print()

print("  D.I.V.I.S.O.R--OF--A--N.U.M.B.E.R  ")

for numbers in range(1, 101):
    print("Divisors of:",numbers,end="")
    
    for index in range(1, numbers + 1): 
        if numbers % index == 0:
    
            print(index, end=" ") 
            
    print() 
