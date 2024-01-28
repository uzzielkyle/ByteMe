from conversions.from_decimal import FromDecimal


class FromHex:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = 16
    
    def decode(self, s: str) -> int:
        try:
            return self.ALPHABET.index(s)
        except ValueError:
            raise Exception ("cannot decode: %s" % s)

    def to_binary(self, hex: str = '') -> str:
        decimal = self.to_decimal(hex)
        
        return FromDecimal().to_binary(decimal)
        
    def to_octal(self, hex: str = '') -> str:
        decimal = self.to_decimal(hex)
        
        return FromDecimal().to_octal(decimal)  
          
    def to_decimal(self, hex: str = '') -> str:
        if '.' in hex:
            whole_hex, part_hex = hex.split('.')
            return \
                f'{self.to_decimal_whole(whole_hex)}.{self.to_decimal_part(part_hex)}'
        
        return self.to_decimal_whole(hex)
        
    def to_decimal_whole(self, hex: str = '') -> str:
        power = len(hex) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(hex[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
    
    def to_decimal_part(self, hex: str = '') -> str:
        power = -1
        decimal = 0
        index = 0
        
        while index < len(hex):
            decimal += self.decode(hex[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal).strip('0.')
               
    def to_hex(self, hex: str = '') -> str:
        return hex
    