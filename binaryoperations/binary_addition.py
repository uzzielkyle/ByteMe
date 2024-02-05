class BinaryAddition:
    @staticmethod
    def perform(binary_num1, binary_num2):
        max_len = max(len(binary_num1), len(binary_num2))
        binary_num1 = binary_num1.zfill(max_len)
        binary_num2 = binary_num2.zfill(max_len)
        
        result = ''
        carry = 0
        
        for i in range(max_len -1, -1, -1):
            bit_sum = int(binary_num1[i]) + int(binary_num2[i]) + carry
            carry = bit_sum // 2
            result = str(bit_sum % 2) + result
        
        if carry: 
            result = '1' + result
            
        result = BinaryAddition.group_by_bytes(result)
        return result
    
    @staticmethod
    def add_paddings(binary: str) -> str:
        # removing decimal point if there is
        binary = binary.split('.')
        point_position: int | None = None

        if len(binary) == 2:
            binary_whole = binary[0]
            binary_whole_length = len(binary_whole)
            binary_whole_padding_amount = 0


            while (binary_whole_length % 4) != 0:
                binary_whole_padding_amount += 1
                binary_whole_length += 1

            if (binary_whole_length-binary_whole_padding_amount % 4) != 0:  
                if binary_whole[0] == '0':   
                    binary_whole = binary_whole.zfill(binary_whole_length)
                else:
                    binary_whole = ('1' * binary_whole_padding_amount) + binary_whole

            point_position = binary_whole_length // 4  # determines where to put decimal point later

            binary_fraction = binary[1]
            binary_fraction_length = len(binary_fraction)
            binary_fraction_padding_amount = 0

            while (binary_fraction_length % 4) != 0:
                binary_fraction_padding_amount += 1
                binary_fraction_length += 1

            binary_fraction = binary_fraction + ('0' * binary_fraction_padding_amount)

            binary = f'{binary_whole}{binary_fraction}'
            binary_length = len(binary)

        else:
            binary = binary[0]
            binary_length = len(binary)

            while (binary_length % 4) != 0:
                binary_length += 1

            binary = binary.zfill(binary_length)

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
    def get_name():
        return 'Addition'