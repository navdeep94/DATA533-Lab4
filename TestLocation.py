{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3a6ed198-317a-40de-9f37-3cbbdf869ca0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from realestate.apartment import Location\n",
    "import unittest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "95ae45a6-c038-436e-ba39-e70812eb7ecd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_apartment_cities (__main__.TestLocation) ... ok\n",
      "test_apartment_facing_direction (__main__.TestLocation) ... ok\n",
      "test_apartment_locality (__main__.TestLocation) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "setUpClass\n",
      "Set up\n",
      "Test Cases for Apartment Cities Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Facing Direction Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Locality Executed\n",
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
       "<unittest.main.TestProgram at 0x126ed5ff550>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class TestLocation(unittest.TestCase):\n",
    "    def setUp(self):\n",
    "        self.location_usa = Location.Location('USA')\n",
    "        self.location_canada = Location.Location('CANADA')\n",
    "        self.location_uk = Location.Location('UK')\n",
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
    "    def test_apartment_cities(self): # test case\n",
    "        self.assertEqual(Location.Location.apartment_cities(self.location_usa), ['Chicago','Seattle','New York','Boston'])\n",
    "        self.assertEqual(Location.Location.apartment_cities(self.location_usa), ['Chicago','Seattle','New York','Boston'])\n",
    "        self.assertEqual(Location.Location.apartment_cities(self.location_uk), ['London','Birmighan','Leeds','Southampton'])\n",
    "        self.assertEqual(Location.Location.apartment_cities(self.location_canada), ['Vancouver','Kelowna','Montreal','Toronto'])\n",
    "        self.assertEqual(Location.Location.apartment_cities(self.location_uk), ['London','Birmighan','Leeds','Southampton'])\n",
    "        print(\"Test Cases for Apartment Cities Executed\")\n",
    "        \n",
    "        \n",
    "    def test_apartment_locality(self): # test case\n",
    "        self.assertEqual(Location.Location.apartment_locality(self.location_usa), ['Charles Street','Brown Road','Morgan Highway','Alpine Park'])\n",
    "        self.assertEqual(Location.Location.apartment_locality(self.location_canada), ['English Bay','Glenmore','Concordia Street','Robson Park'])\n",
    "        self.assertEqual(Location.Location.apartment_locality(self.location_uk), ['Smith Rd','James Arthur Mall','Michelle Street','Captain James Edward Road'])\n",
    "        self.assertEqual(Location.Location.apartment_locality(self.location_canada), ['English Bay','Glenmore','Concordia Street','Robson Park'])\n",
    "        self.assertEqual(Location.Location.apartment_locality(self.location_usa), ['Charles Street','Brown Road','Morgan Highway','Alpine Park'])\n",
    "        print(\"Test Cases for Apartment Locality Executed\")\n",
    "        \n",
    "        \n",
    "        \n",
    "    def test_apartment_facing_direction(self): # test case\n",
    "        self.assertEqual(Location.Location.apartment_facing_direction(self.location_uk), ['North West','South','South West','East'])\n",
    "        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])\n",
    "        self.assertEqual(Location.Location.apartment_facing_direction(self.location_canada), ['South West','North','West','South East'])\n",
    "        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])\n",
    "        self.assertEqual(Location.Location.apartment_facing_direction(self.location_usa), ['North','South','East','West','North East'])\n",
    "        print(\"Test Cases for Apartment Facing Direction Executed\")\n",
    "\n",
    "unittest.main(argv =[''], verbosity=2, exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ffe3e4e6-6b3d-46b5-a957-76c3a4433a35",
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
      "Test Cases for Apartment Cities Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Facing Direction Executed\n",
      "Tear Down\n",
      "Set up\n",
      "Test Cases for Apartment Locality Executed\n",
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
    "    suite.addTest(unittest.makeSuite(TestLocation))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ca2938f-01f7-4229-8a0c-5e7d8e16512f",
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
