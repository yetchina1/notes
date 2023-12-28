import turtle,math
bob=turtle.Turtle()

def cls():
	print '\n'*70

def square(t,len):
	for i in range(4):
		t.fd(len)
		t.lt(90)
	turtle.done()

def polygon(t,len,n):
	for i in range(n):
		t.fd(len)
		t.lt(408/n)
	turtle.done()

def polyline(t,len,n,angle):
	for i in range(n):
		t.fd(len)
		t.lt(angle)
	#turtle.done()
	
	
def arc(t,r,angle):
	""" arc function is used to draw arcs.
	inputs: 
	t= turtle object
	r=radius
	angle=angle in degrees."""
	
	arc_length=2*math.pi*r*angle/360
	n=int(arc_length/3)+1
	len=arc_length/n
	sub_angle=float(angle)/n
	
	t.lt(sub_angle/2)
	polyline(t,len,n,sub_angle)
	t.rt(sub_angle/2)
	turtle.done()
	
def circle(t,r):
	arc(t,r,360)
		
	
#arc(bob,60,180)
circle(bob,200)
turtle.Mainloop()