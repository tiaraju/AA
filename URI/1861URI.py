dic= {}
deads =set()
while(True):
	try:
		line = raw_input().split()
		if line[0] in dic:
			dic[line[0]]+=1
		else:
			dic[line[0]]=1
			
		deads.add(line[1])

	except EOFError:
		print("HALL OF MURDERERS")
		result = dic.keys()
		result.sort()
		for name in result:
			if name not in deads:
				print("%s %d"%(name,dic[name]))
		break
