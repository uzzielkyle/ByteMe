import unittest
import sys
sys.path.append("..") 

from conversions.from_hex import FromHex


class TestFromHex(unittest.TestCase):
    def test_from_hex_to_binary(self):
        data = 'A'
        result = FromHex().to_binary(data)
        expected_output = '1010'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_octal(self):
        data = 'A'
        result = FromHex().to_octal(data)
        expected_output = '12'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_decimal(self):
        data = 'A'
        result = FromHex().to_decimal(data)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_hex(self):
        data = 'A'
        result = FromHex().to_hex(data)
        expected_output = 'A'
        
        self.assertEqual(result, expected_output)
       
        
if __name__ == '__main__':
    unittest.main()
        