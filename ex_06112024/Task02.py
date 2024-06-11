#Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
num = 2
square = num**2
cube = num**3
print(square)
print(cube)



x = input("Enter the first number\t")
y = input("Enter the first number\t")
x = int(x)
y = int(y)
if x > y:
    print("x is greater than y")
    print(x)
elif x < y :
    print("y is greater than x")
    print(f"{y} is greater than {x}")
    print(y)
else:
    print("x and y are equal")