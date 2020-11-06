import Hiker
import Trail

class Status:
    def __init__(self, Hiker, Trail):
        self.Hiker = Hiker
        self.Trail = Trail

    def getHiker(self):
        return self.Hiker

    def getTrail(self):
        return self.Trail

