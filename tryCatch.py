def rase_exception():
    age = int(input("enter your age\n"))
    if age > 120:
        raise Exception("enter correct age")

# rase_exception()
try:
    rase_exception()
except Exception as exp:
    print(exp)
