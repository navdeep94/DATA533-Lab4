{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a496cde1-af31-43dd-a88c-eedc104eb914",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_nearby_amenities (__main__.TestAreaType) ... ok\n",
      "test_population (__main__.TestAreaType) ... ok\n",
      "test_view (__main__.TestAreaType) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "setUpClass\n",
      "Set Up\n",
      "Tear Down\n",
      "Set Up\n",
      "Tear Down\n",
      "Set Up\n",
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
      "Ran 3 tests in 0.002s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x1696e54af10>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from realestate.familyhome import areatype\n",
    "import unittest\n",
    "class TestAreaType(unittest.TestCase):\n",
    "    \n",
    "    def setUp(self):\n",
    "        self.o1 = areatype.AreaType('1', 'low', '1')\n",
    "        self.o2 = areatype.AreaType('2', 'high', '2')\n",
    "        self.o3 = areatype.AreaType('3 or more', 'medium', '3')\n",
    "        self.o4 = areatype.AreaType('2', 'low', '3')\n",
    "        self.o5 = areatype.AreaType('1', 'low', '1')\n",
    "        print(\"Set Up\")\n",
    "        \n",
    "   \n",
    "    \n",
    "    @classmethod\n",
    "    def setUpClass(cls):\n",
    "        print(\"setUpClass\")\n",
    "    \n",
    "    def test_nearby_amenities(self):\n",
    "        self.assertEqual(areatype.AreaType.nearby_amenities(self.o1), 'Hospital, Park, Shopping Center, School, and a Mall')\n",
    "        self.assertEqual(areatype.AreaType.nearby_amenities(self.o2), 'Hospital, Park, Shopping Center, and a School')\n",
    "        self.assertEqual(areatype.AreaType.nearby_amenities(self.o3), 'Hospital, Park, Shopping Center, School, Mall, Library, Beach, and a Cafe')\n",
    "        self.assertEqual(areatype.AreaType.nearby_amenities(self.o4), 'Hospital, Park, Shopping Center, and a School')\n",
    "        self.assertEqual(areatype.AreaType.nearby_amenities(self.o5), 'Hospital, Park, Shopping Center, School, and a Mall')\n",
    "        \n",
    "    def test_view(self): \n",
    "        self.assertEqual(areatype.AreaType.view(self.o1), 'Normal view, park facing, or sea facing')\n",
    "        self.assertEqual(areatype.AreaType.view(self.o2), 'Normal View or Park facing')\n",
    "        self.assertEqual(areatype.AreaType.view(self.o3), 'Normal view, park facing, sea facing, or sun facing')\n",
    "        self.assertEqual(areatype.AreaType.view(self.o4), 'Normal View or Park facing')\n",
    "        self.assertEqual(areatype.AreaType.view(self.o5), 'Normal view, park facing, or sea facing')\n",
    "\n",
    "    def test_population(self): \n",
    "        self.assertEqual(areatype.AreaType.population(self.o1), 'highly populated')\n",
    "        self.assertEqual(areatype.AreaType.population(self.o2), 'average population around')\n",
    "        self.assertEqual(areatype.AreaType.population(self.o3), 'very less population')\n",
    "        self.assertEqual(areatype.AreaType.population(self.o4), 'average population around')\n",
    "        self.assertEqual(areatype.AreaType.population(self.o5), 'highly populated')        \n",
    "\n",
    "    def tearDown(self):\n",
    "        print(\"Tear Down\")\n",
    "        \n",
    "    @classmethod\n",
    "    def tearDownClass(cls):\n",
    "        print('teardownClass')    \n",
    "        \n",
    "unittest.main(argv =[''], verbosity=2, exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ac841318-636d-46dc-b8fe-7bb716d79ed6",
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
      "Set Up\n",
      "Tear Down\n",
      "Set Up\n",
      "Tear Down\n",
      "Set Up\n",
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
    "def my_suite(): \n",
    "    suite = unittest.TestSuite()\n",
    "    result = unittest.TestResult()\n",
    "    suite.addTest(unittest.makeSuite(TestAreaType))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc594371-7b8a-4ee3-af8a-b98f9fae3dd8",
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
