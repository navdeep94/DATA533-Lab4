from realestate.familyhome import areatype
import unittest

class TestAreaType(unittest.TestCase):
    
    def setUp(self):
        self.o1 = areatype.AreaType('1', 'low', '1')
        self.o2 = areatype.AreaType('2', 'high', '2')
        self.o3 = areatype.AreaType('3 or more', 'medium', '3')
        self.o4 = areatype.AreaType('2', 'low', '3')
        self.o5 = areatype.AreaType('1', 'low', '1')
        print("Set Up")

    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    def test_nearby_amenities(self):
        self.assertEqual(areatype.AreaType.nearby_amenities(self.o1), 'Hospital, Park, Shopping Center, School, and a Mall')
        self.assertEqual(areatype.AreaType.nearby_amenities(self.o2), 'Hospital, Park, Shopping Center, and a School')
        self.assertEqual(areatype.AreaType.nearby_amenities(self.o3), 'Hospital, Park, Shopping Center, School, Mall, Library, Beach, and a Cafe')
        self.assertEqual(areatype.AreaType.nearby_amenities(self.o4), 'Hospital, Park, Shopping Center, and a School')
        self.assertEqual(areatype.AreaType.nearby_amenities(self.o5), 'Hospital, Park, Shopping Center, School, and a Mall')
        
    def test_view(self): 
        self.assertEqual(areatype.AreaType.view(self.o1), 'Normal view, park facing, or sea facing')
        self.assertEqual(areatype.AreaType.view(self.o2), 'Normal View or Park facing')
        self.assertEqual(areatype.AreaType.view(self.o3), 'Normal view, park facing, sea facing, or sun facing')
        self.assertEqual(areatype.AreaType.view(self.o4), 'Normal View or Park facing')
        self.assertEqual(areatype.AreaType.view(self.o5), 'Normal view, park facing, or sea facing')

    def test_population(self): 
        self.assertEqual(areatype.AreaType.population(self.o1), 'highly populated')
        self.assertEqual(areatype.AreaType.population(self.o2), 'average population around')
        self.assertEqual(areatype.AreaType.population(self.o3), 'very less population')
        self.assertEqual(areatype.AreaType.population(self.o4), 'average population around')
        self.assertEqual(areatype.AreaType.population(self.o5), 'highly populated')        

    def tearDown(self):
        print("Tear Down")
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')    
        
unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite(): 
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAreaType))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
