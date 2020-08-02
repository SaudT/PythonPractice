import turtle 
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0


#Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off screen updates helps it go fast


#Snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "up"


#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High Schore: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        time.sleep(.001)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        time.sleep(.001)


def go_left():
    if head.direction != "right":
        head.direction = "left"
        time.sleep(.001)


def go_right():
    if head.direction != "left":
        head.direction = "right"
        time.sleep(.001)


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop
while True:
    wn.update()

#check for collision with border
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))

        head.goto(0,0)
        head.direction = "stop"

    #Hide segments
        for segment in segments:
            segment.goto(1000,1000)

    #Clear the segment list
        segments.clear()

#check to see if collide into itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))

            head.goto(0,0)
            head.direction = "stop"

            #Hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #Clear the segment list
            segments.clear()



#check for collision with food
    if head.distance(food) < 20:
        #Move food to random spot on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        
        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        #Shorten the delay
        delay -= 0.001

        #Increase Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))

    #Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1): #len -1 = the length of array, 0 = go down to 0 exclusive, -1 at the end means decrement by 1
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 (first one after 0)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    


    move()
    time.sleep(delay)

wn.mainloop()  



