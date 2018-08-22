from turtle import *
import turtle
from random import randint
n=int(input("Enter the no of persons to start the race(between 2 to 7) : "))
print()
a=[]
for i in range(n):
    a1=input("enter the name of player "+str(i+1)+" :")
    print()
    a.append(a1)
def race(pa,b):
    t=Pen()
    t.shape("arrow")
    
    turtle.setup(1300, 650)
    t.screen.bgcolor("pink")
    t.color("red")
    t.speed(10)
    t.up()
    t.goto(-600,200)
    a1=200
    t.down()
    bb=[]
    col=["green","blue","red","DarkGoldenrod","cyan","gray","purple"]
    for i in b:
        bb.append(i)
    for l in range(len(b)):
        b[l]=turtle.Turtle()
        b[l].shape("turtle")
    for i in range(10):
        t.write(i+1)
        for j in range(pa+1):
            t.forward(150)
            t.up()
            t.forward(15)
            t.down()
        a1=a1-45
        t.up()
        t.goto(-600,a1)
        t.down()
    aa=-450    
    for i in range(pa):
        b[i].penup()
        
        b[i].goto(aa,210)
        
        b[i].write(bb[i])
        b[i].goto(aa+7,200)
        b[i].pendown()
        aa=aa+150+15
        b[i].color(col[i])
        b[i].right(90)
    t.up()
    t.goto(-500,250)
    t.down()
    score=[]
    for i in range(len(b)):
        score.append(0)
    t.write("RACE STARTED",font=("Arial", 20, "normal"))
    for j in range(130):
        for i in range(len(b)):
            if(j>90):
                for k in score:
                    if(k>410):
                        break
            temp=randint(1,5)
            b[i].forward(temp)
            score[i]=score[i]+temp
    max1=max(score)
    for i in range(len(score)):
        if(score[i]==max1):
            t.up()
            t.goto(-400,-250)
            t.down()
            t.write(str(bb[i])+"  WON THE MATCH ",font=("Arial", 25, "bold"))
            























    
race(n,a)

    
    
