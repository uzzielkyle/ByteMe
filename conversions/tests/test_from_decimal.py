import unittest
import sys
sys.path.append("..") 

from conversions.from_decimal import FromDecimal


class TestFromDecimal(unittest.TestCase):
    def test_from_decimal_to_binary(self):
        data = 10
        result = FromDecimal().to_binary(data)
        expected_output = '1010'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_octal(self):
        data = 10
        result = FromDecimal().to_octal(data)
        expected_output = '12'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_decimal(self):
        data = 10
        result = FromDecimal().to_decimal(data)
        expected_output = '10'
        
        self.assertEqual(result, expected_output)
        
    def test_from_decimal_to_hex(self):
        data = 10
        result = FromDecimal().to_hex(data)
        expected_output = 'A'
        
        self.assertEqual(result, expected_output)
       
        
if __name__ == '__main__':
    unittest.main()
        