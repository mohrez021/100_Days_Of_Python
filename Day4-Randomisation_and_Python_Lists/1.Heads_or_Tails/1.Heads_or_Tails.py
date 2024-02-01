from random import randint

random_coin_side = randint(0, 1)

if random_coin_side == 0:
    print("Tails")
else:
    print("Heads")
