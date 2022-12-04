import turtle
import numpy as np
import time


def main(speed=0, bg_color="grey"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    myTurtle.speed(speed)
    # change background color
    turtle_screen.bgcolor(bg_color)
  
 
    """TODO: define different colors here"""
    My_color = ['blue' , 'red' ,'orange' , 'white' ,'yellow', 'pink']


    for _ in range(len(My_color)):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]
        r_color = np.random.randint(0,5)

        """TODO: set snowflake color here (one of the colors defined above)"""
        myTurtle.color(My_color[r_color])
        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()

        # draw the snowflake
        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)


def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
    time.sleep(15)

