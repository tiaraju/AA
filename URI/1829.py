import math
n = int(raw_input())
rodadas=[]
pedro = 0
lucas = 0
for i in range(n):
	exp1 = raw_input().split('^')
	exp2=raw_input()[:-1]

	first = int(exp1[1]) * math.log10(int(exp1[0]))
	second =1
	for k in range(1,int(exp2)+1):
		second+=math.log10(k)

	if first > second:
		rodadas.append(0)
		lucas+=1
	else:
		pedro+=1
		rodadas.append(1)
if lucas>pedro:
	print("Campeao: Lucas!")
elif pedro> lucas:
	print("Campeao: Pedro!")
else:
	print("A competicao terminou empatada!")

for i in range(len(rodadas)):
	if(rodadas[i] == 0):
		print 'Rodada #%d: Lucas foi o vencedor' %(i+1)
	else:
		print 'Rodada #%d: Pedro foi o vencedor' %(i+1)