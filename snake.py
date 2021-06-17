from turtle import Turtle

square_position =[(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in square_position:
            self.add_segment(i)


    def add_segment(self, i):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(i)
        self.segments.append(square)

    def extend_snake(self):
        # adds new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y) #last segmant moves to the position of 2nd last & so on.
        self.head.forward(20)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)    #to make previous snake disappear
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]