import turtle

wn = turtle.TurtleScreen
poli = turtle.Turtle()


### This function draws any regular polygon; n is the number of sides. ###

def drawPolygon(n):
   
   interiorAng = 360 / int(n)

   for i in range(0, n):
       poli.forward(70)
       poli.left(interiorAng)
      

### This function draws a square of a given side (in pixels) ###

def drawSquare(n):
    
    for i in range(0,4):
        poli.forward(float(n))
        poli.left(90)
