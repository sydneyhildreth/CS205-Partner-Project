import Hiker
import Trail
import HikingLog

class Demo:
    def __init__(self, HikingLog):
        self.HikingLog = HikingLog

    def startDemo(self):

        #---------------HIKER 1 -----------------------------------#

        hiker1 = Hiker.Hiker('Sydney')
        trail1 = Trail.Trail('Mt. Mansfield', 'Stowe', "2.3 miles", "1")
        trail3 = Trail.Trail('Hamilton Falls', 'Jamaica', "1.5 miles", "3")

        # add trail and hiker name to hikingLog
        self.HikingLog.addHiker(hiker1)
        self.HikingLog.addTrail(trail1)
        self.HikingLog.addTrail(trail3)

        #add the status for hiker 1
        self.HikingLog.updateStatus(hiker1, trail1)
        self.HikingLog.updateStatus(hiker1, trail3)

        # ---------------HIKER 2 -----------------------------------#

        hiker2 = Hiker.Hiker('Sid')
        trailName2 = 'Mt. Pisgah'
        trail2 = Trail.Trail(trailName2, 'Westmore', "1,500 ft", "2")

        # add trail and hiker name to hikingLog
        self.HikingLog.addHiker(hiker2)
        self.HikingLog.addTrail(trail2)

        # add the status for hiker
        self.HikingLog.updateStatus(hiker2, trail2)




        #print out to ensure it adds correct
        print("------------Hiker 1-----------------")
        print(hiker1.toString())
        print("Trail 1 Info: ", trail1.toString())
        # displays all the trail from one hiker
        print("Get Status Hiker 1: ", self.HikingLog.getStatus(hiker1))

        print("")
        print("------------Hiker 2-----------------")
        print(hiker2.toString())
        print("Trail 2 Info: ", trail1.toString())
        print("Get Status Hiker 2: ", self.HikingLog.getStatus(hiker2))

        print("")
        print("--------Show Full Hiking Log---------")

        print(self.HikingLog.showHikingLog())

        print("")
        print("Loading Hiker 1...")
        hikerToFind = self.HikingLog.findHiker(1)
        if hikerToFind is not None:
            trails = self.HikingLog.getStatus(hikerToFind)
            if len(trails) > 0:
                print("Trails Hiked: " ,self.HikingLog.getStatus(hikerToFind))
            else:
                print(None)
        else:
            print("Hiker 1 does not seem to be in the system..")

        print("")
        print("Loading Hiker 2...")
        hikerToFind = self.HikingLog.findHiker(2)
        if hikerToFind is not None:
            trails = self.HikingLog.getStatus(hikerToFind)
            if len(trails) > 0:
                print("Trails Hiked: ", self.HikingLog.getStatus(hikerToFind))
            else:
                print(None)
        else:
            print("Hiker 2 does not seem to be in the system..")





















