from turtle import *


def twin_tails():
    color("#EAA7CA","#EAA7CA")
    penup()
    goto(-80, 170)
    pendown()
    begin_fill()
    
    seth(120)
    circle(70, 130)
    circle(700, 20)
    circle(-350, 40)
    seth(0)
    forward(140)
    seth(70)
    circle(800, 25)
    
    end_fill()
    color("#2A191F","#2A191F")
    penup()
    goto(80, 170)
    pendown()
    begin_fill()
    
    seth(60)
    circle(-70, 130)
    circle(-700, 20)
    circle(350, 40)
    seth(180)
    forward(140)
    seth(110)
    circle(-800, 25)
    
    end_fill()
    





def head():
    color("#FBE6E3","#FBE6E3")
    penup()
    goto(-150,50)
    pendown()
    begin_fill()
    
    seth(265)
    circle(400, 20)
    circle(40, 20)
    circle(300, 33)
    color("#FBE6E3","#FBE6E3")
    goto(0, 50)
    
    end_fill()
    penup()
    goto(150,50)
    pendown()
    begin_fill()
    
    seth(275)
    circle(-400, 20)
    circle(-40, 20)
    circle(-300, 33)
    color("#FBE6E3","#FBE6E3")
    goto(0, 50)
    
    end_fill()
    penup()
    goto(150,50)
    pendown()
    begin_fill()
    
    seth(90)
    circle(150, 180)
    
    end_fill()
    

def hairline():
    color("#EAA7CA","#EAA7CA")
    penup()
    goto(0, 200)
    pendown()
    begin_fill()
    
    seth(180)
    circle(151, 90)
    left(150)
    circle(-150, 67)
    goto(0, 123)
    
    end_fill()
    color("#2A191F","#2A191F")
    penup()
    goto(0, 200)
    pendown()
    begin_fill()
    
    seth(0)
    circle(-151, 90)
    right(150)
    circle(150, 67)
    goto(0, 123)
    
    end_fill()


def collars():
    color("#3A292F","#3A292F")
    penup()
    goto(-130, 120)
    pendown()
    
    pensize(10)
    
    seth(170)
    circle(-100, 90)
    circle(-15, 95)
    circle(-100, 40)

    penup()
    goto(-130, 120)
    pendown()
    
    seth(210)
    circle(-120, 70)
    circle(-10, 120)
    circle(-120, 25)
    
    color("#FAB7DA","#FAB7DA")
    penup()
    goto(130, 120)
    pendown()
    
    seth(10)
    circle(100, 90)
    circle(15, 95)
    circle(100, 40)

    penup()
    goto(130, 120)
    pendown()
    
    seth(330)
    circle(120, 70)
    circle(10, 120)
    circle(120, 25)



    pensize(5)
    color("#B9B9B7","#B9B9B7")
    penup()
    goto(-130, 120)
    pendown()
    
    seth(170)
    for i in range (9):
        penup()
        circle(-100, 9)
        pendown()
        circle(-100, 1)
    
    penup()
    goto(-130, 120)
    pendown()
    
    seth(210)
    for i in range (7):
        penup()
        circle(-120, 9)
        pendown()
        circle(-120, 1)
    
    penup()
    goto(130, 120)
    pendown()
    
    seth(10)
    for i in range (9):
        penup()
        circle(100, 9)
        pendown()
        circle(100, 1)
    
    penup()
    goto(130, 120)
    pendown()
    
    seth(330)
    for i in range (7):
        penup()
        circle(120, 9)
        pendown()
        circle(120, 1)
        


    pensize(1)





def horns():
    color("#EE97B7","#EE97B7")
    penup()
    goto(-80, 150)
    pendown()
    begin_fill()
    
    seth(110)
    forward(100)
    right(150)
    forward(100)
    seth(250)
    circle(-45, 70) 
    
    end_fill()
    penup()
    goto(80, 150)
    pendown()
    begin_fill()
    
    seth(70)
    forward(100)
    left(150)
    forward(100)
    seth(290)
    circle(45, 70) 
    
    end_fill()


def bang():
    color("#FAB7DA","#FAB7DA")
    penup()
    goto(0, 123)
    pendown()
    begin_fill()
    
    seth(100)
    circle(50, 120)
    right(50)
    circle(40, 65)
    circle(300, 50)
    left(175)
    circle(-300, 30)
    right(170)
    circle(350, 40)
    left(170)
    circle(-350, 15)
    right(170)
    circle(100, 30)
    left(175)
    circle(-120, 40)
    right(150)
    circle(100, 40)
    left(160)
    circle(-130, 40)
    right(160)
    circle(100, 40)
    left(150)
    circle(-110, 70)
    right(140)
    circle(150, 50)
    left(160)
    circle(-200, 50)
    circle(-34, 115)
    
    end_fill()
    color("#3A292F","#3A292F")
    penup()
    goto(0, 123)
    pendown()
    begin_fill()
    
    seth(60)
    circle(-50, 90)
    left(30)
    forward(5)
    circle(-60, 60)
    circle(-250, 60)
    right(170)
    circle(250, 10)
    left(175)
    circle(-250, 30)
    right(155)
    circle(250, 5)
    left(160)
    circle(-250, 5)
    right(170)
    circle(350, 30)
    left(175)
    circle(-250, 10)
    right(175)
    circle(250, 47)
    circle(38, 95)
    
    end_fill()
    
    color("#FAB7DA","#FAB7DA")
    penup()
    goto(95, 50)
    pendown()
    pensize(3)
    
    seth(340)
    forward(40)
    penup()
    goto(130, 55)
    pendown()
    seth(220)
    forward(38)
    
    pensize(1)
    
    
    

if __name__ == "__main__":
    speed(0)
    hideturtle()
    bgcolor("#F8D7E7")
    
    twin_tails()
    head()
    hairline()
    collars()
    horns()
    bang()
    
    done()