class Car():
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.speedometer = None
        self.make = None

    def __str__(self):
        return f"{self.wheels} | {self.engine} | {self.speedometer} | {self.make}"

class CarBuilder():
    def __init__(self):
        self.car = Car()

    def build(self):
        return self.car

class CarEngineBuilder(CarBuilder):
    def addEngine(self, enginetype):
        self.car.engine = enginetype
        return self

class CarWheelsBuilder(CarEngineBuilder):
    def addWheels(self, wheels):
        self.car.wheels = wheels
        return self

class CarSpeedometerBuilder(CarWheelsBuilder):
    def addSpeedometer(self, speedometer):
        self.car.speedometer = speedometer
        return self

class CarMakeBuilder(CarSpeedometerBuilder):
    def addMake(self, make):
        self.car.make = make
        return self

if __name__ == '__main__':
    car = CarMakeBuilder()
    car_ready = car.addMake("Nissan").addSpeedometer("0-150").addEngine("4Stroke").addWheels("4Wheels").build()
    print(car_ready)


