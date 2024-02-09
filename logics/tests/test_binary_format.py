import unittest
import sys
sys.path.append("..") 

from logics.binary_format import BinaryFormat


class TestBinaryFormat(unittest.TestCase):
    def test_two_bytes_no_space(self):
        data = '10101111'
        result = BinaryFormat().perform(data)
        expected_output = '1010 1111'
        
        self.assertEqual(result, expected_output)
        
    def test_fraction_only(self):
        data = '.11'
        result = BinaryFormat().perform(data)
        expected_output = '.1100'
        
        self.assertEqual(result, expected_output)
        
    def test_whole_with_unnecessary_fix_point(self):
        data = '11.'
        result = BinaryFormat().perform(data)
        expected_output = '0011'
        
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()
    