import math
def mysqrt(a):
	if a !=1:
		estimate=a-1
	else:
		return 1
	
	delta=0.000001
	while True:
		y=(estimate+a/estimate)/2.0
		diff = abs(y-estimate)
		#print 'estimate: ', estimate
		#print 'y: ', y
		#print 'diff: ', diff
		estimate = y
		if diff <= delta:
			break
	return y
	
def test_sqrt():
	#num= raw_input('Enter a number. To quit enter 0: ')
	print 'a','\t mysqrt(a)',
	print '\t math.sqrt(a)','\t diff'
	print '--','\t ---------------','\t ---------------------', '\t' ,'------'
	num=1
	while num <= 9:
		#mysqrt(num)
		print num,'\t', mysqrt(num),'\t', math.sqrt(num),'\t', abs(math.sqrt(num)-mysqrt(num))
		num=num+1
	
		
		
		
	
	
	