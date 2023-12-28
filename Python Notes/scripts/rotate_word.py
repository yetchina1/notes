def rotate_word(word,n):
	new_str=''
	excess=0
	if n>26:
		n=n%26
	for c in word:
		#print c
		if c.islower():
			if (ord(c)+n <=122):
				new_str+=chr(ord(c)+n)
			else:
				excess=ord(c)+n-122
				new_str+=chr(97+excess-1)
		
		elif c.isupper():
			if (ord(c)+n <= 90):
				new_str+=chr(ord(c)+n)
				#print new_str
			else:
				excess=ord(c)+n-90
				new_str+=chr(65+excess-1)
	return new_str
		