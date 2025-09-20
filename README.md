# SpeedzWear Inventory Management System

A Python-based command-line inventory management system designed for managing product stock, sales, and purchases with automatic invoice generation.

## Features

- **Product Display**: View all products in a formatted table with details including name, brand, quantity, price, and origin
- **Add New Products**: Add new products to the inventory with validation and duplicate checking
- **Stock Management**: Add stock to existing products with automatic quantity updates
- **Sales Processing**: Process product sales with automatic discount calculation and stock deduction
- **Invoice Generation**: Automatic generation of invoices for purchases, stock additions, and sales
- **Data Persistence**: All inventory data is stored in `inventory.txt` file
- **Input Validation**: Comprehensive validation for user inputs

## Discount System

The system applies automatic discounts for bulk purchases (>10 items):
- **Domestic products**: 7% discount
- **International products**: 5% discount

## File Structure

```
Inventory-Management-System/
├── main.py           # Main program entry point and menu system
├── operation.py      # Core business logic and operations
├── read.py          # File reading operations
├── write.py         # File writing and invoice generation
├── inventory.txt    # Inventory data storage (CSV format)
└── README.md        # This documentation file
```

## Prerequisites

- Python 3.x
- No external dependencies required (uses only built-in Python libraries)

## Installation & Setup

1. Clone or download the project files
2. Ensure all Python files are in the same directory
3. Create an `inventory.txt` file in the same directory with initial product data (optional)

### Sample `inventory.txt` format:
```
Loafer Light,GoldStar,200,1000,domestic
Inigo 732,Caliber,100,2800,domestic
Lite Racer,Adidas,200,7000,international
Air Force 1,Nike,250,4000,international
```

**Format**: `ProductName,Brand,Quantity,Price,Origin`

## Usage

1. Run the main program:
   ```bash
   python main.py
   ```

2. Select from the menu options:
   - **1**: Display all products in inventory
   - **2**: Add a new product to inventory
   - **3**: Add stock to existing products
   - **4**: Sell products (process sales)
   - **5**: Exit the system

## Menu Options Explained

### 1. Display Products
Shows all products in a formatted table with columns:
- Name
- Brand  
- Quantity
- Price
- Origin (domestic/international)

### 2. Add New Product
- Enter product details (name, brand, quantity, price, origin)
- System checks for duplicates
- Generates purchase invoice
- Updates inventory file
- Allows adding multiple products in one session

### 3. Add Stock
- Select existing product by name
- Enter quantity to add
- Updates total stock quantity
- Generates stock invoice
- Allows adding stock for multiple products

### 4. Sell Product
- Select product by name
- Enter quantity to sell
- Automatic discount calculation for bulk orders
- Stock availability checking
- Generates sales invoice
- Updates remaining stock

### 5. Exit System
Safely closes the program with a farewell message.

## Data Storage

- **Primary Storage**: `inventory.txt` (CSV format)
- **Invoices**: Generated with timestamps for purchases, stock additions, and sales
- **Format**: All data stored as comma-separated values

## Input Validation

The system includes comprehensive validation:
- **Numeric inputs**: Ensures positive integers for quantities and prices
- **Text inputs**: Validates product names are not empty
- **Names**: Vendor names accept only alphabets and spaces
- **Yes/No prompts**: Accepts only 'y' or 'n' responses
- **Duplicate checking**: Prevents adding duplicate products

## Error Handling

- **File not found**: Gracefully handles missing `inventory.txt`
- **Invalid inputs**: Continuous prompting until valid input is provided
- **Insufficient stock**: Prevents overselling with appropriate messages
- **Empty inventory**: Handles empty inventory scenarios

## Invoice System

The system automatically generates timestamped invoices for:
- New product purchases
- Stock additions
- Product sales

Invoice files are named with current date and time for uniqueness.

## Example Workflow

1. Start the program: `python main.py`
2. Choose option 1 to view current inventory
3. Choose option 2 to add new products
4. Choose option 3 to restock existing items
5. Choose option 4 to process sales
6. Choose option 5 to exit

## Contributing

This is a standalone educational project. Feel free to:
- Add new features
- Improve the user interface
- Enhance validation
- Add database support
- Implement GUI interface

## License

This project is open source and available under standard terms.

## Support

For issues or questions:
- Review the code documentation
- Check input validation requirements
- Ensure `inventory.txt` format is correct
- Verify Python 3.x installation

---

**Note**: Make sure to backup your `inventory.txt` file regularly as it contains all your inventory data.