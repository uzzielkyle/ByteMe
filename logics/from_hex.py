from logics.from_decimal import FromDecimal
from logics.binary_format import BinaryFormat
from logics.from_binary import FromBinary


class FromHex:
    ALPHABET = \
    "0123456789ABCDEF"
    BASE = 16
    
    def encode(self, n: int) -> str:
        try:
            return self.ALPHABET[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)
        
    def decode(self, s: str) -> int:
        try:
            return self.ALPHABET.index(s)
        except ValueError:
            raise Exception ("cannot decode: %s" % s)

    def to_binary(self, hex: str = '') -> str:
        def convert_to_decimal(decimal: str) -> str:
            result = ''
            
            while decimal > 2:
                result += self.encode(decimal % 2)
                decimal = decimal // 2
            
            result += self.encode(decimal % 2)
            
            result = result[::-1].zfill(4)
            
            return result
            
        binary = ''
        
        for char in hex:
            if char == '.':
                binary += char
                continue
            
            binary += convert_to_decimal(self.decode(char))
            
        binary = BinaryFormat().perform(binary)
        
        return binary
        
    def to_octal(self, hex: str = '') -> str:
        binary = self.to_binary(hex)

        return FromBinary().to_octal(binary)
          
    def to_decimal(self, hex: str = '') -> str:
        binary = self.to_binary(hex)
        
        return FromBinary().to_decimal(binary)
                       
    def to_hex(self, hex: str = '') -> str:
        try:            
            for char in hex:
                if char not in '-.0123456789ABCDEF':
                    raise   
            
                if hex[1] == '.':
                    negative_sign, hex_fraction = hex.split('.')
                    hex = f'{negative_sign}0.{hex_fraction}'
                
            if hex[0] == '.':
                hex = f'0{hex}'
                
            return hex
        except:
            return 'not a hex'
    