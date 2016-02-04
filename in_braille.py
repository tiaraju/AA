number_to_braille = {0:".*\n**\n..",1:"*.\n..\n..",2:"*.\n*.\n..",3:"**\n..\n..",4:"**\n.*\n..",5:"*.\n.*\n..",6:"**\n*.\n..",7:"**\n**\n..",8:"*.\n**\n..",9:".*\n*.\n.."}

braille_to_number = {".*\n**\n..":0,"*.\n..\n..":1,"*.\n*.\n..":2,"**\n..\n..":3,"**\n.*\n..":4,"*.\n.*\n..":5,"**\n*.\n..":6,"**\n**\n..":7,"*.\n**\n..":8,".*\n*.\n..":9}



d = int(raw_input())
while(d != 0):
	l = raw_input()
	if(l=="S"):
		number = int(raw_input())
		result =""
		for i in str(number):
			result+=number_to_braille[int(i)]
		print(result)
	else:
		print("TODO")

	d = int(raw_input())





