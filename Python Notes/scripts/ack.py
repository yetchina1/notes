def ack(m,n):
	if m == 0:
		return n+1
	elif m >0 and n == 0:
		result = ack(m-1,1)
		return result
	elif m > 0 and n > 0:
		result = ack(m-1,ack(m,n-1))
		return result
print ack(3,4)