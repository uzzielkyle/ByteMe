import unittest
import sys
sys.path.append("..") 

from conversions.from_binary import FromBinary


class TestFromBinary(unittest.TestCase):
    def test_from_binary_to_binary(self):
        data = '1010'
        result = FromBinary().to_binary(data)
        expected_output = '1010'
        
        self.assertEqual(result, expected_output)
        
    def test_from_binary_to_octal(self):
        data = '1010'
        result = FromBinary().to_octal(data)
        expected_output = '12'
        
        self.assertEqual(result, expected_output)
        
    def test_from_binary_to_decimal(self):
        data = '1010'
        result = FromBinary().to_decimal(data)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)
        
    def test_from_binary_to_hex(self):
        data = '1010'
        result = FromBinary().to_hex(data)
        expected_output = 'A'
        
        self.assertEqual(result, expected_output)
       
        
if __name__ == '__main__':
    unittest.main()
        