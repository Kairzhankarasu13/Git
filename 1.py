# print("Git Git")

print("введите арифметическую операцию через пробел")

print()

a,b,c = input().split()
a = int(a)
b = str(b)
c = int(c)

if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a*c)
elif b == "/":
    print(a/c)