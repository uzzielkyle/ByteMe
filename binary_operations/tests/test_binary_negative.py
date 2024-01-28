import unittest
import sys
sys.path.append("..") 

from binary_operations.binary_negative import BinaryNegative


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
        
    def test_three_bytes_incomplete(self):
        data = '0 1101 1000'
        result = BinaryNegative().perform(binary=data)
        expected_output = '1111 0010 1000'
        
        self.assertEquals(result, expected_output)
    

if __name__ == '__main__':
    unittest.main()