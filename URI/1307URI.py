
def gdc(x,y):
	while y:
		x,y=y,x%y
	return x

n = int(raw_input())

for i in range(n):
	num1 = int(raw_input(),2)
	num2 = int(raw_input(),2)

	if gdc(num1,num2) ==1:
		print "Pair #%d: Love is not all you need!" %(i+1)
	else:
		print "Pair #%d: All you need is love!"%(i+1)