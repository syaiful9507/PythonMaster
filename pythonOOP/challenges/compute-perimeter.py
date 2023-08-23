class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_perimeter(self):
        result = self.x + self.y + self.z
        return result


a = int(input())
b = int(input())
c = int(input())

perimeter = Triangle(a,b,c)
print(perimeter.get_perimeter())

