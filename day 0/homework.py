from turtle import *

#we want to print a house

#step 1:  draw a square
shape("turtle")
width(7)
speed(30)

color("red")

forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square()

forward(70)
color("yellow")
left(90)
begin_fill()
forward (120) #height of the door
right(90)
forward(60)
right(90)
forward(120)

end_fill()


penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
left(30)

forward(30)
left(90)
forward(20)
pendown()
begin_fill()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()
#window
penup()

right(90)
forward(130)
pendown()
begin_fill()
forward (35)
right(90)

forward(35)
right(90)

forward(35)
right(90)

forward(35)
end_fill()





exitonclick()