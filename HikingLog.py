import Status

class HikingLog:
    hikingLog = None

    @classmethod
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

    def findHiker(self, id):
        for hiker in self.hikers:
            if hiker.getId() == id:
                return hiker
        return None


    def hasBeenHiked(self, trail):
        for t in self.status:
            if t.getTrail() == trail:
                return True
        return False


    def updateStatus(self, hiker, trail):
        #print(self.hasBeenHiked(trail))
        if not self.hasBeenHiked(trail):
            x = Status.Status(hiker, trail)
            self.status.add(x)
            hiker.addStatus(trail)
            return x
        else:
            print("Oops looks like you have already hiked this.")
            return None

    #Made a mistake by adding trail to hiker only and not hiker and status list
    def updateStatusWrong(self, hiker, trail):
        if not self.hasBeenHiked(trail):
            x = Status.Status(hiker, trail)
            hiker.addStatus(trail)
            return x
        else:
            print("Oops looks like you have already hiked this.")
            return None


    def showHikingLog(self):
        for x in self.status:
            s = x.getHiker().toString() + ' => ' + x.getTrail().toString()
            print(s)

    def whoHikedTrail(self, trail):
        hiker = []
        for x in self.status:
            if x.getTrail() == trail:
                s = x.getHiker().getName()
                hiker.append(s)

        return hiker

