from random import randint
from time import sleep
from RandomNamesList import random_name, random_attack


class Chicken:
    def __init__(self):
        self.name = random_name()
        self.health = randint(20, 40)
        self.attack = randint(6, 10)
        self.defense = randint(0, 5)
        self.speed = randint(1, 10)

    def __str__(self):
        return f"""Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {
        self.speed}"""


# Attack function.
def attack(attacker, defender):

    # If attack misses:
    if randint(0, 50) in range(0, defender.speed):
        print('{} Missed!\n'.format(attacker.name))
        sleep(3.5)

    # If critical hit occurs:
    elif randint(0, 100) in range(5):
        defender.health -= (2 * attacker.attack)
        print("{} scored critical hit against {}! {}'s health decreased to {}\n".format(attacker.name,
                                                                                        defender.name, defender.name,
                                                                                        defender.health))
        sleep(3.5)

    # Normal hits:
    else:
        defender.health -= abs(attacker.attack - randint(0, defender.defense))
        print("{} {} {}! {}'s health decreased to {}!\n".format(attacker.name, random_attack(), defender.name,
                                                                defender.name,
                                                                defender.health))
        sleep(3.5)


# Battle function.
def battle(chicken_1, chicken_2):
    # Allows second to go first if first has lower speed.
    if chicken_1.speed < chicken_2.speed:
        attack(chicken_2, chicken_1)

    # Loops while both chickens still have health.
    while chicken_1.health > 0 and chicken_2.health > 0:

        attack(chicken_1, chicken_2)
        if chicken_2.health <= 0:
            break

        attack(chicken_2, chicken_1)
        if chicken_1.health <= 0:
            break

    if chicken_1.health <= 0:
        print('{} Wins!'.format(chicken_2.name))
        return chicken_2
    else:
        print('{} Wins!'.format(chicken_1.name))
        return chicken_1


if __name__ == '__main__':
    print("Christopher's Cock-Fighting Simulator!!!\n7.8/10 IGN- 'Too many cock-fights'\nDisapproved by PETA!\n")
    PlayerMoney = 100

    while PlayerMoney > 0:

        FirstChicken = Chicken()
        SecondChicken = Chicken()
        while FirstChicken.name == SecondChicken.name:
            FirstChicken = Chicken()
            SecondChicken = Chicken()

        # Player selects their chicken to bet on.
        while True:
            chicken_choice = str(input(
                f'''Choose Your Chicken:\n{FirstChicken}\n[1] Select {FirstChicken.name}\n\n{SecondChicken}\n[2] Select {SecondChicken.name}\n'''))
            if chicken_choice == '1':
                PlayerChickenBet = FirstChicken
                break
            if chicken_choice == '2':
                PlayerChickenBet = SecondChicken
                break
            else:
                print('Invalid Selection')
                sleep(2)
                continue

        # Deals with the player's betting.
        PlayerBet = -1
        while PlayerBet > PlayerMoney or PlayerBet < 0:
            try:
                PlayerBet = int(input("Place bet under £{}: £".format(PlayerMoney)))
            except ValueError:
                print("Invalid Amount")
                sleep(2)
                continue
            if PlayerBet > PlayerMoney:
                print("Insufficient Funds")
                sleep(2)
                continue

        # Commence Battle:
        if battle(FirstChicken, SecondChicken) == PlayerChickenBet:
            print('You Won £{}!\n'.format(PlayerBet))
            PlayerMoney += PlayerBet
            sleep(3.5)
        else:
            print('You Lose £{}!\n'.format(PlayerBet))
            PlayerMoney -= PlayerBet
            sleep(3.5)

    print('Game Over!')
