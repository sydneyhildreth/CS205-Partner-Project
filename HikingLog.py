import Status

class HikingLog:
    hikingLog = None

    def get(self):
        if self.hikingLog is None:
            self.hikingLog = HikingLog()
        return self.hikingLog


    def getHiker(self):
        return self.hikers

    def getTrail(self):
        return self.trails

    def getStatus(self, hiker):
        trailsHiked = []
        for x in self.status:
            if x.getHiker() == hiker:
                trailsHiked.append(x.getTrail().toString())
        return trailsHiked

    def __init__(self):
        self.hikers = set()
        self.trails = set()
        self.status = set()

    def addHiker(self, Hiker):
        self.hikers.add(Hiker)

    def addTrail(self, Trail):
        self.trails.add(Trail)

    def hasBeenHiked(self, trail):
        for x in self.status:
            if x.getTrail == trail:
                return True
            return False

    def updateStatus(self, hiker, trail):
        if not self.hasBeenHiked(trail):
            x = Status.Status(hiker, trail)
            self.status.add(x)
            hiker.addStatus(trail)
            return x
        else:
            return None

    def showStatus(self):
        for x in self.status:
            s=x.getHiker().toString() + " " + x.getTrail().toString()
            print(s)
