import turtle

def draw_square(mangla):
	side = 4
	while side:
		mangla.forward(100)
		mangla.right(90)
		side  = side - 1
def draw_h(t):
	t.penup()
	t.sety(250)
	t.setx(-280)
	t.pendown()
	t.right(90)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(40)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(40)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(40)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(40)
	t.left(90)
	t.forward(20)
def draw_a(t):
	t.penup()
	t.sety(250)
	t.setx(-140)
	t.pendown()
	t.left(70)
	t.forward(110)
	t.right(180+70)
	t.forward(20)
	t.left(70)
	t.forward(50)
	t.right(70)
	t.forward(30)
	t.right(70)
	t.forward(50)
	t.left(70)
	t.forward(20)
	t.right(180+70)
	t.forward(120)
	t.right(70)
	t.forward(20)	
def draw_circle():
	mangla = turtle.Turtle()
	mangla.shape("turtle")
	mangla.color("yellow")
	mangla.circle(100)
def draw_triangle():
	mangla = turtle.Turtle()
	mangla.shape("turtle")
	mangla.color("green")
	side = 3
	while side:
		mangla.forward(100)
		mangla.right(120)
		side  = side - 1
def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")
	mangla = turtle.Turtle()
	mangla.shape("turtle")
	mangla.color("blue")
	for i in range(1,37):
		draw_square(mangla)
		mangla.right(10)
	# draw_square(mangla)
	window.exitonclick()
mangla = turtle.Turtle()
mangla.shape("turtle")
mangla.color("blue")
#turtle.write("messi fan", font=("Arial", 160, "normal"))
draw_h(mangla)
draw_a(mangla)
draw_h(mangla)																																																																																																																																																																																																																																																																								
