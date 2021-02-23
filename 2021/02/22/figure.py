class Figure(object):

    def __init__(self, dots, height, width):
        self.dots = dots
        self.height = height
        self.width = width

    def calcArea(self):
        pass


class Line(Figure):

    def __init__(self, dots, height, width):
        super().__init__(dots, height, width)
        if dots != 2:
            raise AssertionError('line has two points')

    def calcArea(self):
        return 0


class Triangle(Figure):

    def __init__(self, dots, height, width):
        super().__init__(dots, height, width)
        if dots != 3:
            raise AssertionError('triangle has three points')

    def calcArea(self):
        return self.height * self.width / 2


class Rectangle(Figure):

    def __init__(self, dots, height, width):
        super().__init__(dots, height, width)
        if dots != 4:
            raise AssertionError('rectangle has four points')

    def calcArea(self):
        return self.height * self.width


line = Line(2, 4, 0)
triangle = Triangle(3, 4, 2)
rectangle = Rectangle(4, 4, 2)

print(
    'line의 점의 갯수: %.0d, line의 넓이: %.0d'
    % (line.dots, line.calcArea())
)
print(
    'triangle의 점의 갯수: %.0d, triangle의 넓이: %.0d'
    % (triangle.dots, triangle.calcArea())
)
print(
    'rectangle의 점의 갯수: %.0d, rectangle의 넓이: %.0d'
    % (rectangle.dots, rectangle.calcArea())
)
