import cmath
a=int(input("enter a\n"))
b=int(input("enter b\n"))
c=int(input("enter c\n"))
r=(b*b)-(4*a*c)
x1=(-b+cmath.sqrt(r))/(2*a)
x2=(-b-cmath.sqrt(r))/(2*a)
print("the solutions are")
print(x1,x2)
