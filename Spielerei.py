from abc import ABC

class Ops(ABC):
    def do_ops(self):
        pass

class Addition(Ops):
    def do_ops(self):
        pass

class Subtraction(Ops):
    def do_ops(self):
        pass

class Multiplication(Ops):
    def do_ops(self):
        pass

class Division(Ops):
    def do_ops(self):
        pass

class AbstractFactory:
    pass

class ConcreteFactory(AbstractFactory):
    _created_operators = []

    def __init__(self):
        self.operators = {"plus" : "Addition",
                          "+" : "Addition",
                          "-" : "Subtraction",
                          "minus" : "Subtraction",
                          "*" : "Multiplication",
                          "times" : "Multiplication",
                          ":" : "Division",
                          "divide" : "Division"}

        for o in set(self.operators.values()):
            self._created_operators.append((o, eval(o)()))
            #print(self._created_operators)

if __name__ == '__main__':
    fac = ConcreteFactory()




