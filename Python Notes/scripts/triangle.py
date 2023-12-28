import turtle,math
def triangle(t,len,len_side,angle):
	t.fd(len)
	t.lt(angle)
	t.fd(len_side)
	t.lt(180-angle)
	t.fd(len)
	t.lt(180)


def tri_flower(t,len,num):
	angle1 = 360.0/num
	angle=angle1
	len_side=2*math.pi/num
	for i in range(num):
		triangle(t,len,len_side,angle)
		angle=angle+angle1

t=turtle.Turtle()
tri_flower(t,50,7)
turtle.done()
turtle.Mainloop()