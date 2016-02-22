while(True):
	try:
		exp = input()
		control =0
		for i in exp:
			if(i=='('):
				control+=1
			elif(i==')'):
				control-=1
			if(control == -1):
				break
		if control ==0:
			print("correct")
		else:
			print("incorrect")
	except EOFError:
		break
