from realestate.familyhome import highlights
import unittest
class TestHighlights(unittest.TestCase):
    
    def setUp(self):
        self.o1 = highlights.Highlights('1', 'low', '1')
        self.o2 = highlights.Highlights('2', 'high', '2')
        self.o3 = highlights.Highlights('3 or more', 'medium', '3')
        self.o4 = highlights.Highlights('2', 'low', '3')
        self.o5 = highlights.Highlights('1', 'low', '1')
        print("Set Up")
        
        
    @classmethod
    def setUpClass(cls):
        print("setUpClass")    
    
    
    def test_garage_capacity(self): 
        self.assertEqual(highlights.Highlights.garage_capacity(self.o1), 'No Garage available')
        self.assertEqual(highlights.Highlights.garage_capacity(self.o2), 'Garage with one car capacity')
        self.assertEqual(highlights.Highlights.garage_capacity(self.o3), 'Garage with two cars capacity')
        self.assertEqual(highlights.Highlights.garage_capacity(self.o4), 'Garage with one car capacity')
        self.assertEqual(highlights.Highlights.garage_capacity(self.o5), 'No Garage available')
 
    def test_swimming_pool_type(self): 
        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o1), 'No Swimming Pool')
        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o2), 'No Swimming Pool or Indoor Swimming Pool')
        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o3), 'No Swimming Pool, Indoor Swimming Pool or Outdoor Swimming Pool')
        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o4), 'No Swimming Pool or Indoor Swimming Pool')
        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o5), 'No Swimming Pool')

    def test_furnish_type(self): 
        self.assertEqual(highlights.Highlights.furnish_type(self.o1), 'Partially Furnished')
        self.assertEqual(highlights.Highlights.furnish_type(self.o2), 'Partially Furnished or Fully Furnished')
        self.assertEqual(highlights.Highlights.furnish_type(self.o3), 'Fully Furnished or Luxuriously Furnished')
        self.assertEqual(highlights.Highlights.furnish_type(self.o4), 'Partially Furnished or Fully Furnished')
        self.assertEqual(highlights.Highlights.furnish_type(self.o5), 'Partially Furnished')        
     
    
    def tearDown(self):
        print("Tear Down")

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
        
unittest.main(argv =[''], verbosity=2, exit=False)

def my_suite(): 
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestHighlights))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
