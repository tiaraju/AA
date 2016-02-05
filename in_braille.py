first_number_to_braille = {0:". *",1:"* .",2:"* .",3:"* *",4:"* *",5:"* .",6:"* *",7:"* *",8:"* .",9:". *"}
second_number_to_braille = {0:"* *",1:". .",2:"* .",3:". .",4:". *",5:". *",6:"* .",7:"* *",8:"* *",9:"* ."}

braille_to_number = {".***..":0,"*.....":1,"*.*...":2,"**....":3,"**.*..":4,"*..*..":5,"***...":6,"****..":7,"*.**..":8,".**...":9}

word=[]


d = int(raw_input())
while(d != 0):
	l = raw_input()
	result =""
	if(l=="S"):
		number = int(raw_input())
		for i in str(number):
			result+=(first_number_to_braille[int(i)])
			if(i < len(str(number))-1):
				result+=" "
		result+="\n"

		for i in str(number):
			result+=(second_number_to_braille[int(i)])
			if(i < len(str(number))-1):
				result+=" "
		result+="\n"

		for i in str(number):
			result+=". ."
			if(i < len(str(number))-1):
				result+=" "

	else:
		digit = ""
		for i in range(3):
			j=i
			line = raw_input().split()
			for k in range(len(line)):
				word.insert(j,line[k])
				j+=3

		for i in range(len(word)):
			if(i%3 == 0 and i!=0):
				result+=str(braille_to_number.get(digit))
				digit=word[i]
			else:
				digit+=word[i]

	print result
	d = int(raw_input())





