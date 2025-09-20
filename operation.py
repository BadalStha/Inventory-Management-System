import write
def display_products(data):
    """
    Displays all products in a formatted table.

    Parameters:
        data (list): List of products, where each product is a list of its attributes.

    Returns: None
    """
    print("==============================Products in Inventory==================================")
    print("Name            | Brand           | Quantity        | Price           | Origin")
    for each in data:
        print("{:<15} | {:<15} | {:<15} | {:<15} | {:<15} ".format(each[0], each[1], each[2], each[3], each[4]))
    print("=====================================================================================")


def add_new_product(data):
    """
    Adds a new product to the inventory after validating input and checking for duplicates.
    Also generates a purchase invoice and updates the inventory file.

    Parameters:
        data (list): List of existing products.

    Returns: None
    """
    invoice_details = []
    while True:
        product_name = is_empty("\nEnter product name: ")

        if is_already_exist(data, product_name):
            print("This item is already in the inventory.")
        else:
            product_brand = is_empty("Enter product brand: ")
            product_quantity = valid_user_input('Enter the product quantity: ')
            product_price = valid_user_input('Enter the product Price: ')
            product_origin = is_empty("Enter product origin: ")

            new_list = [product_name, product_brand, product_quantity, product_price, product_origin]
            invoice_details.append(new_list)
            data.append(new_list)

            if not get_yes_no("\nDo you want to add another product? (y/n): "):
                print("\nProduct details: ", invoice_details, " \n ")
                write.invoice_of_add_new_product(invoice_details)
                write.write_data(data)
                print("\nProduct Purchased Successfully!")
                break



def add_stock(data):
    """
    Adds stock to an existing product in the inventory.
    Updates the product quantity and generates a stock invoice.

    Parameters:
        data (list): List of existing products.

    Returns: None
    """
    invoice_details = []
    while True:
        product_name = input("\nEnter product name: ")
        product_in_inventory = False

        for i in range(len(data)):
            if data[i][0].lower() == product_name.lower():
                product_in_inventory = True
                product_quantity = valid_user_input("Enter the product quantity: ")
                selected_item = data[i]
                previous_quantity = int(selected_item[2])

                updated_quantity = int(previous_quantity) + product_quantity
                invoice_record = [selected_item[0], selected_item[1], product_quantity, int(selected_item[3]), selected_item[4]]
                invoice_details.append(invoice_record)
                data[i][2] = updated_quantity
        if not product_in_inventory:
            print("No such product found")

        if not get_yes_no("\nDo you want to add stock of another product? (y/n): "):
            write.invoice_of_new_stock(invoice_details)
            write.write_data(data)
            print("\nStock purchased Successfully")
            break



def sales_product(data):
    """
    Processes the sale of a product, updates inventory, applies discounts if applicable,
    and generates a sales invoice.

    Parameters:
        data (list): List of existing products.

    Returns: None
    """
    invoice_details = []
    while True:
        product_name = input("\nEnter product name: ")
        if is_already_exist(data, product_name):

            for i in range(len(data)):
                if data[i][0].lower() == product_name.lower():
                    product_quantity = valid_user_input('Enter the product quantity: ')
                    selected_item = data[i]
                    previous_quantity = int(selected_item[2])
                    discount = 0
                    if product_quantity > 10:
                        if selected_item[4] == "domestic":
                            discount = 0.07
                        elif selected_item[4] == "international":
                            discount = 0.05
                    discount_amount = product_quantity * int(selected_item[3]) * discount
                    total_price = product_quantity * int(selected_item[3])
                    final_price = total_price - discount_amount

                    if previous_quantity >= product_quantity:
                        updated_quantity = int(previous_quantity) - product_quantity
                        invoice_record = [selected_item[0], selected_item[1], product_quantity, int(selected_item[3]), selected_item[4], discount_amount, final_price]
                        invoice_details.append(invoice_record)

                        data[i][2] = updated_quantity
                    else:
                        print("Insufficient Stock Available!")

            if not get_yes_no("\nIs there another product that is being sold? (y/n): "):
                write.invoice_of_sales_product(invoice_details)
                write.write_data(data)
                print("\nStock sold Successfully")
                break
        else:
            print("\nThis product is not in the inventory.\n")



def get_yes_no(message):
    """
    Prompts the user for a yes/no response and validates the input.

    Parameters:
        message (str): The prompt message to display to the user.

    Returns:
        bool: True if user enters 'y', False if user enters 'n'.
    """
    while True:
        yes_no = input(message)
        if yes_no.lower() == 'y':
            return True
        elif yes_no.lower() == 'n':
            return False
        else:
            print("Only 'y' or 'n' is accepted.\n")

def valid_user_input(input_message):
    """
    Prompts the user for a positive integer input and validates it.

    Parameters:
        input_message (str): The prompt message to display to the user.

    Returns:
        int: The validated positive integer entered by the user.
    """
    while True:
        try:
            product_quantity = int(input(input_message))
            if product_quantity <= 0:
                print("\nNumber cannot be in negative.\n")
                continue
            break
        except ValueError:

            print("\nPlease enter a valid integer.\n")
            continue
    return product_quantity

def is_already_exist(data, product_name):
    """
    Checks if a product with the given name already exists in the inventory.

    Parameters:
        data (list): List of existing products.
        product_name (str): Name of the product to check.

    Returns:
        bool: True if the product exists, False otherwise.
    """
    is_available = False
    for each in data:
        if each[0].lower() == product_name.lower():
            is_available = True
            break
    return is_available

def valid_name(vendor_name):
    """
    Prompts the user for a valid name (only alphabets and spaces allowed).
    Keeps asking until a valid name is entered.

    Parameters:
        vendor_name (str): The prompt message to display to the user.

    Returns:
        str: The validated name.
    """
    alphabet = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '
    ]
    while True:
        name = input(vendor_name)
        if name.strip() == "":
            print("Invalid name. Please enter a name containing only alphabets.")
            continue
        for char in name:
            if char not in alphabet:
                print("Invalid name. Please enter a name containing only alphabets.")
                break
            else:
                return name

def is_empty(product_details):
    """
    Prompts the user for a product name and ensures it is not empty.

    Parameters:
        product_details (str): The prompt message to display to the user.

    Returns:
        str: The non-empty product name entered by the user.
    """
    while True:
        name = input(product_details)
        if name.strip() == "":
            print("Product name cannot be empty. Please enter a valid product name.")
        else:
            return name