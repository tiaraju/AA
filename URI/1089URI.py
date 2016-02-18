d = int(raw_input())
while d!= 0:
	try:
		temp = map(int,raw_input().split())
		values =[]
		picks =0
		values.append(temp[-1])
		for i in temp:
			values.append(i)
		values.append(temp[0])

		for i in range(1,(len(values)-1)):
			if((values[i] < values[i-1] and values[i] < values[i+1]) or (values[i] > values[i-1] and values[i] > values[i+1])):
				picks += 1

		print picks
		d = int(raw_input())
	except EOFError:
		break