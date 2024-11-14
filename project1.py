import turtle   #turtle is a Python module used to create graphics and simple games
import time     #time is a module to work with time-related tasks like introducing delays
import random   #random is a module used to generate random numbers

delay=0.1       # Delay between screen updates

#score
score=0     # Player's current score
high_score=0    # Highest score achieved

# setup screen
wn=turtle.Screen()      # Create a screen object to control the window
wn.title("Snake game")      # Set the title of the game window
wn.bgcolor("Green")     # Set the background color of the window
wn.setup(width=600,height=600)      # Set the size of the window
wn.tracer(0)        #turns of the automatic screen updates to improve performance

# snake head 
head=turtle.Turtle()    # Create a turtle object representing the snake's head
head.speed(0)           # Set the drawing speed
head.shape("square")    # Set the shape of the snake's head to a square
head.color("black")     # Set the color of the head to black
head.penup()            # Prevent drawing lines when moving
head.goto(0,0)          # Position the head at the center of the screen
head.direction="stop"   # Initial direction is "stop"

# snake food 

food=turtle.Turtle()    # Create a turtle object representing the food
food.speed(0)           # Set the drawing speed
food.shape("circle")    # Set the food's shape to a circle
food.color("red")       # Set the food color to red
food.penup()            # Prevent drawing lines
food.goto(0,100)        # Place the food at a random position

segments=[]             # Create an empty list to hold the body segments

pen=turtle.Turtle()     # Create a turtle object to display score
pen.speed(0)            # Set the drawing speed
pen.shape("square")     # Use a square shape for the pen
pen.color("white")      # Set the color to white
pen.penup()             # Prevent drawing lines
pen.hideturtle()        # Hide the pen cursor
pen.goto(0,260)         # Position the score display at the top of the screen


pen.write(f"Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))    #the current score and high score at the top of the screen


# functions
def go_up():            #defining a function to go upward
    if head.direction != "down":
        head.direction = "up"

def go_down():          #defining a function to go downward
    if head.direction != "up":
        head.direction = "down"

def go_left():          #defining a function to go left
    if head.direction != "right":
        head.direction = "left"

def go_right():         #defining a function to go right
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y=head.ycor()       # Get the current y-coordinate
        head.sety(y+20)     # Move the head upwards by 20 units

    if head.direction == "down":
        y=head.ycor()       # Get the current y-coordinate
        head.sety(y-20)     # Move the head downwards by 20 units

    if head.direction == "left":
        x=head.xcor()       # Get the current x-coordinate
        head.setx(x-20)     # Move the head left by 20 units

    if head.direction == "right":
        x=head.xcor()       # Get the current x-coordinate
        head.setx(x+20)     # Move the head right by 20 units


# keyboard buttons set/binding  
wn.listen()                 # Listen for keypress events
wn.onkeypress(go_up,"w")    # Bind the "W" key to the go_up() function
wn.onkeypress(go_down,"s")  # Bind the "S" key to the go_down() function
wn.onkeypress(go_left,"a")  # Bind the "A" key to the go_left() function
wn.onkeypress(go_right,"d") # Bind the "D" key to the go_right() function

# main game loop
while True:
    wn.update()     # Update the screen to reflect changes

    # check collision with border 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(1)   # Pause the game for 1 second
        head.goto(0,0)  # Reset the snake's head position
        head.direction = "stop"     # Stop the movement


        # hide segments 
        for segment in segments:        
            segment.goto(1000,1000)

        # clear the segment list 
        segments.clear()

        # reset the score 
        score=0

        # reset the delay
        delay=0.1

        pen.clear()     # Clear the previous score
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "normal"))

    # check the collision with food 
    if head.distance(food)<20:      # Check if head is near the food
        # movement of food in random spot 
        x=random.randint(-290,290)  # Generate random x-coordinate for new food
        y=random.randint(-290,290)  # Generate random y-coordinate for new food
        food.goto(x,y)              # Move the food to the new position


        # add segment
        new_segment=turtle.Turtle()     
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # shorten delay 
        delay-=0.001

        # increase score 
        score+=10

        # Update high score
        if  score>high_score:
            high_score=score

        pen.clear()     # Clear the old score

        pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    # move end segment in reverse order 

    for index in range(len (segments)-1,0,-1):      
        x=segments[index-1].xcor()                  # Get the previous segment's x-coordinate
        y=segments[index-1].ycor()                  # Get the previous segment's y-coordinate

        segments[index].goto(x,y)                   # Move the current segment to the previous segment's position

        # move segment 0 at where head is 
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
                
    move()      # Move the snake's head

    # check for head collision with the body segments
    for segment in segments:        
        if segment.distance(head)<20:       # If the head is close to any segment
            time.sleep(1)                   # Pause the game for 1 second
            head.goto(0,0)                  # Reset the snake's head position
            head.direction="stop"           # Stop the snake

            # hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # clear the segment list 
            segments.clear()

            # reset the score 
            score=0

            # reset the delay 
            delay=0.1

            # update the score delay 
            pen.clear()

            pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)       # Introduce a delay to control the speed of the game

wn.mainloop()               # Start the Turtle graphics event loop