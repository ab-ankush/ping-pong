from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color("white")
        self.shapesize(5, 1, None)
        self.goto(position)

    def up(self):
        if self.ycor() <= 280:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() > -280:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
