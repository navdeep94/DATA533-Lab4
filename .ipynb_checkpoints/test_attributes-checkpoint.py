# Attributes test
from realestate.familyhome import attributes
import unittest
class TestAttributes(unittest.TestCase):
    
    def setUp(self):
        self.o1 = attributes.Characteristics('1', 'low', '1')
        self.o2 = attributes.Characteristics('2', 'high', '2')
        self.o3 = attributes.Characteristics('3 or more', 'medium', '3')
        self.o4 = attributes.Characteristics('2', 'low', '3')
        self.o5 = attributes.Characteristics('1', 'low', '1')
        self.p1 = attributes.Quality('1', 'low', '1')
        self.p2 = attributes.Quality('2', 'high', '2')
        self.p3 = attributes.Quality('3 or more', 'medium', '3')
        self.p4 = attributes.Characteristics('2', 'low', '3')
        self.p5 = attributes.Quality('1', 'low', '1')
        print("Set Up")
        
   
      
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
       
    def test_house_price(self): 
        self.assertEqual(attributes.Characteristics.house_price(self.o1), '500000-600000')
        self.assertEqual(attributes.Characteristics.house_price(self.o2), '600000-700000')
        self.assertEqual(attributes.Characteristics.house_price(self.o3), '700000-800000')
        self.assertEqual(attributes.Characteristics.house_price(self.o4), '600000-700000')
        self.assertEqual(attributes.Characteristics.house_price(self.o5), '500000-600000')
               
    def test_house_area(self): 
        self.assertEqual(attributes.Characteristics.house_area(self.o1), '1400 sq. ft')
        self.assertEqual(attributes.Characteristics.house_area(self.o2), '1600 sq. ft')
        self.assertEqual(attributes.Characteristics.house_area(self.o3), '1800 sq. ft')
        self.assertEqual(attributes.Characteristics.house_area(self.o4), '1600 sq. ft')
        self.assertEqual(attributes.Characteristics.house_area(self.o5), '1400 sq. ft')            

    def test_build_quality(self): 
        self.assertEqual(attributes.Quality.build_quality(self.p1), 'Average Quality')
        self.assertEqual(attributes.Quality.build_quality(self.p2), 'Good Quality')
        self.assertEqual(attributes.Quality.build_quality(self.p3), 'Excellent Quality')
        self.assertEqual(attributes.Quality.build_quality(self.p4), 'Good Quality')
        self.assertEqual(attributes.Quality.build_quality(self.p5), 'Average Quality')                    

        
    def tearDown(self):
        print("Tear Down")
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite(): 
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAttributes))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
