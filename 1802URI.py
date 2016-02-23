p = raw_input().split()
p = [int(x) for x in p]
p.sort()

m = raw_input().split()
m = [int(x) for x in m]
m.sort()

f = raw_input().split()
f = [int(x) for x in f]
f.sort()

q = raw_input().split()
q = [int(x) for x in q]
q.sort()

b = raw_input().split()
b = [int(x) for x in b]
b.sort()

amount = int(raw_input())
total =0

for i in range(amount):
	total+=p[len(p)-1]
	p.remove(p[len(p)-1])

	total+=m[len(m)-1]
	m.remove(m[len(m)-1])

	total+=f[len(f)-1]
	f.remove(f[len(f)-1])

	total+=q[len(q)-1]
	q.remove(q[len(q)-1])

	total+=b[len(b)-1]
	b.remove(b[len(b)-1])
	if(len(p)==0):
		break
print total
