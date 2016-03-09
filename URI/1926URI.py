import math
query = int(raw_input())

primes = [True]*1000001
primes[0]=False
primes[1]=False

for k in range(2,1000):
	if primes[k]:
		for j in range(k*k,1000001,k):
			primes[j]= False

soma = [0]*1000001
for k in range(3,1000001):
	if((primes[k] and primes[k-2]) or(primes[k] and primes[k+2])):
		soma[k]=soma[k-1]+1
	else:
		soma[k]=soma[k-1]

for i in range(query):
	a,b=map(int,raw_input().split())
	
	if a>b:
		temp=a
		a=b
		b=temp
	
	print(soma[b]-soma[a-1])
	