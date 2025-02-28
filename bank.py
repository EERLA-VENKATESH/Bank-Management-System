class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.account_number] = customer

    def get_customer(self, account_number):
        return self.customers.get(account_number, None)
