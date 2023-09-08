from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1
        self.move_speed *= 0.9

    def rollback(self):
        self.x_bounce()
        self.move_speed = 0.1
        self.goto(0, 0)
