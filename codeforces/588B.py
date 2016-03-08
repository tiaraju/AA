def is_lovely(num,divisors):
	for i in divisors:
		if num%(i**2) == 0:
			return False
	return True

def get_divisors(num):
	divisors=[]
	for i in range(2,num):
		if num%i==0:
			divisors.append(i)	
	return divisors

n = int(input())
divisores = get_divisors(n)
main_divisors=divisores
index =1

while not is_lovely(n,divisores):
	n=main_divisors[(len(main_divisors)-index)]
	divisores=get_divisors(n)
	index+=1

print(n)
