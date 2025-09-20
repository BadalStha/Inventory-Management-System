import datetime
import operation
def unique_file_name():
    """
    Generates a unique file name string based on the current date and time.

    This function retrieves the current date and time, and formats it into a string
    that can be used as a unique file name for invoices or data files.

    Parameters: None

    Returns:
        str: A unique string representing the current date and time.
    """
    c_time = datetime.datetime.now()
    current_year = c_time.year
    current_month = c_time.month
    current_day = c_time.day
    current_hour = c_time.hour
    current_minute = c_time.minute
    current_second = c_time.second
    current_micro = c_time.microsecond

    current_time = "{}-{}-{}__{}-{}-{}-{}".format(current_year, current_month, current_day, current_hour,
                                                  current_minute, current_second, current_micro)
    return current_time


def write_data(data):
    """
    Writes the inventory data to the 'inventory.txt' file.

    This function overwrites the inventory file with the current list of products,
    saving each product as a comma-separated line.

    Parameters: data (list): List of products, where each product is a list of its attributes.

    Returns: None
    """
    with open('inventory.txt', 'w') as file:
        for each in data:
            file.write("{},{},{},{},{}\n".format(each[0], each[1], each[2], each[3], each[4]))


def invoice_of_add_new_product(invoice_details):
    """
    Generates and writes a purchase invoice for newly added products.

    This function collects vendor details, calculates totals and VAT, and writes
    a formatted invoice file for the new product purchase.

    Parameters: invoice_details (list): List of newly added products for the invoice.

    Returns: None
    """
    vendor_name = operation.valid_name("\nEnter the vendor name: ")
    bill_no = input("Enter the bill no: ")
    contact = input("Enter the contact no: ")
    address = input("Enter the address: ")

    total_amt = 0
    for each in invoice_details:
        total_amt = total_amt + (each[2] * each[3])
    vat_amt = total_amt * 13 / 100
    final_price = total_amt + vat_amt
    file_name = "new_product_purchase_" + unique_file_name() + ".txt"

    with open(file_name, 'w') as file:
        file.write("=======================New Product Purchase Invoice=======================")
        file.write("\nVendor name: " + vendor_name + " \n")
        file.write("Bill No: " + bill_no + " \n")
        file.write("Contact No :" + contact + " \n")
        file.write("Address: " + address + " \n")

        file.write("\n--------------------------------------------------------------------------")
        file.write("\nName               | Quantity           | Price              | Total price\n")

        for each in invoice_details:
            file.write("--------------------------------------------------------------------------\n")
            file.write('{:<20} {:<20} {:<20} {:<20}\n'.format(each[0], each[2], each[3], each[2] * each[3]))
        file.write("--------------------------------------------------------------------------\n")

        file.write("\nTotal Amount: {} \t".format(total_amt))
        file.write("VAT Amount: {}\n".format(vat_amt))
        file.write("Total Price: {}".format(final_price) + "\n")
        file.write("==========================================================================")


def invoice_of_new_stock(invoice_details):
    """
    Generates and writes a purchase invoice for added stock.

    This function collects vendor details, calculates totals and VAT, and writes
    a formatted invoice file for the stock purchase.

    Parameters: invoice_details (list): List of stock items added for the invoice.

    Returns: None
    """
    vendor_name = operation.valid_name("\nEnter the Vendor name: ")
    bill_no = input("Enter the bill no: ")
    contact = input("Enter the contact no: ")
    address = input("Enter the address: ")

    total_amount = 0
    for each in invoice_details:
        total_amount += each[2] * each[3]

    vat_amount = total_amount * 13 / 100
    final_price = total_amount + vat_amount
    file_name = "new_stock_purchase_" + unique_file_name() + ".txt"

    with open(file_name, 'w') as file:
        file.write("======================Product Stock Purchase Invoice======================")
        file.write("\nVendor name:" + vendor_name + " \n")
        file.write("Bill No:" + bill_no + " \n")
        file.write("Contact No:" + contact + " \n")
        file.write("Address:" + address + " \n")

        file.write("\n--------------------------------------------------------------------------")
        file.write("\nName               | Quantity           | Price              | Total price\n")

        for each in invoice_details:
            file.write("--------------------------------------------------------------------------\n")
            file.write('{:<20} {:<20} {:<20} {:<20}\n\n'.format(each[0], each[1], each[2], each[2] * each[3]))
        file.write("--------------------------------------------------------------------------\n")

        file.write("\nTotal amt {} \t".format(total_amount))
        file.write("VAT amt {}\n".format(vat_amount))
        file.write("Grand total {}".format(final_price))
        file.write("==========================================================================")

def invoice_of_sales_product(invoice_details):
    """
    Generates and writes a sales invoice for sold products.

    This function collects customer details, calculates totals, discounts, and VAT,
    and writes a formatted invoice file for the sales transaction.

    Parameters: invoice_details (list): List of sold products for the invoice.

    Returns: None
    """
    customer_name = operation.valid_name("\nEnter the customer name: ")
    bill_no = input("Enter the bill no: ")
    contact = input("Enter the contact no: ")
    address = input("Enter the address: ")

    total_amount = 0
    for each in invoice_details:
        total_amount = each[6]

    vat_amount = total_amount * 13 / 100
    final_price = total_amount + vat_amount
    file_name = "sales_" + unique_file_name() + ".txt"

    with open(file_name, 'w') as file:
        file.write("===================================SpeedzWear Private Wholesaler=====================================")
        file.write("\n===========================================Sales Invoice=============================================")
        file.write("\nCustomer name: " + customer_name + " \n")
        file.write("Bill No:" + bill_no + " \n")
        file.write("Contact No:" + contact + " \n")
        file.write("Address:" + address + " \n")

        file.write("\n-----------------------------------------------------------------------------------------------------")
        file.write("\nShoes Name     | Shoes Brand    | Quantity       | Price          | Discount Amount     | Total price   \n")

        for each in invoice_details:
            file.write("-----------------------------------------------------------------------------------------------------\n")
            file.write('{:<15}| {:<15}| {:<15}| {:<15}| {:<20.2f}| {}\n'.format(each[0], each[1], each[2], each[3] , each[5], each[6]))
        file.write("-----------------------------------------------------------------------------------------------------\n")
        file.write("\nTotal Amount: {} \t".format(total_amount))
        file.write("VAT Amount: {}\n".format(vat_amount))
        file.write("Total Price: {}".format(final_price))
        file.write("\n=====================================================================================================")
