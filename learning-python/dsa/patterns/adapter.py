class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
      super().__init__(circle.getRadius() * 2)
    
    def getSideLength(self) -> float:
      return self.sideLength
    
squarehole = SquareHole(5)
square = Square(5)
print(squarehole.canFit(square))

circle = Circle(2.5)
#print(squarehole.canFit(circle))

adapter = CircleToSquareAdapter(circle)
print(squarehole.canFit(adapter))