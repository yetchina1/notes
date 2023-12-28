def count(word,letter):
	i=0
	count=0
	while(i<len(word)):
		#print i
		if word[i]==letter:
			count=count+1
		i=i+1
	return count