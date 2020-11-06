
class Hiker:
    numHiker = 0
    def __init__(self, name):
        self.name = name
        Hiker.numHiker = Hiker.numHiker + 1
        self.id = Hiker.numHiker
        self.status = set()


    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def toString(self):
        s = "Hiker Name: " + self.name + ", id = " + str(self.id) + ", Number of Trails Hiked: " + str(len(self.status))
        return s

    def addStatus(self, trail):
        self.status.add(trail)

    def getStatus(self):
        return list(self.status)






    