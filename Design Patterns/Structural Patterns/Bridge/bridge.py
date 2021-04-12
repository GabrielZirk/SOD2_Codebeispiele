# Circles and squares
# Each can be rendered in vector or raster form
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass
    def render_square(self, lenght):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, length):
        print(f'Drawing a square of length {length}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')

    def render_square(self, length):
        print(f'Drawing pixels for square of length {length}')


class Shape():
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer, length):
        super().__init__(renderer)
        self.length = length

    def draw(self):
        self.renderer.render_square(self.length)

    def resize(self, factor):
        self.length *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(6)
    circle.draw()