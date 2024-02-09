import unittest
import sys
sys.path.append("..") 

from conversions.from_octal import FromOctal


class TestFromOctal(unittest.TestCase):
    def test_from_octal_to_binary(self):
        data = '12'
        result = FromOctal().to_binary(data)
        expected_output = '1010'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_octal(self):
        data = '12'
        result = FromOctal().to_octal(data)
        expected_output = '12'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_decimal(self):
        data = '12'
        result = FromOctal().to_decimal(data)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_hex(self):
        data = '12'
        result = FromOctal().to_hex(data)
        expected_output = 'A'
        
        self.assertEqual(result, expected_output)
        

class TestFromOctalFraction(unittest.TestCase):               
    def test_from_octal_to_binary_fraction(self):
        data = '12.5'
        result = FromOctal().to_binary(data)
        expected_output = '1010.101'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_octal_fraction(self):
        data = '21.5021'
        result = FromOctal().to_octal(data)
        expected_output = '21.5021'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_decimal_fraction(self):
        data = '21.5021'
        result = FromOctal().to_decimal(data)
        expected_output = '17.629150390625'
        
        self.assertEqual(result, expected_output)
        
    def test_from_octal_to_hex_fraction(self):
        data = '5020.674'
        result = FromOctal().to_hex(data)
        expected_output = 'A10.DE'
        
        self.assertEqual(result, expected_output)
    
    
        
        
if __name__ == '__main__':
    unittest.main()
        