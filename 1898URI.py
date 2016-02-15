# -*- coding: utf-8 -*-
l=raw_input()
k=raw_input()
ans=""
resp=""

for i in range(len(l)):
	if(l[i].isdigit() or l[i]=='.'):
		ans+=l[i]

for i in range(len(k)):
	if(k[i].isdigit() or k[i]=='.'):
		resp+=k[i]

index_l = ans.find('.')
index_k = resp.find('.')
if(index_l != -1):
	if(len(ans)-index_l > 3):
		ans=ans[:index_l+3]

if(index_k != -1):
	if(len(resp)-index_k > 3):
		resp=resp[:index_k+3]

resp = float(ans[11:])+float(resp)
print("cpf %s"%ans[:11])
print("%.2f"%resp)

