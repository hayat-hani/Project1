while True:
    n = int(input("Enter the first number (the smallest): \n"))
    m = int(input("Enter the second number (the largest): \n"))
    if n < m :
        break
    else:
        print("Invalid numbers!")
sum = 0
for i in range(n, m+1):
    sum = sum + i
print("The summation from n to m = ", sum)



