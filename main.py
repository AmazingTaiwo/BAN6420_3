from Policyholder import Policyholder
from Product import Product
from Payment import Payment


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

# Register Policyholders
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
policyholder1.suspend_policyholder()

# Reactivate product and policyholder
product1.status = 'active'
policyholder1.reactivate_policyholder()

# Suspend policyholder
policyholder2.suspend_policyholder()
