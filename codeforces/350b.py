n = int(raw_input())
objects = raw_input().split()
path = raw_input().split()
hotels=[]
tracks = {}
maximum_path=[]
exists = list([x for x in path if path.count(x)>1])

for i in range(len(path)):
	if(path[i]==0):
		continue
	else:
		if(not tracks.has_key(i+1)):
			if(not path[i] in exists):
				tracks.setdefault(i+1,[]).append(path[i])
			else:
				tracks.setdefault(i+1,[])

for i in range(len(objects)):
	if(objects[i]=='1'):
		hotels.append(i+1)

for i in hotels:
	temp=[]
	temp.append(i)
	if(i in tracks and len(tracks[i])>0): 
		next_node = tracks[i][0]
		while(tracks.has_key(int(next_node))):
			temp.append(int(next_node))
			if len(tracks[int(next_node)]) >0:
				next_node=tracks[int(next_node)][0]
			else:
				break
	if(len(temp)> len(maximum_path)):
		maximum_path = temp

resp = ""
for i in maximum_path[::-1]:
	resp+=("%s " %i)
print len(maximum_path)
print resp




