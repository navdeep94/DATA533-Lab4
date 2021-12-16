{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9bf28b37-f2fd-4490-b3b4-b30f1053d9dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from realestate.apartment import Condition\n",
    "import unittest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1494dce-3e0f-476b-a39a-871099638025",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_apartment_discount (__main__.TestCondition) ... ok\n",
      "test_apartment_furnishing_status (__main__.TestCondition) ... ok\n",
      "test_apartment_maintenance (__main__.TestCondition) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "setUpClass\n",
      "Set up\n",
      "Test Cases for Apartment Discount Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Furnishing Status Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Maintenance Executed\n",
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
      "Ran 3 tests in 0.006s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x2d3c2c00a60>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class TestCondition(unittest.TestCase):\n",
    "    def setUp(self):\n",
    "        self.conditionAge1 = Condition.Condition('0-3')\n",
    "        self.conditionAge2 = Condition.Condition('3-5')\n",
    "        print(\"Set up\")\n",
    "    \n",
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
    "        \n",
    "    def test_apartment_maintenance(self): # test case\n",
    "        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')\n",
    "        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')\n",
    "        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge2), 'Required')\n",
    "        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge2), 'Required')\n",
    "        self.assertEqual(Condition.Condition.apartment_maintenance(self.conditionAge1), 'Not Required')\n",
    "        print(\"Test Cases for Apartment Maintenance Executed\")\n",
    "        \n",
    "        \n",
    "    def test_apartment_discount(self): # test case\n",
    "        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')\n",
    "        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge1), '0-5%')\n",
    "        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')\n",
    "        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge1), '0-5%')\n",
    "        self.assertEqual(Condition.Condition.apartment_discount(self.conditionAge2), '5-10%')\n",
    "        print(\"Test Cases for Apartment Discount Executed\")\n",
    "        \n",
    "        \n",
    "    def test_apartment_furnishing_status(self): # test case\n",
    "        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')\n",
    "        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge2), 'Semi Furnished')\n",
    "        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')\n",
    "        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge2), 'Semi Furnished')\n",
    "        self.assertEqual(Condition.Condition.apartment_furnishing_status(self.conditionAge1), 'Fully Furnished')\n",
    "        print(\"Test Cases for Apartment Furnishing Status Executed\")\n",
    "        \n",
    "        \n",
    "unittest.main(argv =[''], verbosity=2, exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9ee47031-09f7-44ee-9e78-fa3570779584",
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
      "Test Cases for Apartment Discount Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Furnishing Status Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Maintenance Executed\n",
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
    "    suite.addTest(unittest.makeSuite(TestCondition))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32a435b8-7fb2-486b-add7-b5040322b5bb",
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
