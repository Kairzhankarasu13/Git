# print("Git Git")

# print("введите арифметическую операцию через пробел")

# print()

# a,b,c = input().split()
# a = int(a)
# b = str(b)
# c = int(c)

# if b == "+":
#     print(a+c)
# elif b == "-":
#     print(a-c)
# elif b == "*":
#     print(a*c)
# elif b == "/":
#     print(a/c)


# print("input a")
# print()
# a = int(input())
# print()
# print("input b ")
# print()
# b = int(input())
# print()
# print("input c")
# print()
# c = int(input())
# print()
# d = a + b + c
# print("d =",d)


# a=int(input('a = '))
# b=int(input('b = '))
# (a - (a + 1) % 2, b - b % 2, -2)
# c=((a + 1) % 3)
# print(c)


Q = [1, 'gg', 5, 6, 'gto', 7, 8]
N=[]
W=[]
for i in Q:
    if type(i) == int:
        N.append(i)
        
    elif type(i) == str:
        W.append(i)
print(N)
print(W)