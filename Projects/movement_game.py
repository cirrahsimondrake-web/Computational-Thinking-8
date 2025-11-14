# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)
obstacles = []
#section 2: Setup
s1 = create_sprite ("Huey",-100,100)
set_background ("trees")
#s2 = create_sprite ("81lsgRgCTTL._AC_SL1500")
# TODO - set the starting value for your variable


# Section 3: Controls
my_character = "Huey"
def change_character():
	global my_character
	set_image(s1,"81lsgRgCTTL._AC_SL1500")
	my_character = "ball"
window.onkeypress (change_character, "q")

def change_character():
	set_image(s2,"Huey")
window.onkeypress (change_character,"w" )

def move_up():
    s1.setheading(90)
    s1.forward(10)
        
def move_down():
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    s1.setheading(180)
    s1.forward(10)
    
def move_right():    
    s1.setheading(0)
    s1.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")

window.listen()
timer = 0
lives = 5
# character part
while True:
	time.sleep(0.01)
	timer += 1  
	window.update()

	if timer == 300:
		s1.color("red")
		s1.write("3", font = ("Arial", 40, "normal"))
	if timer == 400:
		s1.clear()
		s1.write("2", font = ("Arial", 40, "normal"))
	if timer == 500:
		s1.clear()
		s1.write ("1", font = ("Arial", 40, "normal"))
	if timer == 600:
		break
timer = 0
if my_character == "Huey":
	# ball part
	while True:
		time.sleep(0.01)
		timer += 1  
		window.update()

		#TODO - code for automatic actions
		if timer % 10 == 0:
			y_position = random.randint(-250, 250)
			s2 = create_sprite("81lsgRgCTTL._AC_SL1500", 300, y_position)
			s2.setheading(180)
			obstacles.append(s2)

		#Move each dodge ball
		for s2 in obstacles:
			s2.forward(8)

	#if you collide, you die
			if get_distance(s1,s2) < 50:
				lives -= 1
				s2.hideturtle()
				obstacles.remove(s2)

		if lives == 0:
			print("Huey lost!")
			break

elif my_character == "ball":
	while True:
		time.sleep(0.01)
		timer += 1  
		window.update()

		

