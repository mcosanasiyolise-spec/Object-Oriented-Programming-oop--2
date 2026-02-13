from turtle import *

class Face:

    def__init__(self, xpos, ypos):
    self.size = 90
    self.coord = (xpos, ypos)
    self.noseSize = 'small'

    def setSize(self, radius):
        self.size = radius 

    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
         self.drawEye(45)
        selfMouth()
        self.drawNose()
        pensize(5)


        def goHome(self):
           penup()
           goto(self.coord)

           setheading(0)

           def drawoutline(self):
              penup()
              forward(self.size)
              left(90)
              pendown()
             circle(self.size) 
           self.goHome()

           def drawEye(self, turn):
              penup()
              left(turn)
              forward(self.size/ 2)
              pendown()
              dot(self.size/10)
              self.goHome()

              def drawMouth(self):
                 penup()

                 right(135)
                 forward(self.size/1.7)
                 left(90)
                 pendown()

                 circle(self.size/1.7,90)
                 self.goHome()

                 def drawNose(self):
                    if self.noseSize == 'large':
                       dot(self.size/2, "grey")
                    elif self.noseSize =='small' :
                       dot(self.size/6, "grey")
                    else:
                       dot(self.size/4, "grey")
                    self.goHome()

                    fl = Face(0, 0)
                    fl.draw()

                    showturtle()
                    done()