"""
                                                                                            Candidatenr: 1017
Note!

I have chosen not to comment the code explicitly,
but instead I have converted "comments" to variables, methods and class names to make the code self-explanatory.
I have also used a visual separator or divider to improve the readability and organization of the output.
Maybe this isn't the best way to practice. But in this case I find it easier to check/control the code 
and understand it this way.

"""

class Bug:
    def __init__(self, initialPosition):
        self.position = initialPosition
        self.directionR = 1  
        self.directionL = -1

    def turn(self):
        self.position += self.directionL
        self.directionR = -self.directionL
        
        print("Turned", "left," if self.directionL == -1 else "right", f"new position is: {self.position}")

    def move(self):
        self.position += self.directionR
        print("Moved forward to right, new position:", self.position)

    def getPosition(self):
        return self.position

bugsy = Bug(10)
print("-----------------------------")
print("Starting position is:", bugsy.getPosition())
print("-----------------------------")

bugsy.move()
bugsy.turn()
bugsy.move()
bugsy.move()
bugsy.turn()
bugsy.move()
bugsy.move()
bugsy.turn()

print("-----------------------------")
print("Final position is:", bugsy.getPosition())
print("-----------------------------")