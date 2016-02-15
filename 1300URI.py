while True:
	try:
		answer ='Y' if int(raw_input())%6 == 0 else 'N'
		print answer
	except EOFError:
		break
