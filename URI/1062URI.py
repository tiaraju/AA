n = int(input())
while(n != 0):
	line = input().split()
	
	if int(line[0])==0:
		n=int(input())
		print()
		continue

	initial_max_value=n
	max_value = initial_max_value	
	line = line[::-1]
	stack = []
	for number in line:
		if int(number) == max_value:
			max_value-=1
			while len(stack) > 0 and stack[len(stack)-1] == max_value:
				max_value-=1
				stack.pop()
		else:
			stack.append(int(number))

	if len(stack) <= 0:
		print("Yes")
	else:
		print("No")