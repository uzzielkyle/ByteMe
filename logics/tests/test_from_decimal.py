import unittest
import sys
sys.path.append("..") 

from logics.from_decimal import FromDecimal


class TestFromDecimal(unittest.TestCase):
    def test_from_decimal_to_binary(self):
        data = '10'
        result = FromDecimal().to_binary(data)
        expected_output = '0000 1010'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_octal(self):
        data = '10'
        result = FromDecimal().to_octal(data)
        expected_output = '12'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_decimal(self):
        data = '10'
        result = FromDecimal().to_decimal(data)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_hex(self):
        data = '10'
        result = FromDecimal().to_hex(data)
        expected_output = 'A'
        
        self.assertEqual(result, expected_output)
        

class TestFromDecimalFraction(unittest.TestCase):
    def test_from_decimal_to_binary_fraction(self):
        data = '10.5'
        result = FromDecimal().to_binary(data)
        expected_output = '0000 1010.1000'
        
        self.assertEqual(result, expected_output)
    
    def test_from_decimal_to_octal_fraction(self):
        data = '24.23'
        result = FromDecimal().to_octal(data)
        expected_output = '30.16560507'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_decimal_fraction(self):
        data = '23.24'
        result = FromDecimal().to_decimal(data)
        expected_output = '23.24'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_hex_fraction(self):
        data = '8.24'
        result = FromDecimal().to_hex(data)
        expected_output = '8.3D70A3D7'
        
        self.assertEqual(result, expected_output)
    
       
        
if __name__ == '__main__':
    unittest.main()
        