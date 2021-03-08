class House:
    def __init__(self):
        self.kitchen = None
        self.bathroom = None
        self.toilet = None
        self.living_room = None

    def __str__(self):
        return f"{self.kitchen, self.bathroom, self.toilet, self.living_room}"

class AbstractHouseBuilder:
    def __init__(self):
        self.house = None

    def createHouse(self):
        self.house = House()

class LuxuryHouseBuilder(AbstractHouseBuilder):
    def addKitchen(self):
        self.house.kitchen = "Luxury kitchen"

    def addBathroom(self):
        self.house.bathroom = "Luxury bathroom"

    def addToilet(self):
        self.house.toilet = "Luxury toilet"

    def addLivingRoom(self):
        self.house.living_room = "Luxury living room"

class Director:
    def __init__(self, builder):
        self.builder = builder

    def constructHouse(self):
        self.builder.createHouse()
        self.builder.addKitchen()
        self.builder.addBathroom()
        self.builder.addToilet()
        self.builder.addLivingRoom()

    def getHouse(self):
        return self.builder.house

if __name__ == '__main__':
    LuxuryHouseBuilder = LuxuryHouseBuilder()
    director = Director(LuxuryHouseBuilder)


    director.constructHouse()
    HouseOne = director.getHouse()
    print(HouseOne)


