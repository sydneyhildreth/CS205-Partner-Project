
class Hiker:
    def __init__(self, id, name):
        Hiker.nextHiker = Hiker.nextHiker + 1
        self.id =Hiker.nextHiker
        self.name = name
        self.status = set()


    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def toString(self):
        s = "Hiker Name: " + self.name + "id = " + self.id + "Number of Trails Hiked: " + str(len(self.status))
        return s

    def addStatus(self, trail):
        self.status.add(trail)

    def getStatus(self):
        return list(self.status)






    