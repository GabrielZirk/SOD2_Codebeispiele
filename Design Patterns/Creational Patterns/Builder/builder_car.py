class Car:
    def __init__(self):
        self.engine = None
        self.tyres = None
        self.speedometer = None
        self.make = None

    def __str__(self):
        return '{}|{}|{}|{}'.format(self.engine, self.tyres, self.speedometer, self.make)

class Engine:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

class Tyres:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

class Speedometer:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

class AbstractBuilder:
    def __init__(self):
        self.car = None
    def createNewCar(self):
        self.car = Car()

class ConcreteBuilder(AbstractBuilder):
    def addEngine(self, engine):
        self.car.engine = Engine(engine)

    def addTyres(self,tyres):
        self.car.tyres = Tyres(tyres)

    def addSpeedometer(self, speedometer):
        self.car.speedometer = Speedometer(speedometer)

    def addMake(self, make):
        self.car.make = make

class Director:
    def __init__(self, builder):
        self._builder = builder

    def constructCar(self, engine, tyres, speedometer, make):
        self._builder.createNewCar()
        self._builder.addEngine(engine)
        self._builder.addTyres(tyres)
        self._builder.addSpeedometer(speedometer)
        self._builder.addMake(make)

    def getCar(self):
        return self._builder.car

if __name__ == '__main__':
    CarBuilder = ConcreteBuilder()
    Director = Director(CarBuilder)

    Director.constructCar("4-stroke", "Ceat", "0-160", "Nissan")
    CarOne = Director.getCar()
    print("Details of CarOne", CarOne)

