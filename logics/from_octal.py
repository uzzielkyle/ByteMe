from logics.from_binary import FromBinary
from logics.binary_format import BinaryFormat


class FromOctal:
    ALPHABET = \
    "01234567"
    BASE = 8
    
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

    def to_binary(self, octal: str = '') -> str:
        def convert_to_decimal(decimal: str) -> str:
            result = ''
            
            while decimal > 2:
                result += self.encode(decimal % 2)
                decimal = decimal // 2
            
            result += self.encode(decimal % 2)
            
            result = result[::-1].zfill(3)
            
            return result
            
        binary = ''
        
        for char in octal:
            if char == '.':
                binary += char
                continue
            
            binary += convert_to_decimal(self.decode(char))
            
        binary = BinaryFormat().perform(binary)
        
        return binary
        
    def to_octal(self, octal: str = '') -> str:
        try:
            for char in octal:
                if char not in '.01234567':
                    raise
                
            if octal[0] == '.':
                octal = f'0{octal}'
                
            return octal
        except:
            return 'not an octal'
        
    def to_decimal(self, octal: str = '') -> str:
        binary = self.to_binary(octal)
        
        return FromBinary().to_decimal(binary)
               
    def to_hex(self, octal: str = '') -> str:
        binary = self.to_binary(octal)

        return FromBinary().to_hex(binary)
    