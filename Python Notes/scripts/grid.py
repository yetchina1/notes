def plus_line():
	print '+','- '*5,'+ ','- '*5,'+'

def vert_line():
	#print
	print '|','  '*5,'| ','  '*5,'|'

def print_row():
	plus_line()
	do_four(vert_line)
	
def do_four(fn):
	fn()
	fn()
	fn()
	fn()


def print_grid():
	do_four(print_row)
	plus_line()
	
print_grid()