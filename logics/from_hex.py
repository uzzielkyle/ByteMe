from logics.from_decimal import FromDecimal


class FromHex:
    ALPHABET = \
    "0123456789ABCDEF"
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
        def convert(hex: str, is_whole: bool = True) -> str:
            power = len(hex) - 1 if is_whole \
                else -1
            decimal = 0
            index = 0
            
            while index < len(hex):
                decimal += self.decode(hex[index]) * (self.BASE ** power)
                power -= 1
                index += 1
            
            decimal = str(decimal)
            
            if decimal.startswith('0.'):
                decimal = decimal[2:]
                
            return decimal
        
        is_negative = '-' in hex
        
        if is_negative:
            hex = hex.replace('-', '')
        
        if '.' in hex:
            whole_hex, part_hex = hex.split('.')
            if is_negative:
                return \
                    f'-{convert(whole_hex)}.{convert(part_hex, False)}'
            else:
                return \
                    f'{convert(whole_hex)}.{convert(part_hex, False)}'
        
        if is_negative:
            return '-' + convert(hex)
        else:
            return convert(hex)
                       
    def to_hex(self, hex: str = '') -> str:
        try:
            for char in hex:
                if char not in '-.0123456789ABCDEF':
                    raise
            return hex
        except:
            return 'not a hex'
    