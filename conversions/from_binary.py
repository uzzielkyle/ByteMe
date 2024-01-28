from conversions.from_decimal import FromDecimal


class FromBinary:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = 2
    
    def decode(self, s: str) -> int:
        try:
            return self.ALPHABET.index(s)
        except ValueError:
            raise Exception ("cannot decode: %s" % s)

    def to_binary(self, binary: str = '') -> str:
        return binary
        
    def to_octal(self, binary: str = '') -> str:
        decimal = self.to_decimal(binary)
        
        return FromDecimal().to_octal(decimal)
        
    def to_decimal(self, binary: str = '') -> str:
        if '.' in binary:
            whole_binary, part_binary = binary.split('.')
            return \
                f'{self.to_decimal_whole(whole_binary)}.{self.to_decimal_part(part_binary)}'
        
        return self.to_decimal_whole(binary)
        
    def to_decimal_whole(self, binary: str = '') -> str:
        power = len(binary) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(binary[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
    
    def to_decimal_part(self, binary: str = '') -> str:
        power = -1
        decimal = 0
        index = 0
        
        while index < len(binary):
            decimal += self.decode(binary[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal).strip('0.')
               
    def to_hex(self, binary: str = '') -> str:
        decimal = self.to_decimal(binary)
        
        return FromDecimal().to_hex(decimal)
    