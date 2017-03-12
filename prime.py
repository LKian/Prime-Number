usernum = input("Enter a number and we'll determine if it's a prime number: \n")

x = []
for i in range(2,usernum):
	if usernum%i==0:	
		x.append(i)
if len(x)==0:
	print usernum, "is a prime number."
else:
	for i in x:
		print usernum, "is divisible by", i