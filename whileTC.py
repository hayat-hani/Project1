r = 0
while True:
    try:
        r = int(input("enter the redis"))
        break
    except:
        print("enter right value")

print(r)