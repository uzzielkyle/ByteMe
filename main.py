from binary_operations import *
from conversions import *
from os import system


class Interface:
    def __init__(self) -> None:
        self.MAIN_MENU_OPTIONS = {
            '1': self.binary_operations_menu, 
            '2': self.number_system_conversion_menu, 
            '3': self.exit,
        }
        self.BINARY_OPERATIONS_OPTIONS = {}
        self.NUMBER_SYSTEM_CONVERSION_OPTIONS = {}
    
    def main_menu(self):
        self.clear_screen()
        
        menu_display = """Menu-1 (Main Menu)
        
        [1] Binary Operations
        [2] Number System Conversion
        [3] Exit
        """
        
        print(menu_display)
        choice = input('Enter desired option number: ').strip()
        
        try:
            self.MAIN_MENU_OPTIONS[choice]()
        except KeyError:
            input('Invalid input...')
            self.main_menu()
        
    def binary_operations_menu(self):
        self.clear_screen()
        
        menu_display = """Menu-2 (Binary Operations)
        
        [1] Division
        [2] Multiplication
        [3] Subtraction
        [4] Addition
        [5] Negative (Two's Complement)
        """
        
        print(menu_display)
        choice = input('Enter desired option number: ')
        
        # TODO work on this part
        self.main_menu()
        
    def number_system_conversion_menu(self):
        self.clear_screen()
        
        menu_display = """Menu-3 (Conversion)
        
        [1] Binary to X
        [2] Decimal to X
        [3] Octal to X
        [4] Hexa to X
        """
        
        print(menu_display)
        choice = input('Enter desired option number: ')
        
        # TODO work on this part
        self.main_menu()
    
    def exit(self):
        self.clear_screen()
        
        text_display = """
        
        THANK YOU FOR USING ME!
        
        \t - ByteMe
        
        """
        
        print(text_display)
        exit()
        
    @staticmethod
    def clear_screen():
        system('cls')
        
        
if __name__ == '__main__':
    app = Interface()
    app.main_menu()
    