class BinaryAddition:
    @staticmethod
    def perform(binary_num1, binary_num2):
        sign1 = int(binary_num1[0])  # Sign bit of the binary_num1
        sign2 = int(binary_num2[0])  # Sign bit of the binary_num2

        # Handle sign extension
        if sign1 == 1:
            binary_num1 = "1" + binary_num1[1:].zfill(18)  # 18-bit signed
        else:
            binary_num1 = "0" + binary_num1[1:].zfill(18)

        if sign2 == 1:
            binary_num2 = "1" + binary_num2[1:].zfill(18)
        else:
            binary_num2 = "0" + binary_num2[1:].zfill(18)

        max_len = max(len(binary_num1), len(binary_num2))

        result = ''
        carry = 0

        for i in range(max_len - 1, -1, -1):
            bit_sum = int(binary_num1[i]) + int(binary_num2[i]) + carry
            carry = bit_sum // 2
            result = str(bit_sum % 2) + result

        # Check for overflow (discard the most significant bit)
        if carry:
            result = result[1:]

        # Handle overflow and assign sign bit
        if sign1 == sign2 and sign1 != int(result[0]):
            result = "1" + result

        return result

    @staticmethod
    def get_name():
        return 'Addition'