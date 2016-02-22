def binary_search(inicio,fim,lista,element):
	meio = int((inicio+fim)/2)
	if lista[meio] == element:
		while( meio >0 and lista[meio-1]==element):
			meio-=1
		return meio
	elif (fim-inicio) <= 1:
		return -1
	else:
		if element>lista[meio]:
			return binary_search(meio,fim,lista,element)
		else:
			return binary_search(inicio,meio,lista,element)


nq = input().split()
n=int(nq[0])
q=int(nq[1])
case =1

while(n!= 0 and q !=0):

	lista = []
	for i in range(n):
		lista.append(int(input()))

	lista.sort()
	print("CASE# %d:"%(case))
	for i in range(q):
		element=int(input())
		index = binary_search(0,(len(lista)),lista,element)
		if(index != -1):
			print("%d found at %d"%(element,index+1))
		else:
			print("%d not found"%element)
	case+=1

	nq = input().split()
	n=int(nq[0])
	q=int(nq[1])



