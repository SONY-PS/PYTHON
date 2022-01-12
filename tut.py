n=int(input("enter the limit"))
a=[]
for i in range(0,n):
	a.insert(i,int(input("enter the element")))
for i in range(0,n):
	if(a[i]>a[i+1]):
		temp=a[i]
		a[i]=a[i+1]
		a[i+1]=temp
print()