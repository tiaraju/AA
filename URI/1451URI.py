while True:
	try:
		word = raw_input()
		result = ''
		aux = ''
		key = 0
		for letter in word:
			if letter == '[':
				if key == 0:
					result = aux + result
				else:
					result+=aux
				aux = ""
				key =0
				
			elif letter ==']':
				if key == 0:
					result = aux + result
				else:
					result+=aux
				aux = ""
				key = 1
			else:
				aux+=letter	
		if key == 0:
			result  = aux+result
		else:
			result+=aux
		
		print result

	except EOFError:
		break