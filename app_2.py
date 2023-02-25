print("Hello, Please enter your mark:")
mark = int(input())
if mark >= 0 and mark <= 100:
    print("Valid")
    if mark >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid")
print("Thank you")
