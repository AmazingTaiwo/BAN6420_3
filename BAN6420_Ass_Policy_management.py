# Create separate classes for Policyholders
class Policyholder:
    def __init__(staff, policyholder_id, name):
        staff.policyholder_id = policyholder_id
        staff.name = name
        staff.status = 'active'  # By default, a policyholder is active
        staff.products = []
        staff.payments = []
        
# Register Policyholder
    def register(staff):
        staff.status = 'active'
        print(f"Policyholders {staff.name} has been registered.")

# Update Policyholder details
    def update_policyholder(staff, name=None):
        if name:
            staff.name = name
        print(f"Policyholder {staff.policyholder_id} updated.")

# Suspend Policy Holder
    def suspend(staff):
        staff.status = 'suspended'
        print(f"Policyholder {staff.name} has been suspended.")

# Reativate Policy Holder
    def reactivate(staff):
        staff.status = 'active'
        print(f"Policyholder {staff.name} has been reactivated.")

#Payment Management
    # Payment Processing
    # Add Payment
    def add_payment(staff, payment):
        staff.payments.append(payment)
        print(f"Payment of {payment.amount} has been added to {staff.name}'s account.")

    # Display Account Details
    def display_account_details(staff):
        print(f"Policyholder: {staff.name}, Status: {staff.status}")
        print(f"Payments: {[payment.amount for payment in staff.payments]}")
        print(f"Products: {[product.name for product in staff.products]}")

    # Product Management
    # Add Product
    def add_product(staff, product):
        if product.status == 'active':
            staff.products.append(product)
            print(f"{staff.name} has been enrolled in product {product.name}.")


# Create classes for Product
class Product:
    def __init__(staff, product_id, name, price):
        staff.product_id = product_id
        staff.name = name
        staff.price = price
        staff.status = 'active'  # Product is active by default

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
        staff.status = 'removed'
        print(f"Product {staff.product_id} has been removed.")

# Create classes for Payment
class Payment:
    def __init__(staff, amount, policyholder, product):
        staff.amount = amount
        staff.policyholder = policyholder
        staff.product = product
        staff.status = 'processed'  # Payment status can be processed or pending

    # Method to Process Payment
    def process_payment(staff):
        print(f"Payment of {staff.amount} for {staff.product.name} has been processed for {staff.policyholder.name}.")
        staff.policyholder.add_payment(staff)
        staff.product.status = 'active'  # Product remains active after successful payment

    # Metgod to Send Reminder
    def send_reminder(staff):
        print(f"Reminder: Payment of {staff.amount} is due for {staff.product.name} by {staff.policyholder.name}.")

    # Method to Apply Penalties
    def apply_penalty(staff):
        penalty = 10  # Example penalty amount
        print(f"Penalty of {penalty} applied to {staff.policyholder.name} for {staff.product.name}.")
        staff.policyholder.add_payment(staff)


# Product Management
# Method to Create products
product1 = Product(1, "Health Insurance", 150)
product2 = Product(2, "Car Insurance", 200)
product3 = Product(3, "House Insurance", 500)

# Policyholder Demonstration
# policyholders Creation
policyholder1 = Policyholder(401, "Jark Clark")
policyholder2 = Policyholder(402, "Averi Kumar")
policyholder3 = Policyholder(403, "Rakesh Olye")

# Register policyholders
policyholder1.register()
policyholder2.register()
policyholder3.register()

# Policyholders enroll in products
policyholder1.add_product(product1)
policyholder2.add_product(product2)
policyholder3.add_product(product3)

# Process payments
payment1 = Payment(150, policyholder1, product1)
payment1.process_payment()

payment2 = Payment(200, policyholder2, product2)
payment2.process_payment()

payment3 = Payment(500, policyholder3, product3)
payment3.process_payment()

# Display account details for policyholders
policyholder1.display_account_details()
policyholder2.display_account_details()
policyholder3.display_account_details()

# Suspend product and policyholder
product1.remove_product()
policyholder1.suspend()

# Reactivate product and policyholder
product1.status = 'active'
policyholder1.reactivate()

# Suspend policyholder
policyholder2.suspend()
