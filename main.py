import turtle

# creating canvas
turtle.Screen().bgcolor("pink")

sc = turtle.Screen()
sc.setup(700,800)
turtle.title("Welcome to Turtle Windows")
# turtle object creation
board = turtle.Turtle()
# Creating a square 
for i in range(4):
    board.forward(200)
    board.left(90)
    i = i+1
    