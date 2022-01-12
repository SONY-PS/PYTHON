def bindig(n):
	decval=0
	base=1
	temp=n
	while(temp):
        	lastdig= temp%10
        	temp=int(temp/10)       
        	decval+= lastdig*base
        	base = base*2
		print("the decimal equivalent is",decval)
num=int(input("enter an binary value"))
bindig(num)