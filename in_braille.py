first_number_to_braille = {0:".*",1:"*.",2:"*.",3:"**",4:"**",5:"*.",6:"**",7:"**",8:"*.",9:".*"}
second_number_to_braille = {0:"**",1:"..",2:"*.",3:"..",4:".*",5:".*",6:"*.",7:"**",8:"**",9:"*."}

braille_to_number = {".***..":0,"*.....":1,"*.*...":2,"**....":3,"**.*..":4,"*..*..":5,"***...":6,"****..":7,"*.**..":8,".**...":9}

word={}


d = int(raw_input())
while(d != 0):
	l = raw_input()
	result =""
	if(l=="S"):
		number = int(raw_input())
		for i in str(number):
			result+=(first_number_to_braille[int(i)])
			if(int(i) < len(str(number))):
				result+=" "
		if(result[len(result)-1]==" "):
			result=result[:len(result)-1]
		result+="\n"

		for i in str(number):
			result+=(second_number_to_braille[int(i)])
			if(int(i) < len(str(number))):
				result+=" "
		if(result[len(result)-1]==" "):
			result=result[:len(result)-1]
		result+="\n"

		for i in str(number):
			result+=".."
			if(int(i) < len(str(number))):
				result+=" "
		if(result[len(result)-1]==" "):
			result=result[:len(result)-1]

	else:
		digit = ""
		for i in range(3):
			j=0
			line = raw_input().split()
			for k in range(len(line)):
				if(word.has_key(j)):
					word[j] = word[j]+line[k]
				else:
					word[j] = line[k]
				j+=3

		for i in word.keys():
			result+=str(braille_to_number.get(word[i]))
	if(result.isdigit()):
		print int(result)
	else:
		print result
	d = int(raw_input())





