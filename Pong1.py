import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600) #(0,0) is in the center
wn.tracer(0)  #stops window from updating so we can manually update it


#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()   #small t is module name Big T is class name
paddle_a.speed(0) #speed of animation not speed of paddle, 0 is maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()   #small t is module name Big T is class name
paddle_b.speed(0) #speed of animation not speed of paddle, 0 is maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()   #small t is module name Big T is class name
ball.speed(0) #speed of animation not speed of paddle, 0 is maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = .3
ball.dy = .3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B 0", align = "center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
	y = paddle_a.ycor() #finds current y oordinate of paddle_a
	y += 20 
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor() #finds current y oordinate of paddle_a
	y -= 20 
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor() #finds current y oordinate of paddle_a
	y += 20 
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor() #finds current y oordinate of paddle_a
	y -= 20 
	paddle_b.sety(y)

#Keyboard binding
wn.listen()   #listens for a keyboard input
wn.onkeypress(paddle_a_up, "w")  #when w is pressed call paddle_a_up
wn.onkeypress(paddle_a_down, "s")  #when s is pressed call paddle_a_down
wn.onkeypress(paddle_b_up, "Up")  #when up arrow is pressed call paddle_b_up
wn.onkeypress(paddle_b_down, "Down") #when down arrow is pressed call paddle_b_down


#Main game loop

while True:
	wn.update() #updates screen everytime this loop runs
	
	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1

		pen.clear()
		pen.write("Player A: {}  Player B {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball. goto(0,0)
		ball.dx *= -1
		score_b += 1

		pen.clear()	
		pen.write("Player A: {}  Player B {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))



	#paddle and ball collision

	if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx *=  -1

