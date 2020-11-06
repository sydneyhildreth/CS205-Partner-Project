import Hiker
import Trail
import HikingLog

class Demo:
    def __init__(self, hikingLog):
        self.hikingLog = hikingLog

    def startDemo(self):

        #create hiker and trail
        hiker1 = Hiker.Hiker('Sydney')
        trailName1 = 'Mt. Mansfield'
        trail1 = Trail.Trail(trailName1, 'Stowe', "2.3", "1")
        hiker1.addStatus(trail1)

        #add trail and hiker name to hikingLog
        self.hikingLog.addHiker(hiker1)
        self.hikingLog.addTrail(trail1)

        #add the stats
        self.hikingLog.updateStatus(hiker1, trail1)

        # TODO: seems like the updateStatus does not work
        print(self.hikingLog.getStatus(hiker1))

        #print out to ensure it adds correct
        print(hiker1.toString())
        print(trail1.toString())

        # TODO: toString() for Status
        print(self.hikingLog.updateStatus(hiker1, trail1))

        # TODO: toString() for HikingLog
        print(HikingLog.HikingLog().get())


















