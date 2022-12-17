"""TODO: create and move Paddle"""
from paddle import Paddle
from ball import Ball

"""TODO: create cpu controlled Paddle"""

ball = Ball()


class CPU_paddle(Paddle):

    def __init__(self):
        super().__init__()
        self.direction = ball.ycor()

    def follow_ball(self):
        self.goto(self.direction)
