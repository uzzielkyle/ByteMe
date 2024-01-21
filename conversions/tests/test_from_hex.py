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
        

class TestFromHexFraction(unittest.TestCase):
    def test_from_hex_to_binary_fraction(self):
        data = '1A.C8'
        result = FromHex().to_binary(data)
        expected_output = '11010.11001'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_octal_fraction(self):
        data = 'A10.DE'
        result = FromHex().to_octal(data)
        expected_output = '5020.674'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_decimal_fraction(self):
        data = 'D1CE.AB'
        result = FromHex().to_decimal(data)
        expected_output = '53710.66796875'
        
        self.assertEqual(result, expected_output)
        
    def test_from_hex_to_hex_fraction(self):
        data = 'D1CE.AB'
        result = FromHex().to_hex(data)
        expected_output = 'D1CE.AB'
        
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()
        