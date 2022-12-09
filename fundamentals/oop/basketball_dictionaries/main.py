
# Class for Player. Takes a basketball player dictionary as a parameter.
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    @classmethod
    def get_team(cls, team_list):
        players = []

        for member in team_list:
            players.append(Player(member))

        return players

    def display_player_info(self):
        print('\n' + ('-' * 20) )
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        print()

        return self

if __name__ == '__main__':

    # Below are several dictionaries of different basketball players
    kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    }
    jason = {
            "name": "Jason Tatum", 
            "age":24, 
            "position": "small forward", 
            "team": "Boston Celtics"
    }
    kyrie = {
            "name": "Kyrie Irving", 
            "age":32, "position": "Point Guard", 
            "team": "Brooklyn Nets"
    }

    players = [kevin, jason, kyrie]
    
    # Player Instances
    player_kevin = Player(kevin)
    player_jason = Player(jason)
    player_kyrie = Player(kyrie)

    # List of players instatiated into Player objects and added to a team list
    new_team = []

    for player in players:
        new_team.append(Player(player))

    # Create team list with class method from Player class

    bonus_team = Player.get_team(players)

    for member in bonus_team:
        member.display_player_info()


