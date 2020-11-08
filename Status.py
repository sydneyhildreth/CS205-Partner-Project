import Hiker
import Trail

class Status:
    def __init__(self, hiker, trail):
        self.hiker = hiker
        self.trail = trail

    def getHiker(self):
        return self.hiker

    def getTrail(self):
        return self.trail

    def setHiker(self, hiker):
        self.hiker = hiker

    def setTrail(self, trail):
        self.trail = trail

