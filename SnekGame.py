""" TODO
Give snek nommies

"""
from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

### Variables ----------------------
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
blank=(0,0,0)

snek=[[2,4],[3,4],[4,4]]
direction="right"


sense.set_pixel(0,2,blue)
sense.set_pixel(7,4,red)

#snek.append() #add suff to the snek

#### Functoions ---------------------
def draw_snek():
    for point in snek:
        sense.set_pixel(point[0], point[1], white)

def move(direction):
    last= snek[-1]
    first=snek[0]
    next=list(last)
    
    if direction == "right":
        next[0]=last[0] + 1
        if next[0]== 8:
            next[0] = 0
    
    if direction == "left":
        next[0]=last[0] - 1
        if next[0]== -1:
            next[0] = 7
    
    if direction == "up":
        next[1]=last[1] - 1
        if next[1]== -1:
            next[1] = 7
 
    if direction == "down":
        next[1]=last[1] + 1
        if next[1]== 8:
            next[1] = 0

    sense.set_pixel(next[0], next[1], white) # draw the new part of snek (x,y, color)
    snek.append(next)
    sense.set_pixel(first[0], first[1], blank) # remove old tail position (x,y,color)
    snek.remove(first)

#def joystick_moved(event):
#    global direction
#    direction = event.direction
        
def pushed_up(event):
    global direction
    if event.action == 'pressed' and direction != "down":
        direction = "up"
        #print("pushed up")
        # move(direction)
    
def pushed_down(event):
    global direction
    if event.action == 'pressed' and direction != "up":
        direction = "down"
        #print("pushed down")
        # move(direction)

def pushed_left(event):
    global direction
    if event.action == 'pressed'  and direction != "right":
        direction = "left"
        #print("pushed left")
        # move(direction)

def pushed_right(event):
    global direction
    if event.action == 'pressed' and direction != "left":
        direction = "right"
        #print("pushed right")
        # move(direction)


##### Main -----------------------
sense.clear()
draw_snek()

while True:
    move(direction)
    sleep(0.5)
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
        
        