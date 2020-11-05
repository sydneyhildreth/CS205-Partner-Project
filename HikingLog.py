import Status

class HikingLog:
    hikingLog = None

    def get(self):
        if self.hikingLog is None:
            self.hikingLog = HikingLog()
        return self.hikingLog



    def getHiker(self):
        return self.hikers

    def getTrailf(self):
        return self.trails

    def getStatus(self, hiker):
        trailsHiked = []
        for x in self.Status:
            if x.getHiker == hiker:
                trailsHiked.append(x.getHiker)

    def __init__(self):
        self.hikers = set()
        self.trails = set()
        self.Status = set()

    def addHiker(self, Hiker):
        self.hikers.add(Hiker)

    def addTrail(self, Trail):
        self.trails.add(Trail)

    def hasBeenHiked(self, trail):
        for x in self.status:
            if x.getTrail() == trail:
                return True
            else:
                return False

    def updateStatus(self, hiker, trail):
        if not self.hasBeenHiked(trail):
            hiked = Status.Status(hiker, trail)
            self.status.add(hiked)
            hiker.updateStatus(trail)
            return hiked
        else:
            return None
