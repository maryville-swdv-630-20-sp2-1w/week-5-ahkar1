from __future__ import generators
from __future__ import annotations

import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")



class Facade:
  

    def __init__(self, paper1: Paper1, paper2: Paperm2) -> None:
       

        self._paper1 = paper1 or Paper1()
        self._paper2 = paper2 or Paper2()

    def operation(self) -> str:
        

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._paper1.operation1())
        results.append(self._paper2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._paper1.operation_n())
        results.append(self._paper2.operation_z())
        return "\n".join(results)


class Paper1:
    

    def operation1(self) -> str:
        return "Paper1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Paper1: Draw!"


class Paper2:
   

    def operation1(self) -> str:
        return "Paper2: Get ready!"

   

    def operation_z(self) -> str:
        return "Paper2: Draw!"


def client_code(facade: Facade) -> None:
   

    print(facade.operation(), end="")


class SingletonMeta(type):

    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        
        return "Shapes"
    # ...



# Implement shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

def main():
    shapes = [ Shape.factory(i) for i in shapeNameGen(3)]
#Factory Pattern
    for shape in shapes:
        shape.draw()
        shape.erase()
#Facade Pattern
    paper1 = Paper1()
    paper2 = Paper2()
    facade = Facade(paper1, paper2)
    client_code(facade)
    
#Singleton Pattern
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
main()