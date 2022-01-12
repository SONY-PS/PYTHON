import math
a = float(input("Enter a\n"))
b = float(input("Enter b\n"))
c = float(input("Enter c\n"))
s=(a+b+c)/2
x=(s*(s-a)*(s-b)*(s-c))
area=math.sqrt(x)
print("the area is",area)