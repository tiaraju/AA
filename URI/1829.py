import math
n = int(raw_input())
rodadas=""
pedro = 0
lucas = 0
for i in range(n):
	exp1 = raw_input().split('^')
	exp2=raw_input()[:-1]

	first = 1
	second =1

	for k in range(int(exp1[1])):
		first+=math.log10(int(exp1[0]))
	for k in range(1,int(exp2)+1):
		second+=math.log10(k)

	if first > second:
		rodadas+="Rodada #%d: Lucas foi o vencedor\n"%(i+1)
		lucas+=1
	else:
		pedro+=1
		rodadas+="Rodada #%d: Pedro foi o vencedor\n"%(i+1)
if lucas>pedro:
	print("Campeao:Lucas!")
elif pedro> lucas:
	print("Campeao:Pedro!")
else:
	print("A competicao terminou empatada!")
print(rodadas)