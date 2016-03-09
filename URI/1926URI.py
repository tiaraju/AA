import math
query = int(input())

for i in range(query):
	a,b=input().split()
	a = int(a)
	b=int(b)

	num = []
	
	if a>b:
		temp=a
		a=b
		b=temp

	primes = [True]*(b+2)
	primes[0]=False
	primes[1]=False
	m = int(math.sqrt(b))
	for k in range(2,b+2):
		if primes[k]:
			num.append(k)
			for j in range(k*k,(b+1),k):
				primes[j]= False

	counter = 0

	for k in range(len(num)):
		if(num[k]>=a and num[k]<b):
			if(k-2)>=0:
				if (num[k]-2) in num:
					counter+=1
					continue
			if(k+2)<=b+1:
				if (num[k]+2) in num:
					counter+=1

	print(counter)
	