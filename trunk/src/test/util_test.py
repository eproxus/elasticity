import unittest
from elasticity.util import Sequence

class ConstructorTest(unittest.TestCase):
    MaxVal = (0, 1, -1, 10, -10, 1000000)
    
    def testDefaultValue(self):
        for val in self.MaxVal:
            assert val == Sequence(val), 'incorrect default value'
        
    def testInitValue(self):
        assert 3 == Sequence(10, 3), 'incorrect init value'

if __name__ == "__main__":
    unittest.main()