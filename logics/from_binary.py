from logics.binary_format import BinaryFormat


class FromBinary:
    ALPHABET = \
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = 2
    FORMATTER = BinaryFormat()
    
    def decode(self, s: str) -> int:
        try:
            return self.ALPHABET.index(s)
        except ValueError:
            raise Exception ("cannot decode: %s" % s)
    
    def encode(self, n: int) -> str:
        try:
            return self.ALPHABET[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)

    def to_binary(self, binary: str = '') -> str:
        return self.FORMATTER.perform(binary)
        
    def to_octal(self, binary: str = '') -> str:
        binary = self.FORMATTER.perform(binary)
        binary = binary.replace(' ', '') # removes spaces
            
        point_idx = binary.index('.') if '.' in binary else None
        whole_binary = binary[:point_idx]
        
        if whole_binary[0] == '1':
            whole_binary = (3 - (len(whole_binary) % 3)) * '1' + whole_binary
        else:
            whole_binary = (3 - (len(whole_binary) % 3)) * '0' + whole_binary
                
        octal = ''
                
        for idx in range(3, len(whole_binary) + 1, 3):
            bit_str = whole_binary[idx - 3:idx]
            octal = octal + self.to_decimal(bit_str, formatted=False, is_signed=False)
                    
        if point_idx: 
            octal = octal + '.'
            
            fraction_binary = binary[point_idx + 1:]    
            
            if len(fraction_binary) % 3 != 0:
                fraction_binary = fraction_binary + (3 - (len(fraction_binary) % 3)) * '0'   
                
            for idx in range(0, len(whole_binary) + 1, 3):
                bit_str = fraction_binary[idx:idx + 3]
                octal = octal + self.to_decimal(bit_str, formatted=False, is_signed=False)  
                
        while octal[0] == '0':
            if point_idx and octal[0] == '0' and octal[1] == '.':
                break 
            
            octal = octal[1:]
            
        while octal[-1] == '0':
            octal = octal[:-1]

        return octal
        
    def to_decimal(self, binary: str = '', formatted: bool = True, is_signed: bool = True) -> str:
        def convert(binary: str, is_whole: bool = True, is_signed: bool = True) -> str:
            power = len(binary) - 1 - binary.count(' ') if is_whole \
                else - 1
            decimal = 0
            index = 0
                        
            while index < len(binary):
                if binary[index] == ' ':
                    index += 1
                    continue
                
                if is_whole and is_signed and index == 0:
                    decimal += (-1 * self.decode(binary[index])) * (self.BASE ** power)
                else:   
                    decimal += self.decode(binary[index]) * (self.BASE ** power)
                power -= 1
                index += 1
            
            decimal = str(decimal)
            
            if decimal.startswith('0.'):
                decimal = decimal[2:]
                
            return decimal
        
        if formatted:
            binary = self.FORMATTER.perform(binary)
            
        if not is_signed:
            return convert(binary, is_signed=False)
            
        if '.' in binary:
            whole_binary, part_binary = binary.split('.')

            return \
                f'{convert(whole_binary)}.{convert(part_binary, is_whole=False)}'
        
        return convert(binary)
               
    def to_hex(self, binary: str = '') -> str:
        is_negative = binary[0] == '1'
        binary = self.FORMATTER.perform(binary) 
        binary = binary.replace(' ', '') # removes spaces
            
        point_idx = binary.index('.') if '.' in binary else None
        whole_binary = binary[:point_idx]
        
        if whole_binary[0] == '1':
            whole_binary = (4 - (len(whole_binary) % 4)) * '1' + whole_binary
        else:
            whole_binary = (4 - (len(whole_binary) % 4)) * '0' + whole_binary
                
        hex = ''
                
        for idx in range(4, len(whole_binary) + 1, 4):
            dec = int(self.to_decimal(whole_binary[idx - 4:idx], formatted=False, is_signed=False))
            hex = hex + self.encode(dec)
                    
        if point_idx: 
            hex = hex + '.'
            
            fraction_binary = binary[point_idx + 1:]    
            
            if len(fraction_binary) % 4 != 0:
                fraction_binary = fraction_binary + (4 - (len(fraction_binary) % 4)) * '0'   
                    
            for idx in range(4, len(fraction_binary) + 1, 4):
                dec = int(self.to_decimal(fraction_binary[idx - 4:idx], formatted=False, is_signed=False))
                hex = hex + self.encode(dec)
                        
        while hex[0] == '0':
            if point_idx and hex[0] == '0' and hex[1] == '.':
                break 
            
            hex = hex[1:]
                        
        while hex[-1] == '0':
            hex = hex[:-1]
             
        return hex