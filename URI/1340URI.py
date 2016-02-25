while True:
	try:
		queue = []
		p_queue= []
		stack = []

		is_queue= True
		is_p_queue=True
		is_stack = True

		n = int(input())
		for i in range(n):
			a,b=input().split()
			if int(a)==1:
				queue.append(int(b))
				p_queue.append(int(b))
				p_queue.sort()
				stack.append(int(b))
			else:
				if queue.pop(0) != int(b):
					is_queue = False
				if p_queue.pop() != int(b):
					is_p_queue = False
				if stack.pop() != int(b):
					is_stack = False
	
		if is_queue:
			if is_stack or is_p_queue:
				print("not sure")
			else:
				print("queue")
		elif is_stack:
			if is_queue or is_p_queue:
				print("not sure")
			else:
				print("stack")
		elif is_p_queue:
			if is_queue or is_stack:
				print("not sure")
			else:
				print("priority queue")
		else:
			print("impossible")

	except EOFError:
		break
