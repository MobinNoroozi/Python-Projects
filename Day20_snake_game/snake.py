from turtle import Turtle
from test.test_inspect.inspect_fodder2 import positional_only_arg
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        #Snake has a list of segments
        self.segments = []
        self.create_snake() #It create a snake
        self.head = self.segments[0] #Also gets the head which is the first segment

    #Add those positions in order, that creates our snake with 3 segments 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) #adds those segments that each of them is a turtle object
            

    
    #Sets up the shape and color, and adds then into the segments list.
    def add_segment(self, position):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    
    def extend(self):
    """Add a new segment to the end (tail) of the snake.

    We create the new segment at the current position of the last segment
    (self.segments[-1].position()). It will initially overlap the tail,
    but on the next move the normal movement logic will make it follow the snake.
    """
        self.add_segment(self.segments[-1].position())


    def move(self):
    """Move the snake forward.

    To move the whole snake, iterate from the last segment toward the first
    (excluding the head) and set each segment's position to the position of
    the segment in front of it. Doing this backwards avoids overwriting a
    segment's position before it has been copied for the following segment.

    After shifting all body segments, move the head forward by MOVE_DISTANCE
    in whatever direction the head is currently facing.
    """
    # Start at the tail and move each segment to the position of the segment ahead of it.
        for seg_num in range(len(self.segments)-1, 0, -1):
 # Get the coordinates of the segment in front of the current one
            new_x = self.segments[seg_num-1].xcor()    
            new_y = self.segments[seg_num-1].ycor()    
             # Move current segment to that position
           self.segments[seg_num].goto(new_x, new_y)
# Finally, move the head forward so the entire snake advances
        self.head.forward(MOVE_DISTANCE)



    def up(self): #Avoids the snake to run on its own
        if (self.head.heading() != DOWN):
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
        #Move all the segments of the current snake out of the view
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear() #Then clear them 
        self.create_snake() #Create another snake
        self.head = self.segments[0] #Set the head
