import read
import operation

def main():
    """
    Runs the main menu loop for the SpeedzWear Inventory Management System.

    Displays menu options to the user, processes user input, and calls the appropriate
    functions to display products, add new products, add stock, or sell products.
    Continues to prompt the user until they choose to exit the system.

    Parameters: None

    Returns: None
    """
    try:
        while True:
            print("\nWelcome to the SpeedzWear System!")
            print("What do you want to do? ")
            print("1. To display products")
            print("2. To add a new product")
            print("3. To add stock")
            print("4. To sell a product")
            print("5. To exit from the system")

            user_input = input("\nEnter the option (1-5): ")
            data = read.read_file()

            if data == []:
                if not operation.get_yes_no("\nDo you want to do anything else? (y/n): "):
                    print("The program is closed.")
                    break
                else:
                    continue

            if user_input == '1':
                operation.display_products(data)
            elif user_input == '2':
                operation.add_new_product(data)
            elif user_input == '3':
                operation.add_stock(data)
            elif user_input == '4':
                operation.sales_product(data)
            elif user_input == '5':
                print("\nThank you for using the system, Bye!")
                break
            else:
                print("Invalid input. Please try again.")
                continue

            if not operation.get_yes_no("\nDo you want to do anything else? (y/n): "):
                print("The program is closed.")
                break
    except KeyboardInterrupt:
        print("\nBye!")

main()