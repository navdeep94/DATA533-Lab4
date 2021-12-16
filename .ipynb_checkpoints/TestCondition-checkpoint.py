# Class for building Test Cases for Condition module, functions also including setUp,setUpClass,tearDown,tearDownClass
from realestate.apartment import Condition
import unittest

class TestCondition(unittest.TestCase):
    def setUp(self):
        self.conditionAge1 = Condition.Condition('0-3')
        self.conditionAge2 = Condition.Condition('3-5')
        print("Set up")
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        
    def tearDown(self):
        print("Tear Down")

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def test_apartment_maintenance(self): # test case
        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')
        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')
        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge2), 'Required')
        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge2), 'Required')
        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')
        print("Test Cases for Apartment Maintenance Executed")
        
        
    def test_apartment_discount(self): # test case
        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')
        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge1), '0-5%')
        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')
        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge1), '0-5%')
        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')
        print("Test Cases for Apartment Discount Executed")
        
        
    def test_apartment_furnishing_status(self): # test case
        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')
        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge2), 'Semi Furnished')
        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')
        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge2), 'Semi Furnished')
        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')
        print("Test Cases for Apartment Furnishing Status Executed")
        
        
unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCondition))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
