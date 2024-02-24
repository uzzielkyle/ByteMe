from customtkinter import *
from CTkMessagebox import CTkMessagebox
# from PIL import Image
from logics import *


class Interface(CTk):
    BINARY_OPERATIONS_SCREEN_TITLES = {
        '1': "Division",
        '2': "Multiplication",
        '3': "Subtraction",
        '4': "Addition",
        '5': "Negative (Two's Complement)",
    }
    BINARY_OPERATIONS_SCREEN_OPTIONS = {
        '1': BinaryDivision(),
        '2': BinaryMultiplication(),
        '3': BinarySubtraction(),
        '4': BinaryAddition(),
        '5': BinaryNegative(),
    }
    NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES = {
        '1': "Binary to X",
        '2': "Decimal to X",
        '3': "Octal to X",
        '4': "Hex to X",
    }
    NUMBER_SYSTEM_CONVERSION_OPTIONS = {
        '1': FromBinary(),
        '2': FromDecimal(),
        '3': FromOctal(),
        '4': FromHex(),
    }

    def __init__(self):
        super().__init__()
        self.title('ByteMe')
        self.geometry('500x300')
        self.minsize(320, 320)
        # self.resizable(width=False, height=False)
        # Modes: "System" (standard), "Dark", "Light"
        set_appearance_mode("System")
        set_default_color_theme("assets/themes/carrot.json")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_menu()

    # 1st Screen Display the Main Menu
    def main_menu(self):
        self.clear_screen()
        menu_frame = self.create_frame()

        menu_label = CTkLabel(menu_frame, text="Main Menu",
                              font=('Helvetica', 20, "bold"))
        menu_label.pack(padx=10, pady=10)

        binary_button = CTkButton(
            menu_frame, text="Binary Operations", command=self.binary_operations_menu)
        binary_button.pack(padx=5, pady=5)

        conversion_button = CTkButton(
            menu_frame, text="Number System Conversion", command=self.number_system_conversion_menu)
        conversion_button.pack(pady=5)

        exit_button = CTkButton(menu_frame, text="Exit",
                                command=self.exit_screen)
        exit_button.pack(pady=5)

    # 2nd Screen Display the Binary Operations Menu
    def binary_operations_menu(self):
        self.clear_screen()

        menu_frame = self.create_frame()

        menu_label = CTkLabel(
            menu_frame, text="Binary Operations Menu", font=('Helvetica', 20, "bold"))
        menu_label.pack(pady=10)

        division_button = CTkButton(menu_frame, text="Division",
                                    command=lambda: self.perform_binary_operation_input_screen('1'))
        division_button.pack(padx=5, pady=5)

        multiplication_button = CTkButton(menu_frame, text="Multiplication",
                                          command=lambda: self.perform_binary_operation_input_screen('2'))
        multiplication_button.pack(padx=5, pady=5)

        subtraction_button = CTkButton(menu_frame, text="Subtraction",
                                       command=lambda: self.perform_binary_operation_input_screen('3'))
        subtraction_button.pack(padx=5, pady=5)

        addition_button = CTkButton(menu_frame, text="Addition",
                                    command=lambda: self.perform_binary_operation_input_screen('4'))
        addition_button.pack(padx=5, pady=5)

        twos_complement_button = CTkButton(menu_frame, text="Negative (Two's Complement)",
                                           command=lambda: self.perform_binary_operation_input_screen('5'))
        twos_complement_button.pack(padx=5, pady=5)

        back_button = CTkButton(
            menu_frame, text="Back to Main Menu", command=self.main_menu)
        back_button.pack(padx=5, pady=5)

    # Display the Input Screen of Binary Operation
    def perform_binary_operation_input_screen(self, choice):
        self.clear_screen()

        title = self.BINARY_OPERATIONS_SCREEN_TITLES[choice]

        menu_frame = self.create_frame()

        menu_label = CTkLabel(menu_frame, text=title,
                              font=('Helvetica', 20, "bold"))
        menu_label.pack(padx=10, pady=10)

        binary_num1_label = CTkLabel(
            menu_frame, text="Enter the first binary number:")
        binary_num1_label.pack()
        binary_num1_entry = CTkEntry(
            menu_frame, placeholder_text="e.g. 0100 1010")
        binary_num1_entry.pack()

        if choice != '5':
            binary_num2_label = CTkLabel(
                menu_frame, text="Enter the second binary number:")
            binary_num2_label.pack()
            binary_num2_entry = CTkEntry(
                menu_frame, placeholder_text="e.g. 1111 0001")
            binary_num2_entry.pack()

        # Button to perform the operation
        if choice != '5':
            perform_button = CTkButton(menu_frame, text="Perform Operation",
                                       command=lambda:
                                       self.perform_binary_operation_output_screen(choice=choice, binary_num1=binary_num1_entry.get() if binary_num1_entry.get() != '' else '0', binary_num2=binary_num2_entry.get() if binary_num2_entry.get() != '' else '0'))
        else:
            perform_button = CTkButton(menu_frame, text="Perform Operation",
                                       command=lambda:
                                       self.perform_binary_operation_output_screen(choice=choice, binary_num1=binary_num1_entry.get() if binary_num1_entry.get() != '' else '0'))
        perform_button.pack(pady=10)

    # Display the Output Screen of Binary Operation
    def perform_binary_operation_output_screen(self,
                                               choice: str,
                                               binary_num1: str,
                                               binary_num2: str | None = None):

        self.clear_screen()

        title = self.BINARY_OPERATIONS_SCREEN_TITLES[choice]

        menu_frame = self.create_frame()

        menu_label = CTkLabel(menu_frame, text=title,
                              font=('Helvetica', 20, "bold"))
        menu_label.pack(pady=10)

        operation = self.BINARY_OPERATIONS_SCREEN_OPTIONS[choice]

        result = ''
        if choice == '5':
            result = operation.perform(binary_num1)
        else:
            result = operation.perform(binary_num1, binary_num2)

        # Create Labels to display the results
        result_label = CTkLabel(
            menu_frame, text=f"{operation.get_name()} result: {result}")
        result_label.pack(pady=10)

        # Button to return to the conversion menu
        back_button = CTkButton(
            menu_frame, text="Back to Binary Operations Menu", command=self.binary_operations_menu)
        back_button.pack(pady=5)

    # 3rd Screen Display the Number Conversion System

    def number_system_conversion_menu(self):
        self.clear_screen()

        menu_frame = self.create_frame()

        menu_label = CTkLabel(
            menu_frame, text="Number System Conversion Menu", font=('Helvetica', 20, "bold"))
        menu_label.pack(pady=10)

        binary_to_x_button = CTkButton(menu_frame, text="Binary to X",
                                       command=lambda: self.number_system_conversion_input_screen('1'))
        binary_to_x_button.pack(padx=5, pady=5)

        decimal_to_x_button = CTkButton(menu_frame, text="Decimal to X",
                                        command=lambda: self.number_system_conversion_input_screen('2'))
        decimal_to_x_button.pack(padx=5, pady=5)

        octal_to_x_button = CTkButton(menu_frame, text="Octal to X",
                                      command=lambda: self.number_system_conversion_input_screen('3'))
        octal_to_x_button.pack(padx=5, pady=5)

        hex_to_x_button = CTkButton(menu_frame, text="Hex to X",
                                    command=lambda: self.number_system_conversion_input_screen('4'))
        hex_to_x_button.pack(padx=5, pady=5)

        back_button = CTkButton(
            menu_frame, text="Back to Main Menu", command=self.main_menu)
        back_button.pack(padx=5, pady=5)

    def number_system_conversion_input_screen(self, base):
        self.clear_screen()

        title = self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES[base]

        menu_frame = self.create_frame()

        menu_label = CTkLabel(menu_frame, text=title,
                              font=('Helvetica', 20, "bold"))
        menu_label.pack(pady=10)

        number_label = CTkLabel(menu_frame, text="Enter number to convert:")
        number_label.pack(pady=5)

        number_entry = CTkEntry(menu_frame)
        number_entry.pack(pady=5)

        perform_button = CTkButton(menu_frame, text="Convert",
                                   command=lambda: self.number_system_conversion_output_screen(base=base, number=number_entry.get() if number_entry.get() != '' else '0'))
        perform_button.pack(pady=5)

    def number_system_conversion_output_screen(self, base: str, number: str):
        self.clear_screen()

        title = self.NUMBER_SYSTEM_CONVERSION_SCREEN_TITLES[base]

        menu_frame = self.create_frame()

        menu_label = CTkLabel(menu_frame, text=title,
                              font=('Helvetica', 20, "bold"))
        menu_label.pack(pady=10)

        conversion = self.NUMBER_SYSTEM_CONVERSION_OPTIONS[base]

        binary_result = conversion.to_binary(number)
        decimal_result = conversion.to_decimal(number)
        octal_result = conversion.to_octal(number)
        hex_result = conversion.to_hex(number)

        # Create Labels to display the results
        binary_label = CTkLabel(menu_frame, text=f'Binary: {binary_result}')
        binary_label.pack()

        decimal_label = CTkLabel(menu_frame, text=f'Decimal: {decimal_result}')
        decimal_label.pack()

        octal_label = CTkLabel(menu_frame, text=f'Octal: {octal_result}')
        octal_label.pack()

        hex_label = CTkLabel(menu_frame, text=f'Hex: {hex_result}')
        hex_label.pack()

        # Button to return to the conversion menu
        back_button = CTkButton(
            menu_frame, text="Back to Conversion Menu", command=self.number_system_conversion_menu)
        back_button.pack(pady=5)

    def exit_screen(self):
        msg = CTkMessagebox(title="ByteMe | Quit", message="Do you want to quit?",
                            option_1="No", option_2="Yes", corner_radius=0, sound=True, option_focus=1)

        response = msg.get()

        if response == "Yes":
            self.destroy()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_frame(self):
        menu_frame = CTkFrame(self, corner_radius=0)
        menu_frame.grid(row=0, column=0, sticky='nsew')

        return menu_frame


if __name__ == '__main__':
    app = Interface()
    app.mainloop()
