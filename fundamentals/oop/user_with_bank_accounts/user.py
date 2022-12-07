from bank_accounts import BankAccount

class User:

    def __init__(self, name, email, interest_rate = 0.02, balance = 0):
        self.name = name
        self.email = email
        self.account = [BankAccount(interest_rate, balance)]

    def make_deposit(self, amount, account_num = 0):
        self.account[account_num].deposit(amount)

        return self

    def make_withdraw(self, amount, account_num = 0):
        self.account[account_num].withdraw(amount)

        return self

    def display_user_balance(self, account_num = 0):
        print(f'\nBalance of {self.name}\'s Account {account_num}: ${self.account[account_num].balance}\n')

        return self

    def create_account(self):
        acc = BankAccount(0.02, 0)
        self.account.append(acc)

        return self

    def transfer(self, amount, to_user, to_num = 0, from_num = 0):
        self.make_withdraw(amount, from_num)

        if(amount > self.account[from_num].balance):
            print("Transfer terminated")
        else:
            to_user.make_deposit(amount, to_num)
        
        return self

if __name__ == '__main__':
    user1 = User('Joe Smith', 'jsmith@email.com')
    user2 = User('Jeff Bezos', 'jbezos@amazon.com', balance=10000000)

    user1.create_account().make_deposit(100, 1).display_user_balance(1).make_withdraw(50, 1).display_user_balance(1)

    user1.display_user_balance().make_deposit(200).display_user_balance().make_withdraw(100).display_user_balance()

    print('-' * 10)

    user2.transfer(5000000000, user1).display_user_balance()

    user1.display_user_balance()




    

