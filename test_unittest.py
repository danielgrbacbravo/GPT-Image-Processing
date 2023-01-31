import lineEquation 
# The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
  def test_A(self):
    self.assertEqual(lineEquation.A([1,2],[3,4]), "y = 1.0x + 0.0")

    def test_B(self):
        self.assertEqual(lineEquation.B([1,2],[3,4]), "x = 1.0y + 0.0")
    
    def test_C(self):
        self.assertEqual(lineEquation.C([1,2],[3,4]), "1.0y + 1.0x + 0.0 = 0")

    def test_D(self):
        self.assertEqual(lineEquation.D([1,2],[3,4]), "1.0y + 1.0x + -1.0 = 0")

if __name__ == '__main__':
    unittest.main() 
