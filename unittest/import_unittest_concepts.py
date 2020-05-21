#使用unittest框架中的，测试套件TestSuite和测试运行器TextTestRunner

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("test start:")
    
    def tearDown(self):
        print('test end')

if __name__ == "__main__":
    pass