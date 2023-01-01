from classes.ninja import Ninja
from classes.pirate import Pirate

# Determines which battle contestant is faster
# The fast contestant is put a the beginning of the contestants list. The first contestant attacks first
def start(ninja, pirate):
    contestants = [ninja, pirate]
    ninja.show_stats()
    pirate.show_stats()

    if(ninja.speed < pirate.speed):
        contestants = contestants.reverse()

    return contestants

# Given a list of contestants, the contestants begin the battle
# Based on the turn_counter, the contestants alternate between who attacks
def battle(contestants):
    turn_counter = 0

    while(contestants[0].health > 0 or contestants[1].health > 0):
        if turn_counter % 2 == 0:
            contestants[0].attack(contestants[1])
        else:
            contestants[1].attack(contestants[0])

        if(contestants[0].health <= 0 or contestants[1].health <= 0):
            break
        else:
            turn_counter += 1

    # Game is over. Winner is chosen and presented
    print('\nGame Over')
    print('-' * 20)
    print(f'The game took {turn_counter} turns')
    winner = contestants[1] if contestants[0].health <= 0 else contestants[0]
    print(f'\nWinner is the {winner.__class__.__name__}: {winner.name}!')
        
# A ninja and pirate contestant is created and begin battle
# The one who has a health of 0 or below loses
if __name__ == '__main__':
    # Battlees are initialized
    michelangelo = Ninja("Michelanglo")

    jack_sparrow = Pirate("Jack Sparrow")

    # Contenstant list is created
    contestants = start(michelangelo, jack_sparrow)

    # Battle begins
    battle(contestants)