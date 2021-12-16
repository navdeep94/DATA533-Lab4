{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2218ae70-c769-41b4-8318-a7b1aeb90fa1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from realestate.apartment import Feature\n",
    "import unittest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f1c1c07e-b258-46a8-b3ea-cc10ac1b18c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_apartment_area (__main__.TestApartmentType) ... ok\n",
      "test_apartment_floors (__main__.TestApartmentType) ... ok\n",
      "test_apartment_price (__main__.TestApartmentType) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "setUpClass\n",
      "Set up\n",
      "Test Cases for Apartment Area Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Floors Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Price Executed\n",
      "Tear Down\n",
      "teardownClass\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 3 tests in 0.007s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x1a096d06730>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class TestApartmentType(unittest.TestCase):\n",
    "    def setUp(self):\n",
    "        self.apartmentType1 = Feature.Features('1BHK')\n",
    "        self.apartmentType2 = Feature.Features('2BHK')\n",
    "        self.apartmentType3 = Feature.Features('3BHK')\n",
    "        print(\"Set up\")\n",
    "        \n",
    "    @classmethod\n",
    "    def setUpClass(cls):\n",
    "        print(\"setUpClass\")\n",
    "        \n",
    "    def tearDown(self):\n",
    "        print(\"Tear Down\")\n",
    "\n",
    "    @classmethod\n",
    "    def tearDownClass(cls):\n",
    "        print('teardownClass')\n",
    "\n",
    "        \n",
    "    def test_apartment_area(self): # test case\n",
    "        self.assertEqual(Feature.Features.apartment_area(self.apartmentType1), '500 - 800 sqft')\n",
    "        self.assertEqual(Feature.Features.apartment_area(self.apartmentType2), '800 - 1100 sqft')\n",
    "        self.assertEqual(Feature.Features.apartment_area(self.apartmentType2), '800 - 1100 sqft')\n",
    "        self.assertEqual(Feature.Features.apartment_area(self.apartmentType1), '500 - 800 sqft')\n",
    "        self.assertEqual(Feature.Features.apartment_area(self.apartmentType3), '1100 - 1500 sqft')\n",
    "        print(\"Test Cases for Apartment Area Executed\")\n",
    "        \n",
    "    def test_apartment_price(self): # test case\n",
    "        self.assertEqual(Feature.Features.apartment_price(self.apartmentType1), '150000 - 200000 CAD')\n",
    "        self.assertEqual(Feature.Features.apartment_price(self.apartmentType2), '250000 - 300000 CAD')\n",
    "        self.assertEqual(Feature.Features.apartment_price(self.apartmentType2), '250000 - 300000 CAD')\n",
    "        self.assertEqual(Feature.Features.apartment_price(self.apartmentType1), '150000 - 200000 CAD')\n",
    "        self.assertEqual(Feature.Features.apartment_price(self.apartmentType3), '350000 - 400000 CAD')\n",
    "        print(\"Test Cases for Apartment Price Executed\")\n",
    "        \n",
    "    def test_apartment_floors(self): # test case\n",
    "        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType1), [2, 3, 7, 11, 13])\n",
    "        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType2), [1, 4, 5, 8, 10])\n",
    "        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType2), [1, 4, 5, 8, 10])\n",
    "        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType1), [2, 3, 7, 11, 13])\n",
    "        self.assertEqual(Feature.ApartmentType.apartment_floors(self.apartmentType3), [6, 9, 12, 14, 15])\n",
    "        print(\"Test Cases for Apartment Floors Executed\")\n",
    "        \n",
    "unittest.main(argv =[''], verbosity=2, exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2fb73d32-f5a8-43e0-9656-5e77763078ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "..."
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "setUpClass\n",
      "Set up\n",
      "Test Cases for Apartment Area Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Floors Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Price Executed\n",
      "Tear Down\n",
      "teardownClass\n",
      "<unittest.runner.TextTestResult run=3 errors=0 failures=0>\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 3 tests in 0.002s\n",
      "\n",
      "OK\n"
     ]
    }
   ],
   "source": [
    "def my_suite():\n",
    "    suite = unittest.TestSuite()\n",
    "    result = unittest.TestResult()\n",
    "    suite.addTest(unittest.makeSuite(TestApartmentType))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f27233a-65f2-4555-8589-24d783c05859",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
