
class Building:
    def __init__(self, numberOfFloors, buildingType ):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, numberOfFloors, buildingType):
        return self.numberOfFloors == self.buildingType

b1 = Building(1, "дом")
b2 = Building(1, "дом")
b3 = Building(2, "дом")

print(b1.buildingType == b2.buildingType)
print(b1.numberOfFloors == b3.numberOfFloors)



#class Building:
#    def __init__(self, numberOfFloors, buildingType ):
#        self.numberOfFloors = numberOfFloors
#        self.buildingType = buildingType
#    def __eq__(self, numberOfFloors, buildingType):
#            return self.numberOfFloors == self.buildingType


#b1 = Building(1, "house")
#b2 = Building(3, "house")
#print(b1 == b2)
