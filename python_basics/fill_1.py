from turtle import *

speed(0)
r = 40
width( r / 20)
def cir():
    color('black', 'green')
    begin_fill()
    fd(r)
    lt(90)
    circle(r, 90)
    lt(90)
    fd(2 * r)
    rt(90)
    circle(-r, 90)
    rt(90)
    fd(r)
    end_fill()
    fd(r)
    rt(90)
    circle(-r)

up()
goto(r, r)
down()
cir()
up()
goto(-r, -r)
down()
cir()
