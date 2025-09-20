def read_file():
    """
    Reads the inventory data from the 'inventory.txt' file.

    Opens the inventory file, reads each line, splits the line into product attributes,
    and returns a list of products. If the file is not found, prints an error message.

    Parameters: None

    Returns:
        list: A list of products, where each product is represented as a list of its attributes.
              Returns None if the file is not found.
    """
    try:
        file_path = 'inventory.txt'
        with open(file_path, 'r') as file:
            data = file.readlines()
            new_list = []
            for each in data:
                each_data = each.strip().split(',')
                new_list.append(each_data)
        return new_list
    except FileNotFoundError:
        print('The stock file is not found or it does not exist. Create inventory.txt file before starting the program.')
        return []