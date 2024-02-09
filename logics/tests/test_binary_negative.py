import unittest
import sys
sys.path.append("..") 

from logics.binary_negative import BinaryNegative


class TestBinaryNegative(unittest.TestCase):
    def test_one_bit(self):
        data = '1'
        result = BinaryNegative().perform(binary=data)
        expected_output = '1111'
        
        self.assertEqual(result, expected_output)

    def test_one_byte(self):
        data = '1010'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0110'
        
        self.assertEquals(result, expected_output)
        
    def test_two_bytes(self):
        data = '0111 1010'
        result = BinaryNegative().perform(binary=data)
        expected_output = '1000 0110'
        
        self.assertEquals(result, expected_output)
        
    def test_two_bytes_without_space(self):
        data = '10001001'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0111 0111'
        
        self.assertEquals(result, expected_output)
        
    def test_two_bytes_with_fraction(self):
        data = '1001.0010'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0110.1110'
        
        self.assertEquals(result, expected_output)
        
    def test_three_bytes_incomplete(self):
        data = '0 1101 1000'
        result = BinaryNegative().perform(binary=data)
        expected_output = '1111 0010 1000'
        
        self.assertEquals(result, expected_output)
        
    def test_three_bytes_incomplete_with_fractions(self):
        data = '1101.1000 100'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0010.0111 1000'
        
        self.assertEquals(result, expected_output)
        
    def test_four_bytes_incomplete_with_fractions(self):
        data = '1 1001.0100'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0000 0110.1100'
        
        self.assertEquals(result, expected_output)
        
    def test_ni_labots(self):
        data = '1010    1110.0001'
        result = BinaryNegative().perform(binary=data)
        expected_output = '0101 0001.1111'
        
        self.assertEquals(result, expected_output)
    

if __name__ == '__main__':
    unittest.main()