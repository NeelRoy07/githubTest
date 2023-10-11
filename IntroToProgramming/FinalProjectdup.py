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

sc = turtle.Screen()
sc.title("Crossy Road by Neel")
sc.bgcolor("lightblue")
sc.screensize(canvwidth=600, canvheight=300)
sc.tracer(0)

# the player
player = turtle.Turtle()
player.speed(0)
player.color("green")
player.shape("triangle")
player.penup()
player.goto(-430, 0)

# the different obstacles in a dictionary
my_car_dic = {}
for i in range(12):
    car = turtle.Turtle()
    car.speed(0)
    car.color("red")
    car.shape("circle")
    car.penup()
    car.goto(50*i, 75*i)
    my_car_dic["car_"+str(i)] = car

LiveNum = turtle.Turtle()
LiveNum.hideturtle()
LiveNum.penup()
LiveNum.setposition(100, 250)
LiveNum.write("Lives: " + str(lives), align="center",
              font=("Arial", 30, "normal"))

#Function moves the objects
def MoveObs(car, number):
    # I am assuming even numbered cars are going down while odd numbered cars are going up
    if number % 2 == 0:
        # means it is an even numbered car
        if car.ycor() > -198:
            car.sety(car.ycor()-random.randint(5, 10))
        else:
            car.sety(198)

    else:
        #otherwise it is an odd numbered car
        if car.ycor() < 198:
            car.sety(car.ycor()+random.randint(10, 20))
        else:
            car.sety(-198)


# creates all the level obstacles and everything
c = turtle.Turtle()
c.speed(0)
c.pencolor("black")
c.hideturtle()

drawer = turtle.Turtle()
timer = turtle.Turtle()

# key binds
def GoF():
    global px, py
    px += 10
    player.goto(px, py)

def GoB():
    global px, py
    px -= 10
    player.goto(px, py)

def GoUp():
    global px, py
    py += 10
    player.goto(px, py)

def GoDown():
    global px, py
    py -= 10
    player.goto(px, py)

#Draws the road
def DrawRoad(x):
    c.penup()
    c.setpos(x, 200)

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

#checks the distance of the player from the obstacles
def car_dist(car_var):
    global lives, px, py
    if player.distance(car_var) < 15:
        lives -= 1
        player.goto(-430, 0)
        px = -430
        py = 0
        LiveNum.clear()
        LiveNum.write("Lives: " + str(lives), align="center",
                      font=("Arial", 30, "normal"))

#sets the position of the different obstalces
def CarPos():
    my_car_dic["car_0"].goto(-290, 195)
    my_car_dic["car_1"].goto(-260, -195)
    my_car_dic["car_2"].goto(-10, 195)
    my_car_dic["car_3"].goto(310, 195)
    my_car_dic["car_4"].goto(340, -195)
    my_car_dic["car_5"].goto(-40, 195)
    my_car_dic["car_6"].goto(-290, 195)
    my_car_dic["car_7"].goto(-260, -195)
    my_car_dic["car_8"].goto(-10, 195)
    my_car_dic["car_9"].goto(310, 195)
    my_car_dic["car_10"].goto(340, -195)
    my_car_dic["car_11"].goto(-40, 195)


def LevelDifficulty():
    global lives, px, py, lost

    name = input("What is your name? ")
    Difficulty = input("Hello " + name + ". Would you like to play easy, medium, or hard? ")
    times = [16, 21, 26]

    drawer.penup()
    drawer.setpos(-300, 260)
    timer.setpos(-300, 260)

    sc.listen()
    sc.onkeypress(GoF, "d")
    sc.onkeypress(GoB, "a")
    sc.onkeypress(GoUp, "w")
    sc.onkeypress(GoDown, "s")

    if Difficulty.lower() == "hard":
        print("You have 15 seconds")
        time.sleep(2)

        start = time.time()
        while time.time() - start < times[0] and True:

            for num, car in enumerate(my_car_dic):
                MoveObs(my_car_dic[car], num)

            # timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start),font=("Courier", 30, "normal"), align="center")

            for key in my_car_dic.keys():
                car_dist(my_car_dic[key])

            if lives == 0:
                c.clear()

                for i in range(12):
                    my_car_dic[("car_"+str(i))].clear()

                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You have no lives left. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.ycor() > 205 or player.ycor() < -205:
                c.clear()

                for i in range(12):
                    my_car_dic[("car_"+str(i))].hideturtle()

                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You went oustide the playing field. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.xcor() > 430:
                c.clear()

                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("Congradulations!!! You Won", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            sc.update()

        c.setpos(0, 0)
        c.clear()
        c.write("You ran out of time.", align="center", font=("Arial", 30, "normal"))
        time.sleep(2)

    elif Difficulty.lower() == "medium":
        print("You have 20 seconds")
        time.sleep(2)

        start = time.time()
        while time.time() - start < times[1] and True:
            # timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            for num, car in enumerate(my_car_dic):
                MoveObs(my_car_dic[car], num)

            # timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            for key in my_car_dic.keys():
                car_dist(my_car_dic[key])

            if lives == 0:
                c.clear()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You have no lives left. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.ycor() > 205 or player.ycor() < -205:
                c.clear()

                for i in range(12):
                    my_car_dic[("car_"+str(i))].hideturtle()

                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You went oustide the playing field. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.xcor() > 430:
                c.clear()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("Congradulations!!! You Won", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            sc.update()

        c.setpos(0, 0)
        c.clear()
        c.write("You ran out of time.", align="center",
                font=("Arial", 30, "normal"))
        time.sleep(2)

    elif Difficulty.lower() == "easy":
        print("You have 25 seconds")
        time.sleep(2)

        start = time.time()
        while time.time() - start < times[2] and True:
            # timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            for num, car in enumerate(my_car_dic):
                MoveObs(my_car_dic[car], num)

            # timer part
            drawer.forward(1)
            drawer.left(1)
            timer.clear()
            timer.write(int(time.time() - start), font=("Courier", 30, "normal"), align="center")

            for key in my_car_dic.keys():
                car_dist(my_car_dic[key])

            if lives == 0:
                c.clear()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You have no lives left. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.ycor() > 205 or player.ycor() < -205:
                c.clear()

                for i in range(12):
                    my_car_dic[("car_"+str(i))].hideturtle()

                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("You went oustide the playing field. You lost.", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            if player.xcor() > 430:
                c.clear()
                LiveNum.clear()
                drawer.hideturtle()
                timer.hideturtle()
                timer.clear()
                drawer.clear()

                c.setposition(0, 0)
                c.write("Congradulations!!! You Won", align="center", font=("Arial", 30, "normal"))
                time.sleep(2)
                return False

            sc.update()

        c.setpos(0, 0)
        c.clear()
        c.write("You ran out of time.", align="center",
                font=("Arial", 30, "normal"))
        time.sleep(2)

    else:
        print("Please enter easy, medium or hard")

#The actual level
def Level1():
    global lives, px, py, lost

    c.right(90)

    DrawRoad(-299)

    DrawRoad(-52)

    DrawRoad(297)

    c.penup()

    CarPos()

    LevelDifficulty()

Level1()