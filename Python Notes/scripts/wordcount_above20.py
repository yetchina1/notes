def wordcount_above20():
	fin = open('words.txt')
	for row in fin:
		word = row.strip()
		if len(word)>=20:
			print word


def has_no_e():
	fin=open('words.txt')
	line_count=0
	e_line_count=0
	for line in fin:
		line_count+=1
		#print line_count
		line.strip()
		if 'e' not in line:
			e_line_count+=1
			print line
			
	percent_e_line=int(e_line_count*100/line_count)
	print 'percent_e_line: ' , percent_e_line,'%'	

	
def avoids():
	fin = open('words.txt')
	chars=raw_input('enter string of characters which should not be in the word: ')
	count =0
	flag=False
	for word in fin:
		word=word.strip()
		#print word
		for ch in chars:
			if ch not in word:
				flag=True
			else:
				flag=False
				break
		if flag:
			count+=1
		
	print 'Total # of words in which the', chars, ' was not present  is: ', count
	
def use_all():
	fin=open('words.txt')
	chars=raw_input('enter a sting of characters that uses all of these chars in the word')
	count=0
	flag=False
	for word in fin:
		for ch in chars:
			if ch in word:
				flag=True
			else:
				flag=False
		if flag:
			count+=1
	print 'Total # of words in which the', chars, ' were present  is: ', count


def is_abcderian():
	fin = open('words.txt')
	count=0
	for word in fin:
		word = word.lower()
		i=0	
		flag=False
		length=len(word)
		while i < length-1:
			if word[i]<=word[i+1]:
				flag=True
			i+=1
		#print flag
		if not flag:
			count+=1
	return count
				
			
		
		
	
	
	
	
	
		
	
	
		