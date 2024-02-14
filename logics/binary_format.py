class BinaryFormat:
    def perform(self, binary: str) -> str:
        if binary[-1] == '.':
            binary = binary + '0000'
        
        if binary[0] == '.':
            binary = '0000' + binary

            
        binary, point_position = self.add_paddings(binary)
        
        if point_position:
            binary = self.insert_point(binary, point_position)
        else:
            binary = self.group_by_bytes(binary)
            
        return binary
        
    @staticmethod
    def add_paddings(binary: str) -> str:
        binary = binary.replace(' ', '')  # remove spaces
        is_fraction_only: bool = True if '.' in binary and binary[0] == '.' \
            else False
        binary = binary.split('.')
        has_fraction: bool = (len(binary) == 2) \
            and binary[1] != ''
        
        left: str | None = None
        right: str | None = None
        
        if has_fraction:
            left, right = binary
        elif is_fraction_only:
            right = binary[0]
        else:
            left = binary[0]
            
        point_position: int | None = None
        
        if left:
            left_length = len(left)
            left_padding_amount = 0
            
            while (left_length % 4) != 0:
                left_padding_amount += 1
                left_length += 1
                
            if (left_length - left_padding_amount % 4) != 0:
                if left_length > 4 and left[0] == '1':
                    left = ('1' * left_padding_amount) + left
                else:
                    left = left.zfill(left_length)
                    
            # determines where to put fixed point later by number of bytes
            if has_fraction:
                point_position = left_length // 4  

        if right:    
            
            right_length = len(right)
            right_padding_amount = 0
                        
            while (right_length % 4) != 0:
                right_padding_amount += 1
                right_length += 1
                
            right = right + ('0' * right_padding_amount)
            
            if is_fraction_only:
                point_position = 0
            
        if has_fraction:
            binary = f'{left}{right}'
        elif is_fraction_only:
            binary = right
        else:
            binary = left
            
        return binary, point_position
    
    def insert_point(self, binary: str, point_position: int) -> str:
        result = [(binary[idx:idx+4]) for idx in range(0, len(binary), 4)]
            
        result_whole = ''.join(result[:point_position])
        result_whole = self.group_by_bytes(result_whole)
        
        result_fraction = ''.join(result[point_position:])
        result_fraction = self.group_by_bytes(result_fraction)            
        
        result = f'{result_whole}.{result_fraction}'
        
        return result
    
    @staticmethod
    def group_by_bytes(binary: str) -> str:
        result = ''
        for idx in range(0, len(binary), 4):
            result += f'{binary[idx: idx+4]} '
        
        result = result.strip()
        
        return result
    
    @staticmethod
    def balance_two_binaries(binary1: str, binary2: str) -> str:
        diff1 = len(binary2) - len(binary1)
        diff2 = len(binary1) - len(binary2)
        if diff1 > 0:
            if binary1[0] == '1':
                for bytes in range(0, diff1//4):
                    binary1 = '1111 ' + binary1
            else:  
                for bytes in range(0, diff1//4):
                    binary1 = '0000 ' + binary1
            
        if diff2 > 0:
            if binary2[0] == '1':
                for bytes in range(0, diff2//4):
                    binary2 = '1111 ' + binary2
            else:
                for bytes in range(0, diff2//4):
                    binary2 = '0000 ' + binary2
                
        return binary1, binary2
        