n = raw_input();
hexa = False
if len(n)>2:
	if n[1]=='x' or n[1]=='X':
		n=int(n[2:],16)
		hexa = True
	else:
		n=int(n)
else:
	n=int(n)

while n >= 0:
	if hexa:
		print "%d"%n
	else:
		print "0x%X"%n
	n = raw_input()
	hexa = False
	if len(n)>2:
		if n[1]=='x' or n[1]=='X':
			n=int(n[2:],16)
			hexa = True
		else:
			n=int(n)
	else:
		n=int(n)