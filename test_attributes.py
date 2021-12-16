{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c09c91ff-6363-4b53-a4fd-3695e81a341c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_build_quality (__main__.TestAreaType) ... ok\n",
      "test_house_area (__main__.TestAreaType) ... ok\n",
      "test_house_price (__main__.TestAreaType) ... ok\n",
      "test_build_quality (__main__.TestAttributes) ... ok\n",
      "test_house_area (__main__.TestAttributes) ... ok\n",
      "test_house_price (__main__.TestAttributes) ... "
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
      "Ran 6 tests in 0.005s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x1bd2f5d89a0>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from realestate.familyhome import attributes\n",
    "import unittest\n",
    "class TestAttributes(unittest.TestCase):\n",
    "    \n",
    "    def setUp(self):\n",
    "        self.o1 = attributes.Characteristics('1', 'low', '1')\n",
    "        self.o2 = attributes.Characteristics('2', 'high', '2')\n",
    "        self.o3 = attributes.Characteristics('3 or more', 'medium', '3')\n",
    "        self.o4 = attributes.Characteristics('2', 'low', '3')\n",
    "        self.o5 = attributes.Characteristics('1', 'low', '1')\n",
    "        self.p1 = attributes.Quality('1', 'low', '1')\n",
    "        self.p2 = attributes.Quality('2', 'high', '2')\n",
    "        self.p3 = attributes.Quality('3 or more', 'medium', '3')\n",
    "        self.p4 = attributes.Characteristics('2', 'low', '3')\n",
    "        self.p5 = attributes.Quality('1', 'low', '1')\n",
    "        print(\"Set Up\")\n",
    "        \n",
    "   \n",
    "      \n",
    "    @classmethod\n",
    "    def setUpClass(cls):\n",
    "        print(\"setUpClass\")\n",
    "       \n",
    "    def test_house_price(self): \n",
    "        self.assertEqual(attributes.Characteristics.house_price(self.o1), '500000-600000')\n",
    "        self.assertEqual(attributes.Characteristics.house_price(self.o2), '600000-700000')\n",
    "        self.assertEqual(attributes.Characteristics.house_price(self.o3), '700000-800000')\n",
    "        self.assertEqual(attributes.Characteristics.house_price(self.o4), '600000-700000')\n",
    "        self.assertEqual(attributes.Characteristics.house_price(self.o5), '500000-600000')\n",
    "               \n",
    "    def test_house_area(self): \n",
    "        self.assertEqual(attributes.Characteristics.house_area(self.o1), '1400 sq. ft')\n",
    "        self.assertEqual(attributes.Characteristics.house_area(self.o2), '1600 sq. ft')\n",
    "        self.assertEqual(attributes.Characteristics.house_area(self.o3), '1800 sq. ft')\n",
    "        self.assertEqual(attributes.Characteristics.house_area(self.o4), '1600 sq. ft')\n",
    "        self.assertEqual(attributes.Characteristics.house_area(self.o5), '1400 sq. ft')            \n",
    "\n",
    "    def test_build_quality(self): \n",
    "        self.assertEqual(attributes.Quality.build_quality(self.p1), 'Average Quality')\n",
    "        self.assertEqual(attributes.Quality.build_quality(self.p2), 'Good Quality')\n",
    "        self.assertEqual(attributes.Quality.build_quality(self.p3), 'Excellent Quality')\n",
    "        self.assertEqual(attributes.Quality.build_quality(self.p4), 'Good Quality')\n",
    "        self.assertEqual(attributes.Quality.build_quality(self.p5), 'Average Quality')                    \n",
    "\n",
    "        \n",
    "    def tearDown(self):\n",
    "        print(\"Tear Down\")\n",
    "        \n",
    "    @classmethod\n",
    "    def tearDownClass(cls):\n",
    "        print('teardownClass')\n",
    "        \n",
    "unittest.main(argv =[''], verbosity=2, exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7771e87b-4fef-4138-a7da-b784d301e44f",
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
    "    suite.addTest(unittest.makeSuite(TestAttributes))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62085936-95ae-41e2-af18-1c2fab13b1e7",
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
