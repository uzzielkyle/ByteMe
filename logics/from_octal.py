from logics.from_decimal import FromDecimal


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
        try:
            for char in octal:
                if char not in '-.012345678':
                    raise
            return octal
        except:
            return 'not an octal'
        
    def to_decimal(self, octal: str = '') -> str:
        def convert(octal: str, is_whole: bool = True) -> str:
            power = len(octal) - 1 if is_whole \
                else -1
            decimal = 0
            index = 0
            
            while index < len(octal):
                decimal += self.decode(octal[index]) * (self.BASE ** power)
                power -= 1
                index += 1
            
            decimal = str(decimal)
            
            if decimal.startswith('0.'):
                decimal = decimal[2:]
                
            return decimal
           
        is_negative = '-' in octal
        
        if is_negative:
            octal = octal.replace('-', '')
        
        if '.' in octal:
            whole_octal, part_octal = octal.split('.')
            if is_negative:
                return \
                    f'-{convert(whole_octal)}.{convert(part_octal, False)}'
            else:
                return \
                    f'{convert(whole_octal)}.{convert(part_octal, False)}'
        
        if is_negative:
            return '-' + convert(octal)
        else:
            return convert(octal)
               
    def to_hex(self, octal: str = '') -> str:
        decimal = self.to_decimal(octal)
        
        return FromDecimal().to_hex(decimal)
    