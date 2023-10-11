import turtle
import random
import time


"""
Neel Roy
This game is another version of crossy road in which the player has to get to the other side in a specified time limit
Period 8
"""

lives = 3
px = -430
py = 0

lost = 0

sc = turtle.Screen()
sc.title("Crossy Road by Neel")
sc.bgcolor("lightblue")
sc.screensize(canvwidth=600, canvheight=300)
sc.tracer(0)


#the player
player = turtle.Turtle()
player.speed(0)
player.color("green")
player.shape("triangle")
player.penup()
player.goto(-430,0)

#the different obstacles
car1 = turtle.Turtle()
car1.speed(0)
car1.color("red")
car1.shape("circle")
car1.penup()
car1.goto(-289,200)

car2 = turtle.Turtle()
car2.speed(0)
car2.color("red")
car2.shape("circle")
car2.penup()
car2.goto(-260,-200)

car3 = turtle.Turtle()
car3.speed(0)
car3.color("red")
car3.shape("circle")
car3.penup()
car3.goto(-10,200)

car4 = turtle.Turtle()
car4.speed(0)
car4.color("red")
car4.shape("circle")
car4.penup()
car4.goto(310,200)

car5 = turtle.Turtle()
car5.speed(0)
car5.color("red")
car5.shape("circle")
car5.penup()
car5.goto(340,-200)

car6 = turtle.Turtle()
car6.speed(0)
car6.color("red")
car6.shape("circle")
car6.penup()
car6.goto(-40,200)

car7 = turtle.Turtle()
car7.speed(0)
car7.color("red")
car7.shape("circle")
car7.penup()
car7.goto(-289,200)

car8 = turtle.Turtle()
car8.speed(0)
car8.color("red")
car8.shape("circle")
car8.penup()
car8.goto(-40,200)

car9 = turtle.Turtle()
car9.speed(0)
car9.color("red")
car9.shape("circle")
car9.penup()
car9.goto(260,-200)

car10 = turtle.Turtle()
car10.speed(0)
car10.color("red")
car10.shape("circle")
car10.penup()
car10.goto(310,200)

car11 = turtle.Turtle()
car11.speed(0)
car11.color("red")
car11.shape("circle")
car11.penup()
car11.goto(340,-200)

car12 = turtle.Turtle()
car12.speed(0)
car12.color("red")
car12.shape("circle")
car12.penup()
car12.goto(-40,200)

LiveNum = turtle.Turtle()
LiveNum.hideturtle()
LiveNum.penup()
LiveNum.setposition(100,250)
LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))




#creates all the level obstacles and everything
c = turtle.Turtle()
c.speed(0)
c.pencolor("black")
c.hideturtle()

drawer = turtle.Turtle()
timer = turtle.Turtle()


#function that moves all of the obstacles
def MoveObs():
    y1 = car1.ycor()
    y2 = car2.ycor()
    y3 = car3.ycor()
    y4 = car4.ycor()
    y5 = car5.ycor()
    y6 = car6.ycor()
    y7 = car7.ycor()
    y8 = car8.ycor()
    y9 = car9.ycor()
    y10 = car10.ycor()
    y11 = car11.ycor()
    y12 = car12.ycor()
    
    if car1.ycor() > -198:
        car1.sety(y1-random.randint(5,10))
    else:
        car1.goto(-290,195)
    if car2.ycor() < 198:
        car2.sety(y2+random.randint(5,10))
    else:
        car2.goto(-260,-195)
    if car3.ycor() > -198:
        car3.sety(y3-random.randint(5,10))
    else:
        car3.goto(-10,195)
    if car4.ycor() > -198:
        car4.sety(y4-random.randint(5,10))
    else:
        car4.goto(310,195)
    if car5.ycor() < 198:
        car5.sety(y5+random.randint(5,10))
    else:
        car5.goto(340,-195)
    if car6.ycor() > -198:
        car6.sety(y6-random.randint(5,10))
    else:
        car6.goto(-40,195)
    if car7.ycor() > -198:
        car7.sety(y7-random.randint(1,10))
    else:
        car7.goto(-290,195)
    if car8.ycor() < 198:
        car8.sety(y8+random.randint(1,10))
    else:
        car8.goto(-260,-195)
    if car9.ycor() > -198:
        car9.sety(y9-random.randint(1,10))
    else:
        car9.goto(-10,195)
    if car10.ycor() > -198:
        car10.sety(y10-random.randint(1,10))
    else:
        car10.goto(310,195)
    if car11.ycor() < 198:
        car11.sety(y11+random.randint(1,10))
    else:
        car11.goto(340,-195)
    if car12.ycor() > -198:
        car12.sety(y12-random.randint(1,10))
    else:
        car12.goto(-40,195)
    if car12.ycor() > -198:
        car12.sety(y12-random.randint(1,10))
    else:
        car12.goto(-40,195)
    
#key binds
def GoF():
  global px,py
  px += 10
  player.goto(px,py)

def GoB():
  global px,py
  px -= 10
  player.goto(px,py)

def GoUp():
  global px,py
  py += 10
  player.goto(px,py)

def GoDown():
  global px,py
  py -= 10
  player.goto(px,py)

def DrawRoad():
  for i in range(2):
    c.begin_fill()
    c.forward(400)
    c.left(90)
    c.forward(52)
    c.left(90)
    c.end_fill()
    c.begin_fill()
    c.circle(26)
    c.end_fill()

  c.left(90)
  c.forward(26)
  c.right(90)
  c.back(10)
  c.pendown()
  c.pencolor("yellow")
  c.forward(420)

def LevelDifficulty():
    global lives, px, py, lost

    name = input("What is your name? ")
    Difficulty = input("Hello "+ name + ". Would you like to play easy, medium, or hard? ")
    times = [16, 21, 26]
    
    drawer.penup()
    drawer.setpos(-300,260)
    timer.setpos(-300,260)

    sc.listen()
    sc.onkeypress(GoF, "d")
    sc.onkeypress(GoB, "a")
    sc.onkeypress(GoUp, "w")
    sc.onkeypress(GoDown, "s")
    
    if Difficulty.lower() == "hard":
        print("You have 15 seconds")

        start = time.time()
        while time.time() - start < times[0] and True:
            #timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            #checks the distances between the players and object
            MoveObs()
            
            if player.distance(car1) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car2) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car3) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car4) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car5) < 15:
                lives=lives-1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car6) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))
                
            if player.distance(car7) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car8) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car9) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car10) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car11) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car12) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if lives == 0:
                c.clear()
                car1.hideturtle()
                car2.hideturtle()
                car3.hideturtle()
                car4.hideturtle()
                car5.hideturtle()
                car6.hideturtle()
                car7.hideturtle()
                car8.hideturtle()
                car9.hideturtle()
                car10.hideturtle()
                car11.hideturtle()
                car12.hideturtle()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0,0)
                c.write("You have no lives left. You lost.", align = "center", font = ("Arial", 30, "normal"))
                time.sleep(2)
                return False
                lost = 1

            if player.xcor() > 430:
                c.clear()
                car1.hideturtle()
                car2.hideturtle()
                car3.hideturtle()
                car4.hideturtle()
                car5.hideturtle()
                car6.hideturtle()
                car7.hideturtle()
                car8.hideturtle()
                car9.hideturtle()
                car10.hideturtle()
                car11.hideturtle()
                car12.hideturtle()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0,0)
                c.write("Congradulations!!! You Won", align = "center", font = ("Arial", 30, "normal"))
                time.sleep(2)
                return False
                lost = 1
                

            sc.update()
        
    elif Difficulty.lower() == "medium":
        print("You have 20 seconds")

        start = time.time()
        while time.time() - start < times[1] and True:
            #timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            #checks the distances between the players and object
            MoveObs()
            
            if player.distance(car1) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car2) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car3) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car4) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car5) < 15:
                lives=lives-1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car6) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))
                
            if player.distance(car7) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car8) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car9) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car10) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car11) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car12) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if lives == 0:
                LiveNum.setpos(0,0)
                LiveNum.write("You have no lives remaining", align = "center", font = ("arial", 30, "normal"))
                return False
                lost = 1

            if player.xcor() > 430:
                c.clear()
                car1.hideturtle()
                car2.hideturtle()
                car3.hideturtle()
                car4.hideturtle()
                car5.hideturtle()
                car6.hideturtle()
                car7.hideturtle()
                car8.hideturtle()
                car9.hideturtle()
                car10.hideturtle()
                car11.hideturtle()
                car12.hideturtle()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0,0)
                c.write("Congradulations!!! You Won", align = "center", font = ("Arial", 30, "normal"))
                time.sleep(2)
                return False

            sc.update()
    elif Difficulty.lower() == "easy":
        print("You have 25 seconds")

        start = time.time()
        while time.time() - start < times[2] and True:
            #timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            #checks the distances between the players and object
            MoveObs()
            
            if player.distance(car1) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car2) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car3) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car4) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car5) < 15:
                lives=lives-1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car6) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))
                
            if player.distance(car7) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car8) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car9) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car10) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car11) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if player.distance(car12) < 15:
                lives -= 1
                player.goto(-430,0)
                px = -430
                py = 0
                LiveNum.clear()
                LiveNum.write("Lives: "+ str(lives), align="center", font=("Arial", 30, "normal"))

            if lives == 0:
                LiveNum.setpos(0,0)
                LiveNum.write("You have no lives remaining", align = "center", font = ("arial", 30, "normal"))
                time.sleep(2)

                return False

            if player.xcor() > 430:
                c.clear()
                car1.hideturtle()
                car2.hideturtle()
                car3.hideturtle()
                car4.hideturtle()
                car5.hideturtle()
                car6.hideturtle()
                car7.hideturtle()
                car8.hideturtle()
                car9.hideturtle()
                car10.hideturtle()
                car11.hideturtle()
                car12.hideturtle()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0,0)
                c.write("Congradulations!!! You Won", align = "center", font = ("Arial", 30, "normal"))
                time.sleep(2)

                return False

            sc.update()
    else:
        print("Please enter easy, medium or hard")


def Level1():
  global lives, px, py, lost
  c.penup()
  c.setposition(-273,178)
  c.pendown()
  c.fillcolor("black")
  c.penup()
  c.setpos(-299,200)
  c.pendown()
  c.begin_fill()
  c.right(90)

  DrawRoad()

  c.penup()
  c.setpos(-52,200)

  DrawRoad()

  c.penup()
  c.setpos(297,200)

  DrawRoad()


  c.penup()

  
  
  car1.goto(-290,195)
  car2.goto(-260,-195)
  car3.goto(-10,195)
  car4.goto(310,195)
  car5.goto(340,-195)
  car6.goto(-40,195)
  car7.goto(-290,195)
  car8.goto(-260,-195)
  car9.goto(-10,195)
  car10.goto(310,195)
  car11.goto(340,-195)
  car12.goto(-40,195)

  LevelDifficulty()
          
Level1()
