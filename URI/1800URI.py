dic = {}

read = raw_input().split()
two_days = int(read [1])
last_week= int(read [0])


visited_offices=raw_input().split()

for i in range(len(visited_offices)):
	if(dic.has_key(visited_offices[i])):
		dic[visited_offices[i]]+=1
	else:
		dic[visited_offices[i]]=1

for i in range(last_week):
	c = raw_input()
	if(dic.has_key(c)):
		print 0
	else:
		dic[c]=1
		print 1
