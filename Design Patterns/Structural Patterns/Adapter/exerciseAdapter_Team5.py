

# Sie erhalten eine Klasse namens Square und eine Funktion calculate_area(), die
# die Fläche eines bestimmten Rechtecks berechnet
# Um Square in calculate_area zu verwenden (anstatt es mit width/hight Attributen zu erweitern)
#  implementieren Sie bitte die SquareToRectangleAdapter-Klasse
# Dieser Adapter nimmt ein square Objekt und passt es so an, dass es als Argument für calculate_area()
# verwendet werden kann
#

from unittest import TestCase

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.obj = square

    @property
    def width(self):
        return self.obj.side

    @property
    def height(self):
        return self.obj.side

# if __name__ == '__main__':
#     sq = Square(10)
#     adapter = SquareToRectangleAdapter(sq)
#     print(adapter.width)
#     sq.side = 11
#     print(adapter.width)


class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))
