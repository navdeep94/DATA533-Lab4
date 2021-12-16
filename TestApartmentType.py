## Class for building Test Cases for ApartmentType module, functions also including setUp,setUpClass,tearDown,tearDownClass
from realestate.apartment import Feature
import unittest

class TestApartmentType(unittest.TestCase):
    def setUp(self):
        self.apartmentType1 = Feature.Features('1BHK')
        self.apartmentType2 = Feature.Features('2BHK')
        self.apartmentType3 = Feature.Features('3BHK')
        print("Set up")
        
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        
    def tearDown(self):
        print("Tear Down")

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

        
    def test_apartment_area(self): # test case
        self.assertEqual(Feature.Features.apartment_area(self.apartmentType1), '500 - 800 sqft')
        self.assertEqual(Feature.Features.apartment_area(self.apartmentType2), '800 - 1100 sqft')
        self.assertEqual(Feature.Features.apartment_area(self.apartmentType2), '800 - 1100 sqft')
        self.assertEqual(Feature.Features.apartment_area(self.apartmentType1), '500 - 800 sqft')
        self.assertEqual(Feature.Features.apartment_area(self.apartmentType3), '1100 - 1500 sqft')
        print("Test Cases for Apartment Area Executed")
        
    def test_apartment_price(self): # test case
        self.assertEqual(Feature.Features.apartment_price(self.apartmentType1), '150000 - 200000 CAD')
        self.assertEqual(Feature.Features.apartment_price(self.apartmentType2), '250000 - 300000 CAD')
        self.assertEqual(Feature.Features.apartment_price(self.apartmentType2), '250000 - 300000 CAD')
        self.assertEqual(Feature.Features.apartment_price(self.apartmentType1), '150000 - 200000 CAD')
        self.assertEqual(Feature.Features.apartment_price(self.apartmentType3), '350000 - 400000 CAD')
        print("Test Cases for Apartment Price Executed")
        
    def test_apartment_floors(self): # test case
        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType1), [2, 3, 7, 11, 13])
        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType2), [1, 4, 5, 8, 10])
        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType2), [1, 4, 5, 8, 10])
        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType1), [2, 3, 7, 11, 13])
        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType3), [6, 9, 12, 14, 15])
        print("Test Cases for Apartment Floors Executed")
        
unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestApartmentType))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
