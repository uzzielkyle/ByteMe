from conversions.from_decimal import FromDecimal


class FromHex:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
        decimal = self.to_decimal(hex)
        
        return FromDecimal().to_binary(decimal)
        
    def to_octal(self, hex: str = '') -> str:
        decimal = self.to_decimal(hex)
        
        return FromDecimal().to_octal(decimal)  
          
    def to_decimal(self, hex: str = '') -> str:
        power = len(hex) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(hex[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
               
    def to_hex(self, hex: str = '') -> str:
        return hex
    