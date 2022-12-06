class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print()
        print('-' * 10)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(f'Rewards Member: {self.is_rewards_member}')
        print(f'Gold Card Points: {self.gold_card_points}')
        print()
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("Already enrolled in rewards member program")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points")

        return self

if __name__ == '__main__':
    user1 = User("Joe", "K", "joek@email.com", 32)
    user1.display_info().enroll().spend_points(50).display_info()

    user2 = User("Some", "Body", "somebody@email.com", 52)
    user2.enroll().spend_points(80).display_info()
