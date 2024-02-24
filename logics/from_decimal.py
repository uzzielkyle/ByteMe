from logics.from_binary import FromBinary
from logics.binary_negative import BinaryNegative
from logics.binary_format import BinaryFormat


class FromDecimal:
    ALPHABET = "0123456789"

    def encode(self, n: int) -> str:
        try:
            return self.ALPHABET[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)

    def to_binary(self, decimal: str) -> str:
        is_negative = float(decimal) < 0
        decimal = decimal.replace('-', '')

        if '.' in decimal:
            decimal_whole, decimal_part = decimal.split('.')
            binary_whole = self.whole_conversion(decimal=decimal_whole, base=2)
            binary_part = self.fraction_conversion(
                decimal=decimal_part, base=2)
            binary = f'{binary_whole}.{binary_part}'
        else:
            binary = str(self.whole_conversion(decimal=decimal, base=2))

        if binary[0] == '1':
            binary = f'0{binary}'

        binary = BinaryFormat().perform(binary)

        if is_negative:
            binary = BinaryNegative().perform(binary)  # two's complement

        return binary

    def to_octal(self, decimal: str) -> str:
        binary = self.to_binary(decimal)

        return FromBinary().to_octal(binary)

    def to_decimal(self, decimal: int | str = 0) -> str:
        try:
            if decimal == '0':
                return decimal
            is_negative = '-' in decimal
            for char in decimal:
                if char not in '-.0123456789':
                    raise

            if is_negative:
                if decimal.startswith('.'):
                    negative_sign, decimal_fraction = decimal.split('.')
                    decimal = f'{negative_sign}0.{decimal_fraction}'

            while decimal.startswith('0'):
                if decimal.startswith('0') and decimal[1] == '.':
                    break

                decimal = decimal[1:]

            while decimal.endswith('0'):
                decimal = decimal[:-1]

            if decimal.startswith('.'):
                decimal = f'0{decimal}'

            if decimal.endswith('.'):
                decimal = decimal[:-1]

            return decimal
        except:
            return 'not a decimal'

    def to_hex(self, decimal: str) -> str:
        binary = self.to_binary(decimal)

        return FromBinary().to_hex(binary)

    def whole_conversion(self, decimal: str, base: int) -> str:
        try:
            if isinstance(decimal, str):
                decimal = int(decimal)

            if decimal < base:
                return self.encode(decimal)
            else:
                return self.whole_conversion(decimal // base, base) + self.encode(decimal % base)
        except:
            return '0'

    def fraction_conversion(self, decimal: str, base: int) -> str:
        decimal = float(f'0.{decimal}')
        result = ''

        # Set a maximum number of iterations to avoid infinite loop
        max_iterations = 36

        while max_iterations > 0:
            if decimal == 0:
                break

            decimal = decimal * base
            char, decimal = str(decimal).split('.')
            decimal = float(f'0.{decimal}')
            char = int(char)
            result += self.encode(char)

            max_iterations -= 1

        # Remove '0.' from the result if it exists
        if result.startswith('0.'):
            result = result[2:]

        return str(result)
