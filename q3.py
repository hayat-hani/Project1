n1 = 0
n2 = 1
count = 0
nTerms = int(input("Enter index n  to calculate the fibonacci sequence:"))
if nTerms <= 0:
    print("You should enter positive number")
elif nTerms == 1:
    print("Fibonacci sequence for index ", nTerms, ":")
    print(n1)
else:
    while count < nTerms:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count = count + 1
