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

        # check that the book checked out to john is book1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1.toString())

        # check that john shows one book checked out
        trails = self.sid.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the book checked out to john is book1
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail1)


    def testStatusTwo(self):
        print('testStatusTwo()')
        # check out a different book to mary
        s = self.HikingLog.updateStatus(self.syd, self.trail2)
        self.assertIsNotNone(s)

        # check that the library shows one book checked out to mary
        trails = self.HikingLog.getStatus(self.syd)
        self.assertEqual(len(trails), 1)

        # check that the book checked out to mary is book2
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail2.toString())

        # check that mary shows one book checked out
        trails = self.syd.getStatus()
        self.assertEqual(len(trails), 1)

        # check that the book checked out to mary is book2
        if len(trails) == 1:
            self.assertEqual(trails[0], self.trail2)


if __name__ == "__main__":
  unittest.main()

