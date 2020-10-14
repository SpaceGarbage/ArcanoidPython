ballx= 0
bally= 0

ballspeedx= 5
ballspeedy= 2
ballradius= 5

racketx= 0
rackety= 0
racketwidth= 50
racketheight= 20


def setup ():
    global ballx, bally, racketx, rackety, racketwidth, racketheight
    print "Hello World"
    size (400, 400)
    clear()
    frameRate (60)
    ballx=width/2
    bally=width/2
    racketx= mouseX- (racketwidth/2)
    rackety= height - 20
   
def draw ():
    clear ()
    drawRacket()
    drawBall()

def drawRacket ():
    global racketx, rackety, ballspeedx, ballspeedy, racketwidth, racketheight
   
    fill (255)
    #draw a rectangle in coords
    #x : mouse x minus half of width
    #y : height of the window minus 20
    #width : 50
    #height : 10
    racketx= mouseX - (racketwidth/2)
    rect(racketx, rackety, racketwidth, 10)
       

def drawBall ():
    global ballx, bally, ballspeedx, ballspeedy, racketx, rackety, racketwidth, ballradius, racketheight
   
    #circle (ballx, bally, 10)
    #ballx=ballx+ ballspeedx
    #bally=bally+ ballspeedy
    ballx += ballspeedx
    bally += ballspeedy
   
    #if (ballx + 5 > width):
        #ballspeedx *= -1
    #if (bally + 5 > width):
        #ballspeedy *= -1
   
    #if (ballx + 5 < 0):
        #ballspeedx *= -1
    #if (bally + 5 < 0):
        #ballspeedy *= -1
   
    #droite
    if(ballx + ballradius > width):
        ballspeedx *= -1
        ballx = width-ballradius
    #bas
    elif(bally + ballradius > height):
        ballspeedy *= -1
        bally = height-ballradius
       
    #gauche
    if(ballx - ballradius < 0):
        ballspeedx *= -1
        ballx = ballradius
   #haut
    elif(bally - ballradius < 0):
        ballspeedy *= -1
        bally = ballradius
       
    if(rackety < bally + ballradius < rackety + racketheight > rackety and ballspeedy > 0):
        if (racketx < ballx < racketx + racketwidth) :
           ballspeedy *= -1
           bally = rackety - ballradius
        

       
    circle(ballx, bally, 2*ballradius)
   
