import HikingLog
import Hiker
import Trail
import unittest

class testStatus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')
        cls.HikingLog = HikingLog.HikingLog().get()
        trail1Name = 'Mt. Mansfield'
        trail2Name = 'Mt. Pisgah'
        trail3Name = 'Hamilton Falls'
        trail1Location = 'Stowe'
        trail2Location = 'Westmore'
        trail3Location = 'Jamaica'
        trail1Elevation = "2.3 miles"
        trail2Elevation = "1,500ft"
        trail3Elevation = "1.5miles"
        trail1Rank = 1
        trail2Rank = 3
        trail3Rank = 2

        cls.trail1 = Trail.Trail(trail1Name, trail1Location, trail1Elevation, trail1Rank)
        cls.trail2 = Trail.Trail(trail2Name, trail2Location, trail2Elevation, trail2Rank)
        cls.trail3 = Trail.Trail(trail3Name, trail3Location, trail3Elevation, trail3Rank)

        cls.sid = Hiker.Hiker('Sid')
        cls.syd = Hiker.Hiker('Syd')
        cls.sydney = Hiker.Hiker('Sydney')

        cls.HikingLog.addTrail(cls.trail1)
        cls.HikingLog.addTrail(cls.trail2)
        cls.HikingLog.addTrail(cls.trail3)

        cls.HikingLog.addHiker(cls.sid)
        cls.HikingLog.addHiker(cls.syd)

    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')


    def setUp(self):
        # called before every test
        print('setUp()')


    def tearDown(self):
        # called after every test
        print('tearDown()')


    # This test calls the correct implementation of our member function
    def testStatusOne(self):
        print('testStatusone()')
        # check that the Hiking Log shows that no trails are hiked by Sid
        trails = self.HikingLog.getStatus(self.sid)
        self.assertEqual(len(trails), 0)

        # Update Status for Sid
        x = self.HikingLog.updateStatus(self.sid, self.trail1)

        # check that the Hiking Log shows one trail hiked by Sid
        trails = self.HikingLog.getStatus(self.sid)
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by sid is trail1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1.toString())

        # check that sid has hiked only one trail so far
        trails = self.sid.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by sid is trail1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1)


    # This test calls the wrong implementation of our member function
    def testStatusWrong(self):
        print('testStatusWrong()')
        # check that the Hiking Log shows that no trails are hiked by Sid
        trails = self.HikingLog.getStatus(self.sid)
        self.assertEqual(len(trails), 1)

        # Update Status for Sid
        x = self.HikingLog.updateStatusWrong(self.sid, self.trail1)

        # check that the Hiking Log shows one trail hiked by Sid
        trails = self.HikingLog.getStatus(self.sid)
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by sid is trail1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1.toString())

        # check that sid has hiked only one trail so far
        trails = self.sid.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by sid is trail1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1)


    # This is another test for our member function and it tests most of our member function
    def testStatusTwo(self):
        print('testStatusTwo()')
        # let syd hike a different trail and accordingly update status for syd
        s = self.HikingLog.updateStatus(self.syd, self.trail2)
        self.assertIsNotNone(s)

        # check that the hiking log shows that syd has only hiked one trail so far
        trails = self.HikingLog.getStatus(self.syd)
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by syd is trail2
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail2.toString())

        # check that syd has only hiked one trail so far
        trails = self.syd.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by syd is trail2
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail2)

        # add same trail to hiker syd to make sure that it is not being repeated(saved as a different trail although
        # it is the same trail) in the hiking log
        self.HikingLog.updateStatus(self.syd, self.trail2)

        #check to see that syd has only hiked one trail so far
        t = self.HikingLog.getStatus(self.syd)
        self.assertEqual(len(t), 1)

        # check to see that the trail hiked by syd is trail2
        if len(t) == 1:
            self.assertEqual(t[0], self.trail2.toString())

        # check that syd has only hiked one trail so far meaning the trail is not being repeated when we update status
        trails = self.syd.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the trail hiked by syd is trail2
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail2)


    # This test tests whoHasHiked function
    def testWhoHasHiked(self):
        # update that hiker Sydney has hiked trail3 in the hiking log
        self.HikingLog.updateStatus(self.sydney, self.trail3)

        # check to see that trail3 has been hiked only by Sydney so far
        self.assertEqual(self.HikingLog.whoHikedTrail(self.trail3), [self.sydney.getName()])


if __name__ == "__main__":
  unittest.main()

