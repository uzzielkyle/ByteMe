from conversions.from_decimal import FromDecimal


class FromOctal:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = 8
    
    def decode(self, s: str) -> int:
        try:
            return self.ALPHABET.index(s)
        except ValueError:
            raise Exception ("cannot decode: %s" % s)

    def to_binary(self, octal: str = '') -> str:
        decimal = self.to_decimal(octal)
        
        return FromDecimal().to_binary(decimal)
        
    def to_octal(self, octal: str = '') -> str:
        return octal
        
    def to_decimal(self, octal: str = '') -> str:
        if '.' in octal:
            whole_octal, part_octal = octal.split('.')
            return \
                f'{self.to_decimal_whole(whole_octal)}.{self.to_decimal_part(part_octal)}'
        
        return self.to_decimal_whole(octal)
        
    def to_decimal_whole(self, octal: str = '') -> str:
        power = len(octal) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(octal[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
    
    def to_decimal_part(self, octal: str = '') -> str:
        power = -1
        decimal = 0
        index = 0
        
        while index < len(octal):
            decimal += self.decode(octal[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal).strip('0.')
               
    def to_hex(self, octal: str = '') -> str:
        decimal = self.to_decimal(octal)
        
        return FromDecimal().to_hex(decimal)
    