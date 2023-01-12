from turtle import *
space = Screen()
neel = Turtle()

print("Enter the side length: ")

side = int(input())

print("Number of houses: ")

neel.penup()
neel.goto(-240,0)
neel.pendown()

numHouse = int(input())

i = 1

def square()  :
  neel.forward(side)
  neel.left(90)
  neel.forward(side)
  neel.left(90)
  neel.forward(side)
  neel.left(90)
  neel.forward(side)


def triangle()  :
  neel.forward(side)
  neel.left(120)
  neel.forward(side)
  neel.left(120)
  neel.forward(side)
  neel.left(120)


def house()   :
  square()
  neel.left(180)
  neel.forward(side)
  neel.right(90)
  triangle()
  neel.forward(side)
  neel.right(90)
  neel.forward(side)
  neel.left(90)


while (i <= numHouse) :
  house()
  i = i + 1
                                                                      
