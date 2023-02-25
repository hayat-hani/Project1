students = []
i = 1
while len(students) < 5:
    std = input("Please input student number "
                + str(i) + "\n")
    i = i + 1
    students.append(std)
    # if len(students) >= 5:
    #     break

print(students)
