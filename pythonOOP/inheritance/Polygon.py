class Polygon:
    def __init__(self, sides):
        self.sides = sides
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    # create object
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

class Triangle(Polygon):

    def display_info(self):
        print("A triangle is a polygon with 3 edges.")
        
        # call the display_info() method of Polygon
        super().display_info()

triangle = Triangle([3,4,100])
triangle.display_info()
perimeter = triangle.get_perimeter()
print(perimeter)