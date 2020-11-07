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

        # displays all the trail from one hiker
        print("Hiker 1 Trails: ", self.HikingLog.getStatus(hiker1))

        print("")
        print("------------Hiker 2-----------------")
        print(hiker2.toString())
        print("Hiker 2 Trails: ", self.HikingLog.getStatus(hiker2))

        print("")
        print("--------Show Full Hiking Log---------")

        print(self.HikingLog.showHikingLog())

        print("")
        print("Loading Hiker 1...")
        hikerToFind = self.HikingLog.findHiker(1)
        if hikerToFind is not None:
            trails = self.HikingLog.getStatus(hikerToFind)
            print("Looking for trails hiked by", hikerToFind.getName(), "...")
            if len(trails) > 0:

                print("Trails Hiked: " ,self.HikingLog.getStatus(hikerToFind))
                print("                         ---------------------------------")

            else:
                print("Looks like ", hikerToFind.getName(), " hasn't hiked any trails yet.")
            print(hikerToFind.getName(),"recently hiked Camel's Hump in Waterbury, VT. It is 4000ft high and "
                  "she ranks it at 1.")
            print("Updating Records....")
            trail3 = Trail.Trail("Camel's Hump", "Waterbury", "4,000 ft", "1")

            # add trail and hiker name to hikingLog
            self.HikingLog.addTrail(trail3)
            # add the status for hiker
            self.HikingLog.updateStatus(hiker1, trail3)
            print("Updated Trails for", hikerToFind.getName(), ":", self.HikingLog.getStatus(hikerToFind))



        else:
            print("Hiker 1 does not seem to be in the system..")

        print("")
        print("Loading Hiker 2...")
        hikerToFind = self.HikingLog.findHiker(2)
        if hikerToFind is not None:
            trails = self.HikingLog.getStatus(hikerToFind)
            print("Looking for trails hiked by", hikerToFind.getName(), "...")
            if len(trails) > 0:

                print("Trails Hiked: " ,self.HikingLog.getStatus(hikerToFind))
                print("                         ---------------------------------")
            else:
                print("Looks like ", hikerToFind.getName(), " hasn't hiked any trails yet.")

            print("")

            print(hikerToFind.getName(), "recently hiked Cantilever Rock in Underhill Center, VT. It is 2 miles long and "
                                         "he ranks it at 3.")
            print("Updating Records....")
            trail4 = Trail.Trail("Cantilever Rock", "Underhill Center", "2 miles", "3")

            # add trail and hiker name to hikingLog
            self.HikingLog.addTrail(trail4)
            # add the status for hiker
            self.HikingLog.updateStatus(hiker2, trail4)
            print("Updated Trails for", hikerToFind.getName(), ":", self.HikingLog.getStatus(hikerToFind))



        else:
            print("Hiker 2 does not seem to be in the system..")
