from unittest import TestCase, main
from task2 import Shape, Triangle, Circle


class UnitTest(TestCase):

    def setUp(self):
        self.rectangle = Shape(2, 4) # прямоугольник со сторонами 2 и 4
        self.square = Shape(4, 4) # квадрат (прямоугольник) со сторонами 4 и 4
        self.triangle = Triangle(3, 4, 5)
        self.circle = Circle(10)

    def test_quadrilateral(self):
        self.assertEqual(self.rectangle.area, 8)
        self.assertEqual(self.square.area, 16)

    def test_other(self):
        self.assertEqual(self.triangle.area, 6)
        self.assertEqual(self.circle.area, 314.16)


if __name__ == '__main__':
    main()