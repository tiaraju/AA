n = int(input())
while n!=0:
	lista= {}
	for i in range(n):
		line1 = input()
		line2=input().split()

		if line2[0] in lista:
			if  line2[1] in lista[line2[0]] :
				lista[line2[0]][line2[1]].append(line1)
			else:
				lista[line2[0]]=dict({line2[1]:[]})
				lista[line2[0]][line2[1]].append(line1)
		else:
			lista[line2[0]]=dict({line2[1]:[]})
			lista[line2[0]][line2[1]].append(line1)

		print(lista[line2[0]])
	print(lista)
	n=int(input())


