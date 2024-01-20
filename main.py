from binary_operations import *
from conversions import *
from os import system
from time import sleep


class Interface:
    APP_TITLE = 'ByteMe'
    
    def __init__(self) -> None:
        self.MAIN_MENU_OPTIONS = {
            '1': self.not_available_screen,
            # '1': self.binary_operations_menu, 
            '2': self.number_system_conversion_menu, 
            '3': self.exit_screen,
        }
        self.BINARY_OPERATIONS_OPTIONS = {}
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
        
        # TODO work on this part
        self.main_menu()
        
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
            self.number_system_conversion_screen(base=choice)
        elif choice == '5':
            self.main_menu()
        else:
            input('Invalid input...')
            self.number_system_conversion_menu()
            
    def number_system_conversion_screen(self, base: str):
        self.clear_screen()
        
        title = self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES[base]
        conversion = self.NUMBER_SYSTEM_CONVERSION_OPTIONS[base]
        
        print(self.APP_TITLE, '\n')
        print(title, '\n\n')
        number = input('Enter number to convert: ').strip()
        
        print('\n\nOUTPUT\n')
        print(f'Binary: {conversion.to_binary(number)}')
        print(f'Decimal: {conversion.to_decimal(number)}')
        print(f'Octal: {conversion.to_octal(number)}')
        print(f'Hex: {conversion.to_hex(number)}')
        input('...')
        
        self.main_menu()
        
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
    