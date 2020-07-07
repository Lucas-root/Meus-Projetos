import turtle 

qazi_turtle = turtle.Turtle()
controle = 0

while True:
	controle += 1
	qazi_turtle.right(1)
	qazi_turtle.forward(1)
	if controle == 359:
		break
turtle.done()

