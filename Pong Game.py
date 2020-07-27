# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:29:06 2020

@author: Emmanuel Alejandro Hurtado Alejandre Data 2A
"""
'''Pong Game'''
'''This game is only for 2 Human Players'''

'''Importing turtle Module'''
import turtle

window = turtle.Screen()               # Turtle window
window.title("Pong Game")              # Title of the window
window.bgcolor("black")                # Color of the window
window.setup(width=800, height=600)    # Size of the window
window.tracer(0)                       # Stops the window from updating 

'''Scores'''
score_a = 0  # Score counter of Player A
score_b = 0  # Score counter of Player B

'''Paddle A'''
paddle_a = turtle.Turtle()                        # Paddle A is a turtle object
paddle_a.speed(0)                                 # Speed of animation to maximum
paddle_a.shape("square")                          # Shape of the object
paddle_a.color("white")                           # Color of the object
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Size of the object
paddle_a.penup()                                  # Don't draw any trayectory lines
paddle_a.goto(-350, 0)                            # Located in (-350,0)

'''Paddle B'''
paddle_b = turtle.Turtle()                        # Paddle B is a turtle object
paddle_b.speed(0)                                 # Speed of animation to maximum
paddle_b.shape("square")                          # Shape of the object
paddle_b.color("white")                           # Color of the object
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Size of the object
paddle_b.penup()                                  # Don't draw any trayectory lines
paddle_b.goto(350, 0)                             # Located in (350,0)

'''Ball'''
ball = turtle.Turtle()                            # Ball is a turtle object
ball.speed(0)                                     # Speed of Animation to maximum
ball.shape("square")                              # Shape of the object
ball.color("white")                               # Color of the object
ball.penup()                                      # Don't draw any trayectory lines
ball.goto(0, 0)                                   # Located in (0,0)
ball.dx = 0.15                                    # Ball's X inicial speed
ball.dy = 0.15                                    # Ball's Y inicial speed

'''Pen'''                                         
pen = turtle.Turtle()                             # Ball is a turtle object
pen.speed(0)                                      # Speed of Animation to maximum
pen.color("white")                                # Color of the object
pen.penup()                                       # Don't draw any trayectory lines
pen.hideturtle()                                  # Make the turtle invisible
pen.goto(0,260)                                   # Located in (0,260)
pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
                                                  # Content of the Pen showed on screen

'''Methods'''
# Paddle A up movement
def paddle_a_up():                
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y) 
    if(paddle_a.ycor()>250): # If structure avoid that the Paddle left the screen 
        paddle_a.sety(250)

# Paddle A down movement    
def paddle_a_down():                  
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
    if(paddle_a.ycor()<-250): # If structure avoid that the Paddle left the screen 
        paddle_a.sety(-250)

# Paddle B up movement    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
    if(paddle_b.ycor()>250): # If structure avoid that the Paddle left the screen
        paddle_b.sety(250)

# Paddle B down movement   
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)
    if(paddle_b.ycor()<-250): # If structure avoid that the Paddle left the screen
        paddle_b.sety(-250)
        
'''Keyboard blinding'''
window.listen()                           # Pay attention
window.onkeypress(paddle_a_up, "w")       # Activete method paddle_a_up when press w 
window.onkeypress(paddle_a_down, "s")     # Activete method paddle_a_down when press s 
window.onkeypress(paddle_b_up, "Up")      # Activete method paddle_b_up when press Up 
window.onkeypress(paddle_b_down, "Down")  # Activete method paddle_b_down when press Down 


'''Main game loop'''
while True:
    window.update()     # Every time the main loop runs, it updates the screen
    
    '''Bal's movement'''
    ball.setx(ball.xcor() + ball.dx)    # Movement on X axis 
    ball.sety(ball.ycor() + ball.dy)    # Movement on Y axis 
    
    '''Borders delimitation'''
    # Border checking axis Y
    if ball.ycor() > 290:   # if the ball hits the top of the window, then it bounces down
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:  # if the ball hits the end of the window, then it bounces up
        ball.sety(-290)
        ball.dy *= -1
        
    # Border checking axis X
    if ball.xcor() > 390: # If the ball crosses player B's goal, return it to the center and +1 point to Player A
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
        
    if ball.xcor() < -390: # If the ball crosses player A's goal, return it to the center and +1 point to Player B
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
    
    '''Paddles Collisions'''
    # Paddle B and ball collisions
    # If the ball hits the Paddle B, the ball bounce back
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    # Paddle A and ball collisions
    # If the ball hits the Paddle A, the ball bounce back
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

'''
References:
    freeCodeCamp.org(2018) Python Pong Game: https://www.youtube.com/watch?v=C6jJg9Zan7w
    Python 3.3.7 Documentations: https://docs.python.org/3.3/library/turtle.html?highlight=turtle 
'''