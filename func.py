# def print_welcome():
#     print("welcome")
#     print("hello")
#
#
# print_welcome()
#
#
# def printYourInfo(name, age, year):
#     # = input("Enter your name: ")
#     # = input("Enter your age: ")
#     # = input("Enter your university year: ")
#     print("Your Name: ", name)
#     print("Your age: ", age)
#     print("Your university year: ", year)
#     print("*****************************************")
#
#
# printYourInfo("hayat", 20, "second")
# printYourInfo("sara", 22, "fourth")


def calculate_area(r):
    area = r ** 2 * 3.14
    return area


r1 = int(input("Enter r1\n"))
r2 = int(input("Enter r2\n"))
area1 = calculate_area(r1)
area2 = calculate_area(r2)

if area1 > area2:
    print("circle 1 is bigger")
elif area2 > area1:
    print("circle 2 is bigger")
else:
    print("circles are equal")