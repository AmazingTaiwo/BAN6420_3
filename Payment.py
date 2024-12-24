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