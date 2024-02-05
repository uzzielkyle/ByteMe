import unittest
import sys
sys.path.append("..") 

from binary_operations.binary_division import BinaryDivision


class TestBinaryDivision(unittest.TestCase):
    def test_one_bit(self):
        data1 = '1'
        data2 = '1'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '1'
        
        self.assertEqual(result, expected_output)

    def test_one_byte(self):
        data1 = '1101'
        data2 = '10'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '110'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes(self):
        data1 = '10110'
        data2 = '110'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '100'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes_without_space(self):
        data1 = '1101101'
        data2 = '101'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '10101'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes_with_fraction(self):
        data1 = '1011.0101'
        data2 = '110.1'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '100.11'
        
        self.assertEqual(result, expected_output)
        
    def test_three_bytes_incomplete(self):
        data1 = '1101 1000'
        data2 = '110'
        result = BinaryDivision().perform(binary1=data1, binary2=data2)
        expected_output = '10101'
        
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()