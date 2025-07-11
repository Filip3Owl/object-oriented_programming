class BankAccount:

    account_total = 0

    def __init__(self, cardholder_name, balance):
        self.cardholder_name = cardholder_name
        self.balance = balance

    @classmethod
    def account_open(cls, name, balance):
        new_instance = cls(name, balance)
        cls.account_total += 1
        print(f'Account created for {new_instance.name} with balance of ${new_instance.balance}')
        return new_instance
    
    @classmethod
    def show_total_account(cls):
        print(f'Created accounts: {cls.account_total}')
