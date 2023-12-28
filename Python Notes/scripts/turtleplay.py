import turtle,math
def play_turtle():
	t1=turtle.Turtle()
	#print t1
	t1.fd(50)
	t1.lt(180-36)
	t1.fd(math.sqrt(2))
	t1.lt(180-2*36)
	t1.fd(50)
	

play_turtle()
turtle.done()

turtle.Mainloop()