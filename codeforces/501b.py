dic = {}
n = int(input())

for i in range(n):
	full_name = input().split()
	if full_name[0] in list(dic.keys()):
		dic[full_name[1]]=dic[full_name[0]]
		del dic[full_name[0]]
	else:
		dic[full_name[1]]=full_name[0]

print(len(dic))
for k,v in dic.items():
	print("%s %s"%(v,k))
