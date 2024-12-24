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

# Display Policyholder Details
    def display_account_details(staff):
        print(f"Policyholder: {staff.name}, Status: {staff.status}")
        print(f"Payments: {[payment.amount for payment in staff.payments]}")
        print(f"Products: {[product.name for product in staff.products]}")

# Payment Management
    # Payment Processing
    # Add Payment
    def add_payment(staff, payment):
        staff.payments.append(payment)
        print(f"Payment of {payment.amount} has been added to {staff.name}'s account.")

# Product Management
 # # Add Product
    def add_product(staff, product):
        if product.status == 'active':
            staff.products.append(product)
            print(f"{staff.name} has been enrolled in product {product.name}.")
