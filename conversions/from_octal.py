from conversions.from_decimal import FromDecimal


class FromOctal:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
        decimal = self.to_decimal(octal)
        
        return FromDecimal().to_binary(decimal)
        
    def to_octal(self, octal: str = '') -> str:
        return octal
        
    def to_decimal(self, octal: str = '') -> str:
        power = len(octal) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(octal[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
               
    def to_hex(self, octal: str = '') -> str:
        decimal = self.to_decimal(octal)
        
        return FromDecimal().to_hex(decimal)
    