# -*- coding: utf-8 -*-
 
n = int(raw_input())
coef = []
coefAngA, coefAngB = 0, 0
hittable = True
 
for i in range(n+1):
	parede = map(int, raw_input().split())
	distancia = parede[0]
	alturaA = parede[1]
	alturaB = parede[2]
	coefAngA = (float(alturaA))/distancia
	coefAngB = (float(alturaB))/distancia
	coef.append([coefAngA, coefAngB])
 

for i in range(1, len(coef)):
	if (coef[i][0] > coef[i-1][1]) or (coef[i][1] < coef[i-1][0]):
		hittable = False
		break
	else:
		if (coef[i][0] < coef[i-1][0]):
			coef[i][0] = coef[i-1][0]
		if (coef[i][1] > coef[i-1][1]):
			coef[i][1] = coef[i-1][1]
 
if hittable:
	print "Y"
else:
	print "N"