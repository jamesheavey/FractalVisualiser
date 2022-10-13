import turtle


class fractal_visualiser(turtle.Turtle):
    def __init__(self, speed, shape:str, colour:str, fill='yellow'):
        turtle.Turtle.__init__(self)
        self.speed(speed)
        self.colour = colour
        self.color(colour, fill)
        self.shape(shape)
        self.setheading(90)
        
    def tree(self, size, levels, angle):
        if levels == 0:
            self.color("green")
            self.dot(size)
            self.color(self.colour)
            return
        
        self.forward(size)
        self.right(angle)
        self.tree(size * 0.8, levels - 1, angle)
        
        self.left(2 * angle)
        self.tree(size * 0.8, levels - 1, angle)
        
        self.right(angle)
        self.backward(size)
        
    def snowflake(self, size, levels):
        return
        
        


turt = fractal_visualiser(0, 'turtle', 'red')

turt.tree(100, 6, 40)



turtle.done()