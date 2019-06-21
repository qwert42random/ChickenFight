from random import randint
from time import sleep
from RandomNamesList import random_name, random_attack_verb


# Chicken class
class Chicken:
    def __init__(self):
        self.name = random_name()
        self.health = randint(20, 30)
        self.attack = randint(6, 10)
        self.defense = randint(0, 5)
        self.speed = randint(0, 10)

    def __str__(self):
        return "Name: {}\nHealth: {}\nAttack: {}\nDefense: {}\nSpeed: {}".format(self.name, self.health, self.attack,
                                                                                 self.defense, self.speed)


# Attack function.
def attack(attacker, defender):
    attack_verb = random_attack_verb()
    initial_defender_health = defender.health

    # Simulates attack misses:
    if randint(0, 40) in range(0, defender.speed):
        print('{} Missed!\n'.format(attacker.name))
        sleep(3.5)

    # If critical hit occurs:
    elif randint(0, 100) in range(5):
        defender.health -= (2 * attacker.attack)

        attack_verb = "scored a critical hit against"

    # Normal hits:
    else:
        defender.health -= abs(attacker.attack - randint(0, defender.defense))

    # Prevents health falling below 0.
    if defender.health < 0:
        defender.health = 0

    print("{0:} {1:} {2:}! {2:}'s health decreased from {4:} to {3:}!\n".format(attacker.name, attack_verb,
                                                                                defender.name,
                                                                                defender.health,
                                                                                initial_defender_health))
    sleep(3.5)


# Battle function.
def battle(chicken_1, chicken_2):
    # Allows second to go first if first has lower speed.
    if chicken_1.speed < chicken_2.speed:
        attack(chicken_2, chicken_1)

    # Loops while both chickens still have health.
    while chicken_1.health > 0 and chicken_2.health > 0:

        attack(chicken_1, chicken_2)
        chicken_1, chicken_2 = chicken_2, chicken_1

    # Prints and returns the winner.
    print('{} Wins!'.format(chicken_2.name))
    return chicken_2


if __name__ == '__main__':
    print("Christopher's Cock-Fighting Simulator!!!\n7.8/10 IGN- 'Too many cock-fights'\nDisapproved by PETA!\n")
    PlayerMoney = 100

    while PlayerMoney > 0:

        FirstChicken = Chicken()
        SecondChicken = Chicken()
        PlayerChickenBet = None

        # Prevents chicken with the same name being generated.
        while FirstChicken.name == SecondChicken.name:
            SecondChicken = Chicken()

        # Player selects their chicken to bet on.
        while True:
            chicken_choice = input(
                "Choose Your Chicken:\n{}\n[1] Choose {}\n\n{}\n[2] Choose {}\n".format(FirstChicken, FirstChicken.name,
                                                                                        SecondChicken,
                                                                                        SecondChicken.name))
            if chicken_choice == '1':
                PlayerChickenBet = FirstChicken
                break
            elif chicken_choice == '2':
                PlayerChickenBet = SecondChicken
                break
            else:
                print('Invalid Selection')
                sleep(2)

        # Deals with the player's betting.
        PlayerBet = None
        while True:
            try:
                PlayerBet = int(input("Place bet under £{}: £".format(PlayerMoney)))
                if PlayerBet < 0 or PlayerBet > PlayerMoney:
                    print("Invalid Amount")
                else:
                    break
            except ValueError:
                print("Invalid Amount")
                continue

        # Commence battle and determine winner:
        if battle(FirstChicken, SecondChicken) == PlayerChickenBet:
            print('You Won £{}!\n'.format(PlayerBet))
            PlayerMoney += PlayerBet
        else:
            print('You Lose £{}!\n'.format(PlayerBet))
            PlayerMoney -= PlayerBet
        sleep(3.5)

    print('Game Over!')
