from logics import *
from os import system
from time import sleep


class Interface:
    APP_TITLE = 'ByteMe'
    
    def __init__(self) -> None:
        self.MAIN_MENU_OPTIONS = {
            '1': self.binary_operations_menu, 
            '2': self.number_system_conversion_menu, 
            '3': self.exit_screen,
        }
        self.BINARY_OPERATIONS_SCREEN_TITLES = {
            '1': 'Binary Division',
            '2': 'Binary Multiplication',
            '3': 'Binary Subtraction',
            '4': 'Binary Addition',
            '5': 'Binary Two\'s Complement',
        }
        self.BINARY_OPERATIONS_SCREEN_OPTIONS = {
            '1': BinaryDivision(),
            '2': BinaryMultiplication(),
            '3': BinarySubtraction(),
            '4': BinaryAddition(),
            '5': BinaryNegative(),
        }
        self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES = {
            '1': 'Binary to X',
            '2': 'Decimal to X',
            '3': 'Octal to X',
            '4': 'Hex to X',
        }
        self.NUMBER_SYSTEM_CONVERSION_OPTIONS = {
            '1': FromBinary(),
            '2': FromDecimal(),
            '3': FromOctal(),
            '4': FromHex(),
        }
    
    def main_menu(self):
        self.clear_screen()
        
        menu_display = """%s
        
        Menu-1 (Main Menu)
        
        [1] Binary Operations
        [2] Number System Conversion
        [3] Exit
        """ % (self.APP_TITLE)
        
        print(menu_display)
        choice = input('Enter desired option number: ').strip()
        
        try:
            self.MAIN_MENU_OPTIONS[choice]()
        except KeyError:
            input('Invalid input...')
            self.main_menu()
        
    def binary_operations_menu(self):
        self.clear_screen()
        
        menu_display = """%s
        
        Menu-2 (Binary Operations)
        
        [1] Division
        [2] Multiplication
        [3] Subtraction
        [4] Addition
        [5] Negative (Two's Complement)
        [6] Main Menu
        """ % (self.APP_TITLE)
        
        print(menu_display)
        choice = input('Enter desired option number: ')
        
        if choice == '6':
            self.main_menu()  # Exit the loop and return to the main menu

        elif choice in self.BINARY_OPERATIONS_SCREEN_OPTIONS:
                self.perform_binary_operation_input_screen(choice)

        else:
            input("Invalid choice. Please enter a number between 1 and 6.")
            self.binary_operations_menu()

    def perform_binary_operation_input_screen(self, choice: str):
        self.clear_screen()
        
        title = self.BINARY_OPERATIONS_SCREEN_TITLES[choice]

        print(self.APP_TITLE, '\n')
        print(title, '\n\n')
        
        binary_num1 = input("Enter the first binary number: ")
        binary_num2 = None
        if choice != '5':
            binary_num2 = input("Enter the second binary number: ")
            
        try:
            for char in binary_num1 + binary_num2:
                if char not in ' .-01':
                    raise
                
            self.perform_binary_operation_output_screen(
                choice=choice, 
                binary_num1=binary_num1, 
                binary_num2=binary_num2)
        except:
            input('Invalid input.')
            self.perform_binary_operation_input_screen()
        
    def perform_binary_operation_output_screen(self, choice: str, binary_num1: str, binary_num2: str | None):
        self.clear_screen()
        
        title = self.BINARY_OPERATIONS_SCREEN_TITLES[choice]

        print(self.APP_TITLE, '\n')
        print(title, '\n\n')
        
        operation =  self.BINARY_OPERATIONS_SCREEN_OPTIONS[choice]
        
        if choice == '5':
            result = operation.perform(binary_num1)
        else:
            result = operation.perform(binary_num1, binary_num2)
            
        if binary_num2:
            print(f'Binary1: {BinaryFormat().perform(binary_num1)}')
            print(f'Binary2: {BinaryFormat().perform(binary_num2)}')
        else:
            print(f'Binary: {BinaryFormat().perform(binary=binary_num1)}')
            
        print(f"{operation.get_name()} result: {result}")
        input("\n\nPress Enter to continue...")
        
        self.binary_operations_menu()
        
    def number_system_conversion_menu(self):
        self.clear_screen()
        
        menu_display = """%s
        
        Menu-3 (Conversion)
        
        [1] Binary to X
        [2] Decimal to X
        [3] Octal to X
        [4] Hexa to X
        [5] Main Menu
        """ % (self.APP_TITLE)
        
        print(menu_display)
        choice = input('Enter desired option number: ').strip()
        
        if choice in self.NUMBER_SYSTEM_CONVERSION_OPTIONS:
            self.number_system_conversion_input_screen(base=choice)
        elif choice == '5':
            self.main_menu()
        else:
            input('Invalid input...')
            self.number_system_conversion_menu()
            
    def number_system_conversion_input_screen(self, base: str):
        self.clear_screen()
        
        title = self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES[base]
        
        print(self.APP_TITLE, '\n')
        print(title, '\n\n')
        number = input('Enter number to convert: ').strip()
        
        self.number_system_conversion_output_screen(base=base, number=number)
        
    def number_system_conversion_output_screen(self, base: str, number: str):
        self.clear_screen()
        
        title = self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES[base]
        
        print(self.APP_TITLE, '\n')
        print(title, '\n\n')
        
        conversion = self.NUMBER_SYSTEM_CONVERSION_OPTIONS[base]

        print(f'Binary: {conversion.to_binary(number)}')
        print(f'Decimal: {conversion.to_decimal(number)}')
        print(f'Octal: {conversion.to_octal(number)}')
        print(f'Hex: {conversion.to_hex(number)}')
        input("\n\nPress Enter to continue...")
        
        self.number_system_conversion_menu()
        
    def not_available_screen(self):
        self.clear_screen()
        
        print(self.APP_TITLE, '\n')
        
        text_display = """
        
        This menu is still not available.
        
        \t - %s
        
        """ % (self.APP_TITLE)
        
        print(text_display)
        input('')
        
        self.main_menu()
    
    def exit_screen(self):
        self.clear_screen()
        
        text_display = """
        
        THANK YOU FOR USING ME!
        
        \t - %s
        
        """ % (self.APP_TITLE)
        
        print(text_display)
        sleep(1)
        exit()
        
    @staticmethod
    def clear_screen():
        system('cls')
        
        
if __name__ == '__main__':
    try:
        app = Interface()
        app.main_menu()
    except KeyboardInterrupt:
        print('\nSession Interrupted :<')
    