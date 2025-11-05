import turtle
t = turtle.Turtle()

#I did a light background, but people said with a darker background they can see the pink better so I changed it
t.screen.bgcolor("blue")
t.color ("cyan")
t.speed(10)

for i in range (100):
    t.forward (150 + i)
    t.left (120)
#Changing color 

t.color ("gold")
t.speed(10)

for i in range (90):
    t.forward (150 + i)
    t.right (120)

t.color ("green")
t.speed(10)

for i in range (80):
    t.forward (150 + i)
    t.right (131)
t.penup()
t.goto(-100, 100)
t.pendown()
t.color ("crimson")
t.speed(10)

for i in range (85):
    t.forward (90 + i)
    t.left (131 +1)
#This is what makes my pink big hexagon


t.color ("pink")
t.speed(10)

for i in range (100):
    t.forward (122 + i)
    t.left (60)

turtle.exitonclick()