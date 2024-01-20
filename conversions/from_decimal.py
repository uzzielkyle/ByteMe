class FromDecimal:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def encode(self, n: int) -> str:
        try:
            return self.ALPHABET[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)

    def to_binary(self, decimal: int | str = 0) -> str:
        if isinstance(decimal, str):
            decimal = int(decimal)
            
        if decimal < 2:
            return self.encode(decimal)
        else:
            return self.to_binary(decimal // 2) + self.encode(decimal % 2)
        
    def to_octal(self, decimal: int | str = 0) -> str:
        if isinstance(decimal, str):
            decimal = int(decimal)
            
        if decimal < 8:
            return self.encode(decimal)
        else:
            return self.to_octal(decimal // 8) + self.encode(decimal % 8)
        
    def to_decimal(self, decimal: int |str = 0) -> str:
        return str(decimal)
        
    def to_hex(self, decimal: int | str = 0) -> str:
        if isinstance(decimal, str):
            decimal = int(decimal)
            
        if decimal < 16:
            return self.encode(decimal)
        else:
            return self.to_hex(decimal // 16) + self.encode(decimal % 16)
    