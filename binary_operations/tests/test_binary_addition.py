import unittest
import sys
sys.path.append("..") 

from binary_operations.binary_addition import BinaryAddition


class TestBinaryAddition(unittest.TestCase):
    def test_one_bit(self):
        data1 = '1'
        data2 = '1'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)

    def test_one_byte(self):
        data1 = '1010'
        data2 = '1101'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '10111'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes(self):
        data1 = '0111 1010'
        data2 = '1100 0011'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '11000 1101'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes_without_space(self):
        data1 = '10001001'
        data2 = '01111010'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '100001111'
        
        self.assertEqual(result, expected_output)
        
    def test_two_bytes_with_fraction(self):
        data1 = '1001.0010'
        data2 = '1101.1011'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '11011.1101'
        
        self.assertEqual(result, expected_output)
        
    def test_three_bytes_incomplete(self):
        data1 = '0 1101 1000'
        data2 = '1111 0010 1001'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '10001 1010 1001'
        
        self.assertEqual(result, expected_output)
        
    def test_three_bytes_incomplete_with_fractions(self):
        data1 = '1101.1000 100'
        data2 = '1010.0111 001'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '10100.1111 101'
        
        self.assertEqual(result, expected_output)
        
    def test_four_bytes_incomplete_with_fractions(self):
        data1 = '1 1001.0100'
        data2 = '0000 0110.1101'
        result = BinaryAddition().perform(binary1=data1, binary2=data2)
        expected_output = '11010 0011.0001'
        
        self.assertEqual(result, expected_output)
    

if __name__ == '__main__':
    unittest.main()
