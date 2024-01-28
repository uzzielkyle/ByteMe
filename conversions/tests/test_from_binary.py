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


class TestFromBinaryFraction(unittest.TestCase):
    def test_from_binary_to_binary_fraction(self):
        data = '1101.1101'
        result = FromBinary().to_binary(data)
        expected_output = '1101.1101'
        
        self.assertEqual(result, expected_output) 
        
    def test_from_binary_to_octal_fraction(self):
        data = '1101.1101'
        result = FromBinary().to_octal(data)
        expected_output = '15.64'
        
        self.assertEqual(result, expected_output)  
        
    def test_from_binary_to_decimal_fraction(self):
        data = '0111.11'
        result = FromBinary().to_decimal(data)
        expected_output = '7.75'
        
        self.assertEqual(result, expected_output) 
        
    def test_from_binary_to_hex_fraction(self):
        data = '1101.1101'
        result = FromBinary().to_hex(data)
        expected_output = 'D.D'
        
        self.assertEqual(result, expected_output)
        
                
if __name__ == '__main__':
    unittest.main()
        