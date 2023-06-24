# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# NeetuUpadhyay,06.24.2023,Created started script
# NeetuUpadhyay,06.24.2023,Added pseudo-code to start assignment 8
# <NeetuUpadhyay>,<06.24.2023>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #

strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product"""

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return f"{self.product_name} - ${self.product_price}"

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects"""

    @staticmethod
    def read_data_from_file(file_name: object) -> object:
        """Read data from a file"""
        lstOfProductObjects = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) >= 2:
                        product_name = data[0]
                        product_price = float(data[1])
                        product = Product(product_name, product_price)
                        lstOfProductObjects.append(product)
                    else:
                        print("Invalid data format in the file. Skipping the line.")
            return lstOfProductObjects
        except IOError:
            print("Error occurred while reading data from file.")
            return []

    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        """Save data to a file"""
        try:
            with open(file_name, 'w') as file:
                for product in lstOfProductObjects:
                    file.write(product.product_name + ',' + str(product.product_price) + '\n')
            print("Data saved successfully.")
        except IOError:
            print("Error occurred while saving data to file.")

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """A class for performing Input and Output"""

    @staticmethod
    def print_menu_items():
        """Display a menu of choices to the user"""
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def get_user_choice():
        """Get user's menu choice"""
        choice = input("Enter your choice (1-4): ")
        return choice

    @staticmethod
    def print_current_list_items(lstOfProductObjects):
        """Print the current list of items"""
        print("Current Data:")
        for product in lstOfProductObjects:
            print(product)
        print()

    @staticmethod
    def input_product_data():
        """Get product data from user"""
        product_name = input("Enter the product name: ")
        while True:
            try:
                product_price = float(input("Enter the product price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the product price.")
        return Product(product_name, product_price)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    # Show user a menu of options
    IO.print_menu_items()

    # Get user's menu option choice
    user_choice = IO.get_user_choice()

    if user_choice == '1':
        # Show user current data in the list of product objects
        IO.print_current_list_items(lstOfProductObjects)
    elif user_choice == '2':
        # Let user add data to the list of product objects
        product = IO.input_product_data()
        lstOfProductObjects.append(product)
    elif user_choice == '3':
        # Save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        break
    elif user_choice == '4':
        # Exit program
        break
    else:
        print("Invalid choice. Please try again.")
        continue

# Main Body of Script  ---------------------------------------------------- #