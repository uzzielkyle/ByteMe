from conversions.from_decimal import FromDecimal


class FromBinary:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = 2

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

    def to_binary(self, binary: str = '') -> str:
        return binary
        
    def to_octal(self, binary: str = '') -> str:
        decimal = self.to_decimal(binary)
        
        return FromDecimal().to_octal(decimal)
        
    def to_decimal(self, binary: str = '') -> str:
        power = len(binary) - 1
        decimal = 0
        index = 0
        
        while power >= 0:
            decimal += self.decode(binary[index]) * (self.BASE ** power)
            power -= 1
            index += 1
            
        return str(decimal)
               
    def to_hex(self, binary: str = '') -> str:
        decimal = self.to_decimal(binary)
        
        return FromDecimal().to_hex(decimal)
    