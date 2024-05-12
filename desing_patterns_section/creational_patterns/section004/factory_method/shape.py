from abc import ABC, abstractmethod


# Interface para a forma geométrica
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Implementação concreta para um círculo
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


# Implementação concreta para um quadrado
class Square(Shape):
    def draw(self):
        print("Drawing a square")


# Factory Method na classe abstrata
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self) -> Shape:
        pass


# Factory Method concreto para criar círculos
class CircleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Circle()


# Factory Method concreto para criar quadrados
class SquareFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Square()


# Cliente usando Factory Method
if __name__ == '__main__':
    circle_factory = CircleFactory()
    square_factory = SquareFactory()

    circle = circle_factory.create_shape()
    square = square_factory.create_shape()

    circle.draw()
    square.draw()
