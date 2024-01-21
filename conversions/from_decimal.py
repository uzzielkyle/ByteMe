class FromDecimal:
    ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, n: int) -> str:
        try:
            return self.ALPHABET[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)

    def to_binary(self, decimal: str) -> str:
        if '.' in decimal:
            decimal_whole, decimal_part = decimal.split('.')
            return f'{self.to_binary_whole(decimal_whole)}.{self.to_binary_part(decimal_part)}'
        return str(self.to_binary_whole(decimal))

    def to_binary_whole(self, decimal_whole: str) -> str:
        if isinstance(decimal_whole, str):
            decimal_whole = int(decimal_whole)

        if decimal_whole < 2:
            return self.encode(decimal_whole)
        else:
            return self.to_binary_whole(decimal_whole // 2) + self.encode(decimal_whole % 2)

    def to_binary_part(self, decimal_part: str) -> str:
        decimal_part = float(f'0.{decimal_part}')
        binary = ''

        # Set a maximum number of iterations to avoid infinite loop
        max_iterations = 20

        while max_iterations > 0:
            if decimal_part == 0:
                break

            decimal_part = decimal_part * 2
            char, decimal_part = str(decimal_part).split('.')
            decimal_part = float(f'0.{decimal_part}')
            char = int(char)
            binary += self.encode(char)

            max_iterations -= 1

        return str(binary)

    def to_octal(self, decimal: str) -> str:
        if '.' in decimal:
            decimal_whole, decimal_part = decimal.split('.')
            return f'{self.to_octal_whole(decimal_whole)}.{self.to_octal_part(decimal_part)}'
        return str(self.to_octal_whole(decimal))

    def to_octal_whole(self, decimal_whole: str) -> str:
        if isinstance(decimal_whole, str):
            decimal_whole = int(decimal_whole)

        if decimal_whole < 8:
            return self.encode(decimal_whole)
        else:
            return self.to_octal_whole(decimal_whole // 8) + self.encode(decimal_whole % 8)

    def to_octal_part(self, decimal_part: str) -> str:
        decimal_part = float(f'0.{decimal_part}')
        octal = ''

        # Set a maximum number of iterations to avoid infinite loop
        max_iterations = 20

        while max_iterations > 0:
            if decimal_part == 0:
                break

            decimal_part = decimal_part * 8
            char, decimal_part = str(decimal_part).split('.')
            decimal_part = float(f'0.{decimal_part}')
            char = int(char)
            octal += self.encode(char)

            max_iterations -= 1

        return str(octal)

    def to_decimal(self, decimal: int | str = 0) -> str:
        if decimal == '':
            decimal = 0
        return str(decimal)

    def to_hex(self, decimal: str) -> str:
        if '.' in decimal:
            decimal_whole, decimal_part = decimal.split('.')
            return f'{self.to_hex_whole(decimal_whole)}.{self.to_hex_part(decimal_part)}'
        return str(self.to_hex_whole(decimal))

    def to_hex_whole(self, decimal_whole: str) -> str:
        if isinstance(decimal_whole, str):
            decimal_whole = int(decimal_whole)

        if decimal_whole < 16:
            return self.encode(decimal_whole)
        else:
            return self.to_hex_whole(decimal_whole // 16) + self.encode(decimal_whole % 16)

    def to_hex_part(self, decimal_part: str) -> str:
        decimal_part = float(f'0.{decimal_part}')
        hex_str = ''

        # Set a maximum number of iterations to avoid infinite loop
        max_iterations = 20

        while max_iterations > 0:
            if decimal_part == 0:
                break

            decimal_part = decimal_part * 16
            char, decimal_part = str(decimal_part).split('.')
            decimal_part = float(f'0.{decimal_part}')
            char = int(char)
            hex_str += self.encode(char)

            max_iterations -= 1

        return str(hex_str)
