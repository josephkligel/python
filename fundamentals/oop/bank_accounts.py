class BankAccount:

    def __init__(self,  interest_rate, balance = 0.00):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("\nInsufficient funds: Charging $5 fee\n")
            self.balance -= 5

        return self

    def display_account_info(self):
        print(f'\nBalance: ${self.balance}\n')
        return self
    
    def yield_interest(self):
        self.balance *= (1 + self.interest_rate)
        return self

if __name__ == '__main__':
    account1 = BankAccount(0.01)
    account2 = BankAccount(0.05)

    account1.deposit(10).deposit(25).deposit(55).withdraw(35).yield_interest().display_account_info()

    account2.deposit(60).deposit(105).withdraw(10).withdraw(40).withdraw(60).withdraw(135).yield_interest().display_account_info()