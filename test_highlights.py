{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "224d2852-dfa7-42b5-bd6f-77d747288f89",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_furnish_type (__main__.TestHighlights) ... ok\n",
      "test_garage_capacity (__main__.TestHighlights) ... ok\n",
      "test_swimming_pool_type (__main__.TestHighlights) ... "
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
       "<unittest.main.TestProgram at 0x24e7db61160>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from realestate.familyhome import highlights\n",
    "import unittest\n",
    "class TestHighlights(unittest.TestCase):\n",
    "    \n",
    "    def setUp(self):\n",
    "        self.o1 = highlights.Highlights('1', 'low', '1')\n",
    "        self.o2 = highlights.Highlights('2', 'high', '2')\n",
    "        self.o3 = highlights.Highlights('3 or more', 'medium', '3')\n",
    "        self.o4 = highlights.Highlights('2', 'low', '3')\n",
    "        self.o5 = highlights.Highlights('1', 'low', '1')\n",
    "        print(\"Set Up\")\n",
    "        \n",
    "        \n",
    "    @classmethod\n",
    "    def setUpClass(cls):\n",
    "        print(\"setUpClass\")    \n",
    "    \n",
    "    \n",
    "    def test_garage_capacity(self): \n",
    "        self.assertEqual(highlights.Highlights.garage_capacity(self.o1), 'No Garage available')\n",
    "        self.assertEqual(highlights.Highlights.garage_capacity(self.o2), 'Garage with one car capacity')\n",
    "        self.assertEqual(highlights.Highlights.garage_capacity(self.o3), 'Garage with two cars capacity')\n",
    "        self.assertEqual(highlights.Highlights.garage_capacity(self.o4), 'Garage with one car capacity')\n",
    "        self.assertEqual(highlights.Highlights.garage_capacity(self.o5), 'No Garage available')\n",
    " \n",
    "    def test_swimming_pool_type(self): \n",
    "        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o1), 'No Swimming Pool')\n",
    "        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o2), 'No Swimming Pool or Indoor Swimming Pool')\n",
    "        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o3), 'No Swimming Pool, Indoor Swimming Pool or Outdoor Swimming Pool')\n",
    "        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o4), 'No Swimming Pool or Indoor Swimming Pool')\n",
    "        self.assertEqual(highlights.Highlights.swimming_pool_type(self.o5), 'No Swimming Pool')\n",
    "\n",
    "    def test_furnish_type(self): \n",
    "        self.assertEqual(highlights.Highlights.furnish_type(self.o1), 'Partially Furnished')\n",
    "        self.assertEqual(highlights.Highlights.furnish_type(self.o2), 'Partially Furnished or Fully Furnished')\n",
    "        self.assertEqual(highlights.Highlights.furnish_type(self.o3), 'Fully Furnished or Luxuriously Furnished')\n",
    "        self.assertEqual(highlights.Highlights.furnish_type(self.o4), 'Partially Furnished or Fully Furnished')\n",
    "        self.assertEqual(highlights.Highlights.furnish_type(self.o5), 'Partially Furnished')        \n",
    "     \n",
    "    \n",
    "    def tearDown(self):\n",
    "        print(\"Tear Down\")\n",
    "\n",
    "    @classmethod\n",
    "    def tearDownClass(cls):\n",
    "        print('teardownClass')\n",
    "        \n",
    "        \n",
    "unittest.main(argv =[''], verbosity=2, exit=False)       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "23a1ade3-ebf5-4eb5-b70a-13cfe70ff0eb",
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
    "    suite.addTest(unittest.makeSuite(TestHighlights))\n",
    "    runner = unittest.TextTestRunner()\n",
    "    print(runner.run(suite))\n",
    "my_suite()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c721122c-765c-4ab2-bae2-0f21f54e2b19",
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
