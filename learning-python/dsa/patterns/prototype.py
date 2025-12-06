from abc import ABC, abstractmethod
from typing import List

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        return Square(self.length)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.length})'

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        # result = [shape for shape in shapes]
        result = []
        for shape in shapes:
            result.append(shape.clone())
        return result
    
shapes = [
    Square(3),
    Rectangle(5, 4),
    Rectangle(3, 3),
    Square(5)
]

new_shapes = Test().clone_shapes(shapes)
for old_shape, new_shape in zip(shapes, new_shapes):
    print(
        f'Old shape ({old_shape}) is new shape({new_shape}): {old_shape is new_shape}'
    )

'''
Old shape (Square(3)) is new shape(Square(3)): False
Old shape (Rectangle(5, 4)) is new shape(Rectangle(5, 4)): False
Old shape (Rectangle(3, 3)) is new shape(Rectangle(3, 3)): False
Old shape (Square(5)) is new shape(Square(5)): False
'''