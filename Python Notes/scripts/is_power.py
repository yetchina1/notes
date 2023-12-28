def is_power(a,b):
	if a%b !=0:
		return False
	if a == b:
		return True
	return(is_power(int(a/b),b))