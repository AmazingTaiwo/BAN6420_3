# Create classes for Product
class Product:
    def __init__(staff, product_id, name, price):
        staff.product_id = product_id
        staff.name = name
        staff.price = price
        staff.status = 'active'  # Product is active by default

    # Method to Display Product details
    def display_account_details(staff):
        print(f"Product: {staff.name}, Status: {staff.status}")
        print(f"Price: {staff.price}")

    # Method to Create Product
    def create_product(staff):
        staff.status = 'created'
        print(f"Product {staff.product_id} has been created.")

    # Method to Update Product details
    def update_product(staff, name=None, price=None):
        if name:
            staff.name = name
        if price:
            staff.price = price
        print(f"Product {staff.product_id} updated.")


    # Suspend Product
    def remove_product(staff):
        staff.status = 'removed'
        print(f"Product {staff.product_id} has been removed.")

    # Reactivate Product
    def reactivate_product(staff):
        staff.status = 'reactivated'
        print(f"Product {staff.product_id} has been reactivated.")
