import turtle,math
tobj=turtle.Turtle()

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
	#turtle.done()
	

def petal(t,r,angle):
	for i in range(2):
		arc(t,r,angle)
		t.lt(180-angle)

def flower(t,r,npetals,angle):
		for i in range(npetals):
			petal(t,r,angle)
			t.lt(360.0/npetals)
		#turtle.done()

def move(t,length):
	t.pu()
	t.fd(length)
	t.pd()

move(tobj,-100)
flower(tobj,50,7,60)
move(tobj,100)
flower(tobj,40,10,80)
move(tobj,100)
flower(tobj,150,20,20)
turtle.done()
turtle.Mainloop()