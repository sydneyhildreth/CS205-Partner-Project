
class Trail:
    def __init__(self, name, location, elevation, rank):
        self.name = name
        self.location = location
        self.elevation = elevation
        self.rank = rank

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getElevation(self):
        return self.elevation

    def getRank(self):
        return self.rank

    def setName(self, name):
        self.name = name

    def setLocation(self, location):
        self.location = location

    def setElevation(self, elevation):
        self.elevation = elevation

    def setRank(self, rank):
        self.rank = rank

    def toString(self):
        s = self.name + ", " + self.location + ", " + self.elevation + ", " + self.rank
        return s
