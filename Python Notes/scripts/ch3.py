def print_twice(s):
	print s
	

def do_twice(f,arg):
	f(arg)
	f(arg)

def do_four(f,arg):
	do_twice(f,arg)
	do_twice(f,arg)

do_four(print_twice,'vivek')
print "shiva"
	
	
