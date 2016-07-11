import turtle

def draw_square(mangla):
	side = 4
	while side:
		mangla.forward(100)
		mangla.right(90)
		side  = side - 1
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
draw_shapes()	