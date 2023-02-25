print("These are the choices you can enter:")
print("1- add students")
print("2- print students")
print("3- print single student")
print("4- exit")
students = []

while True:
    print("Please input your choice:")
    choice = input()
    if choice == "1":
        std = input("Enter new student name: \n")
        students.append(std)
    elif choice == "2":
        print(students)
    elif choice == "3":
        if len(students) == 0:
            print("You dont have any students")
            continue
        print("Your index range from 0 to " + str(len(students)-1))
        index = int(input("Enter student index\n"))
        print(students[index])
    elif choice == "4":
        break
    else:
        print("Invalid Input")
        continue
    print("Thank you")
print("Program End")

