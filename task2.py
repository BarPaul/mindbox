"""
Напиши на Python библиотеку для поставки внешним клиентам вычислений: 
1. Площадь круга по радиусу
2. Площадь треугольника по трем сторонам. 
Дополнительно к работоспособности оценим: 
1. юнит-тесты
2. легкость добавления других фигур
3. вычисление площади фигуры без знания типа фигуры в compile-time
4. проверку на то, является ли треугольник прямоугольным.
"""
from math import pi, sqrt

def _send_exception(message: str) -> ValueError:
    return ValueError(f"Incorrect values!\nExcepted: {message}")

class Shape:

    def __init__(self, *_sides: tuple[float | int]):
        self._sides = _sides
        self._check_shape()
        self.area = round(self._get_area(), 2)

    def _get_area(self) -> float | int:
        __answer = 1
        for __side in self._sides:
            __answer *= __side
        return __answer

    def _check_shape(self):
        if len(self._sides) < 1 or any(not isinstance(side, float | int) or side <= 0 for side in self._sides):
            raise _send_exception("float/int positive arguments")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with sides {self._sides}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._sides}"


class Circle(Shape):
    def _get_area(self) -> float:
        return pi * self._sides[0] ** 2

    def _check_shape(self):
        if len(self._sides) != 1 or not isinstance(self._sides[0], float | int) or self._sides[0] <= 0:
            raise _send_exception("one float/int positive argument")

class Triangle(Shape):

    def _get_area(self):
        try:
            return sqrt(self.__p * (self.__p - self.__a) * (self.__p - self.__b) * (self.__p - self.__c))
        except ValueError:
            raise _send_exception("Triangle with possible sides")


    def _check_shape(self):
        if len(self._sides) != 3 or any(not isinstance(side, float | int) or side <= 0 for side in self._sides):
            raise _send_exception("3 float | int positive arguments")
        self.__a, self.__b, self.__c = sorted(self._sides)
        self.__p = sum(self._sides) / 2
        self.is_square: bool = self.__a ** 2 + self.__b ** 2 == self.__c ** 2

triangle = Triangle(3, 5, 4)
