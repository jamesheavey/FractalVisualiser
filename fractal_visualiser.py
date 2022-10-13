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
            self.dot(size/2)
            self.color(self.colour)
            return
        
        self.forward(size)
        self.right(angle)
        self.tree(size * 0.8, levels - 1, angle)
        
        self.left(2 * angle)
        self.tree(size * 0.8, levels - 1, angle)
        
        self.right(angle)
        self.backward(size)
        
    def snowflake(self, size, levels, sides):
        
        def snowflake_side(size, levels):
            if levels == 0:
                self.forward(size)
                return
            size /= 3
            
            snowflake_side(size, levels - 1)
            self.left(60)
            snowflake_side(size, levels - 1)
            self.right(120)
            snowflake_side(size, levels - 1)
            self.left(60)
            snowflake_side(size, levels - 1)
            
        for i in range(sides):
            snowflake_side(size, levels)
            self.right(360/sides)
    
    def square(self, size, levels):
        def square_side(size, levels):
            if levels == 0:
                self.forward(size)
                return
            size /= 2
            
            square_side(size, levels - 1)
            self.left(90)
            square_side(size, levels - 1)
            self.right(90)
            square_side(size, levels - 1)
        
        for i in range(4):
            square_side(size, levels)
            self.right(90)
        

def main():
    turt = fractal_visualiser(0, 'turtle', 'red')

    # turt.tree(100, 6, 30)

    # turt.snowflake(100,3,3)
    
    turt.square(100, 4)

    turtle.done()
    
main()