print("  D.I.V.I.S.O.R--C.O.U.N.T--OF--A--N.U.M.B.E.R  ")

for numbers in range(1, 101):
    divisor_count = 0

    #print("Divisors of:",numbers,end="")

    for index in range(1, numbers + 1):
        if numbers % index == 0:
          divisor_count = divisor_count + 1
    print("Divisors of:",numbers," is ",divisor_count)
            #print(index, end=" ")
