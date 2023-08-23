# Replace ___ with your code

# create the Coordinate class
class Coordinate:

    # initialize x and y attributes inside __init__()
    def __init__(self, x,y):
        self.x = x
        self.y = y

    # define the add_coordinates() method
    def add_coordinates(self, c2):
        x = self.x + c2.x
        y = self.y + c2.y







# create objects c1 and c2
c1 = Coordinate(5,6)
c2 = Coordinate(7,9)

# call the add_coordinates() method
c3 = c1.add_coordinates(c2)
print(c3.x)
print(c3.y)

