# student = []
# classes = []
print("These are the choices you can enter:")
print("1- add class")
print("2- add student to class")
print("3- print the whole school")
print("4- print specific student")
print("5- exit")
school = {}
while True:
    print("Please input your choice:")
    choice = input()
    if choice == "1":
        cls = input("Enter new class name: \n")
        school[cls] = []
        # classes.append(cls)
    elif choice == "2":
        cls = input("Enter exist class name: \n")
        std = input("Enter new student name: \n")
        school[cls].append(std)
        # student.append(std)
    elif choice == "3":
        print(school)
        # print("All students are: ", student)
        # print("All classes are: ", classes)
    elif choice == "4":
        print("Enter your class name:")
        student = school[cls]
        if len(student) == 0:
            print("You dont have any students")
            continue
        print("Your index range from 0 to " + str(len(student)-1))
        index = int(input("Enter student index\n"))
        print(student[index])
    elif choice == "5":
        break
    else:
        print("Invalid Input")
        continue
    print("Thank you")
print("Program End")
