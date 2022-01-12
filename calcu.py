a = float(input("Enter a\n"))
b = float(input("Enter b\n"))
ch=int(input("select \n1.add/n2.sub\n3.mul\n4.div\n5.mod"))
if(ch==1):
	print("sum is",a+b)
elif(ch==2):
	print("difference is",a-b)
elif(ch==3):
	print("product is",a*b)
elif(ch==4):
	print("quotient is",a/b)
elif(ch==5):
	print("remainder is",a%b)
else:
	print("Invalid function")
