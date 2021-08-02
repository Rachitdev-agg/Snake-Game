from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class snake:
    def __init__(self):
        self.snakes = []
        starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        for pos in starting_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        place = pos
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(place)
        self.snakes.append(new_part)
    def extend(self):
        self.add_segment(self.snakes[-1].position())
    def move(self):
        for segment in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[segment - 1].xcor()
            new_y = self.snakes[segment - 1].ycor()
            self.snakes[segment].goto(new_x, new_y)
        self.snakes[0].forward(20)
    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)
    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)