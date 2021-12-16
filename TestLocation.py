## Class for building Test Cases for Location module, functions also including setUp,setUpClass,tearDown,tearDownClass
from realestate.apartment import Location
import unittest

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.location_usa = Location.Location('USA')
        self.location_canada = Location.Location('CANADA')
        self.location_uk = Location.Location('UK')
        print("Set up")
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        
    def tearDown(self):
        print("Tear Down")

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def test_apartment_cities(self): # test case
        self.assertEqual(Location.Location.apartment_cities(self.location_usa), ['Chicago','Seattle','New York','Boston'])
        self.assertEqual(Location.Location.apartment_cities(self.location_usa), ['Chicago','Seattle','New York','Boston'])
        self.assertEqual(Location.Location.apartment_cities(self.location_uk), ['London','Birmighan','Leeds','Southampton'])
        self.assertEqual(Location.Location.apartment_cities(self.location_canada), ['Vancouver','Kelowna','Montreal','Toronto'])
        self.assertEqual(Location.Location.apartment_cities(self.location_uk), ['London','Birmighan','Leeds','Southampton'])
        print("Test Cases for Apartment Cities Executed")
        
        
    def test_apartment_locality(self): # test case
        self.assertEqual(Location.Location.apartment_locality(self.location_usa), ['Charles Street','Brown Road','Morgan Highway','Alpine Park'])
        self.assertEqual(Location.Location.apartment_locality(self.location_canada), ['English Bay','Glenmore','Concordia Street','Robson Park'])
        self.assertEqual(Location.Location.apartment_locality(self.location_uk), ['Smith Rd','James Arthur Mall','Michelle Street','Captain James Edward Road'])
        self.assertEqual(Location.Location.apartment_locality(self.location_canada), ['English Bay','Glenmore','Concordia Street','Robson Park'])
        self.assertEqual(Location.Location.apartment_locality(self.location_usa), ['Charles Street','Brown Road','Morgan Highway','Alpine Park'])
        print("Test Cases for Apartment Locality Executed")
        
        
        
    def test_apartment_facing_direction(self): # test case
        self.assertEqual(Location.Location.apartment_facing_direction(self.location_uk), ['North West','South','South West','East'])
        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])
        self.assertEqual(Location.Location.apartment_facing_direction(self.location_canada), ['South West','North','West','South East'])
        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])
        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])
        print("Test Cases for Apartment Facing Direction Executed")

unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestLocation))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
