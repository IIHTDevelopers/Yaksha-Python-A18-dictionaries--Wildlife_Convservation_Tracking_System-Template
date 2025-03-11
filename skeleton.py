"""
Online Store Management System
This program demonstrates dictionary operations through an online store inventory management system.
"""

def initialize_data():
    """
    Initialize the store inventory with predefined products and categories using dictionaries.
    
    Returns:
        tuple: A tuple containing (inventory, new_products) dictionaries
    """
    # TODO: Create the main product inventory dictionary with these exact products:
    # P001: Smartphone XS (electronics, ₹59999.99, 25 in stock, 4.5 rating, features: 5G, 128GB Storage, Dual Camera)
    # P002: Designer Jeans (clothing, ₹4999.99, 40 in stock, 4.2 rating, features: Slim Fit, Stretch Denim, Dark Wash)
    # P003: Bluetooth Headphones (electronics, ₹7999.99, 15 in stock, 4.7 rating, features: Noise Cancelling, 40hr Battery, Hi-Fi Sound)
    # P004: Organic Coffee Beans (groceries, ₹899.99, 50 in stock, 4.8 rating, features: Fair Trade, Whole Bean, Medium Roast)
    # P005: Running Shoes (footwear, ₹6999.99, 30 in stock, 4.6 rating, features: Breathable, Cushioned, Lightweight)
    inventory = {}
    
    # TODO: Create new products dictionary with these exact products:
    # N001: Smart Watch (electronics, ₹15999.99, 20 in stock, 4.4 rating, features: Heart Rate Monitor, GPS, Water Resistant)
    # N002: Protein Powder (health, ₹1999.99, 45 in stock, 4.3 rating, features: Plant-Based, 20g Protein, Sugar-Free)
    new_products = {}
    
    return inventory, new_products

def filter_by_category(inventory, category):
    """
    Filter products by category using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        category (str): Category to filter by
    
    Returns:
        dict: Filtered products dictionary
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if category is None:
        raise ValueError("Category cannot be None")
    
    # TODO: Implement dictionary comprehension to filter products by category
    # Hint: Use {key: value for key, value in dict.items() if condition}
    
    return {}

def filter_by_price_range(inventory, min_price, max_price):
    """
    Filter products by price range using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        min_price (float): Minimum price
        max_price (float): Maximum price
    
    Returns:
        dict: Filtered products dictionary
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if min_price is None or max_price is None:
        raise ValueError("Price range cannot be None")
    if min_price > max_price:
        raise ValueError("Minimum price cannot be greater than maximum price")
    
    # TODO: Implement dictionary comprehension to filter products by price range
    # Hint: Filter products where min_price <= product["price"] <= max_price
    
    return {}

def filter_by_availability(inventory, min_stock=1):
    """
    Filter products by availability using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        min_stock (int): Minimum stock level required
    
    Returns:
        dict: Filtered products dictionary
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if min_stock < 0:
        raise ValueError("Minimum stock cannot be negative")
    
    # TODO: Implement dictionary comprehension to filter products by availability
    # Hint: Filter products where product["stock"] >= min_stock
    
    return {}

def filter_by_feature(inventory, feature):
    """
    Filter products by a specific feature using dictionary comprehension.
    
    Args:
        inventory (dict): The product inventory
        feature (str): Feature to filter by
    
    Returns:
        dict: Filtered products dictionary
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if feature is None:
        raise ValueError("Feature cannot be None")
    
    # TODO: Implement dictionary comprehension to filter products by feature
    # Hint: Filter products where feature is in product["features"] list
    
    return {}

def find_products_with_keyword(inventory, keyword):
    """
    Find products containing a keyword in their name or features.
    
    Args:
        inventory (dict): The product inventory
        keyword (str): Keyword to search for
    
    Returns:
        dict: Filtered products dictionary
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if keyword is None:
        raise ValueError("Keyword cannot be None")
    
    # TODO: Implement dictionary comprehension to find products with the keyword
    # Hint: Convert keyword to lowercase and check if it's in product name or any feature
    # Hint: Use the any() function with a generator expression for checking features
    
    return {}

def update_product_price(inventory, product_id, new_price):
    """
    Update a product's price.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        new_price (float): New price
    
    Returns:
        dict: Updated inventory
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if new_price is None or new_price < 0:
        raise ValueError("New price cannot be None or negative")
    
    # Check if product exists
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # TODO: Create a new dictionary with the updated price
    # Hint: First create a copy of the inventory
    # Hint: Use dictionary unpacking (**) to create a new product dictionary with updated price
    
    return {}

def update_stock_level(inventory, product_id, quantity_change):
    """
    Update a product's stock level.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        quantity_change (int): Amount to change stock by (positive or negative)
    
    Returns:
        dict: Updated inventory
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if quantity_change is None:
        raise ValueError("Quantity change cannot be None")
    
    # Check if product exists
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # TODO: Create a new dictionary with the updated stock
    # Hint: Calculate new stock level and validate it's not negative
    # Hint: Use dictionary unpacking to create a new product dictionary with updated stock
    
    return {}

def add_product_feature(inventory, product_id, new_feature):
    """
    Add a new feature to a product.
    
    Args:
        inventory (dict): The product inventory
        product_id (str): Product ID to update
        new_feature (str): New feature to add
    
    Returns:
        dict: Updated inventory
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    if product_id is None:
        raise ValueError("Product ID cannot be None")
    if new_feature is None or new_feature == "":
        raise ValueError("New feature cannot be None or empty")
    
    # Check if product exists
    if product_id not in inventory:
        raise ValueError(f"Product ID {product_id} not found")
    
    # TODO: Create a new dictionary with the updated features
    # Hint: First check if the feature already exists
    # Hint: Create a copy of the features list and append the new feature
    # Hint: Use dictionary unpacking to create a new product dictionary with updated features
    
    return {}

def merge_inventories(existing_inventory, new_products):
    """
    Merge two inventory dictionaries with transformation.
    
    Args:
        existing_inventory (dict): The existing product inventory
        new_products (dict): New products to add
    
    Returns:
        dict: Merged inventory
    """
    # Input validation
    if existing_inventory is None or new_products is None:
        raise ValueError("Inventories cannot be None")
    
    # TODO: Create a copy of the existing inventory
    # TODO: Add new products with a "new_arrival" flag set to True
    # Hint: Use dictionary unpacking to add the new_arrival flag
    
    return {}

def calculate_category_counts(inventory):
    """
    Calculate the number of products in each category.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        dict: Dictionary with categories as keys and counts as values
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    # TODO: Create a dictionary of category counts
    # Hint: Iterate through inventory.values() and count products in each category
    
    return {}

def calculate_total_inventory_value(inventory):
    """
    Calculate the total value of inventory (price * stock).
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        float: Total inventory value
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    # TODO: Calculate and return the total inventory value
    # Hint: Use sum() with a generator expression that multiplies price by stock
    
    return 0.0

def find_highest_rated_product(inventory):
    """
    Find the highest rated product.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        tuple: (product_id, product_data) of the highest rated product
    """
    # Input validation
    if inventory is None or not inventory:
        raise ValueError("Inventory cannot be None or empty")
    
    # TODO: Find and return the product with the highest rating
    # Hint: Use max() with a key function that extracts the rating
    
    return ("", {})

def create_price_brackets(inventory):
    """
    Group products into price brackets.
    
    Args:
        inventory (dict): The product inventory
    
    Returns:
        dict: Dictionary with price brackets as keys and lists of product IDs as values
    """
    # Input validation
    if inventory is None:
        raise ValueError("Inventory cannot be None")
    
    # TODO: Create price brackets dictionary with these ranges:
    # "budget": 0-3000
    # "mid_range": 3000-10000
    # "premium": 10000+
    price_brackets = {
        "budget": [],
        "mid_range": [],
        "premium": []
    }
    
    # TODO: Categorize each product into the appropriate price bracket
    # Hint: Iterate through inventory.items() and check the price of each product
    
    return price_brackets

def get_formatted_product(pid, product):
    """
    Format a product for display.
    
    Args:
        pid (str): Product ID
        product (dict): Product data
    
    Returns:
        str: Formatted product string
    """
    # Input validation
    if product is None:
        raise ValueError("Product cannot be None")
    
    # TODO: Format the product for display
    # Hint: Format the rating as stars (★ and ☆)
    # Hint: Join features with commas
    # Hint: Add [NEW] tag for new arrivals
    
    return ""

def display_data(data, data_type):
    """
    Display formatted data based on data type.
    
    Args:
        data: Data to display (dict, tuple, etc.)
        data_type (str): Type of data being displayed
    """
    if data is None:
        print("No data to display.")
        return
    
    # TODO: Implement display logic for different data types:
    # "inventory", "filtered" - display formatted products
    # "categories" - display category counts
    # "price_brackets" - display products in each price bracket
    # "highest_rated" - display the highest rated product
    # "inventory_value" - display the total inventory value
    
    pass

def main():
    """Main program function."""
    inventory, new_products = initialize_data()
    
    while True:
        # Show basic info about the inventory
        categories = set(product["category"] for product in inventory.values())
        
        print(f"\n===== ONLINE STORE MANAGEMENT SYSTEM =====")
        print(f"Total Products: {len(inventory)}")
        print(f"Categories: {', '.join(sorted(categories))}")
        
        print("\nMain Menu:")
        print("1. View Inventory")
        print("2. Filter Products")
        print("3. Update Products")
        print("4. Add New Products")
        print("5. View Statistics")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        # TODO: Implement menu handling logic
        # Hint: Use if/elif/else statements to handle different menu options
        
        pass

if __name__ == "__main__":
    main()