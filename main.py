#adding functions on this 
def curve():
  for j in range(200):
    pen.right(1)
    pen.forward(1)


def heart():
  pen.fillcolor("red")
  pen.begin_fill()
  pen.left(50)
  pen.forward(100)
  pen.circle(40,180)
  pen.left(260)
  pen.circle(40,180)
  pen.forward(100)
  pen.end_fill()

def text1():
  pen.up()
  pen.setpos(-68,95)
  pen.down()
  pen.color("green")
  pen.write("I Love you M")



#turtle is a python module 

import turtle
pen=turtle.Turtle()

def curve():
  for j in range(200):
    pen.right(1)
    pen.forward(1)
    
    #add the main body
    
heart()
text1()
pen.ht()


#adding new code on this
