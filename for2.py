tup = (10, 20, -15, 2.5, "hayat", False)

found = False
for t in tup:
    if t == 2.5:
        found = True
        break
    print(t)
print("**************************")
for t in tup:
    if t == -15:
        continue
    print(t)

print("**************************")

if found:
    print("Founded")
else:
    print("Not Founded")










