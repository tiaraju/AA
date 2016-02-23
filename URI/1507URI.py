def issubstr(substr, mystr, start_index=0):
    try:
        for letter in substr:
            start_index = mystr.index(letter, start_index) + 1
        return True
    except: return False

n = int(input())
for i in range(n):
	word = input()
	q = int(input())
	for k in range(q):
		query_word= input()
		if issubstr(query_word,word):
			print("Yes")
		else:
			print("No")
