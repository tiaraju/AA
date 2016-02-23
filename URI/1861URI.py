dic= {}
murderers=set()
deads =set()
while(True):
	try:
		line = raw_input().split()
		if(len(line)>1):
			if line[0] in dic.keys():
				dic[line[0]]+=1
			else:
				dic[line[0]]=1
			
			murderers.add(line[0])
			deads.add(line[1])

	except EOFError:
		print("HALL OF MURDERERS")
		lista = list(murderers-deads)
		lista.sort()
		for name in lista:
			print("%s %d"%(name,dic[name]))
		break
