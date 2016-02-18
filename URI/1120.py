entrada = raw_input().split()
while(entrada[0]!='0' and entrada[1]!='0'):
	d=entrada[0]
	n =entrada[1]
	n=n.replace(d,"")

	if(len(n)==0 or len(n.replace('0',''))==0 ):
		print 0
	else:
		print int(n)
	entrada = raw_input().split()
