from resources import *
from creatures import *
from time import sleep
from random import choice
from textwrap import dedent
from sys import exit
import logging

logging.basicConfig(filename='data.log',level=logging.INFO)

def being(resource1, resource2, creature):
    if resource1.check() == 'gone' or resource2.check() == 'gone':
        creature.deplete()
        creature.deplete()
    else:
        pass

def nature():
    choice([pond, grassland, herd, pack]).grow()
    choice([pond, grassland, herd, pack]).deplete()

# parameters: initial amount, amount of each growth,
# amount of each depletion, and amount of each hunt for animals

# pond = Water(1000, 100, 120)
# grassland = Grass(700, 40, 70)
# herd = Sheep(100, 20, 25, 3)
# pack = Wolf(10, 4, 5, 3)

print("\n")
print("-" * 43)
sleep(1)
print("Eco-Sim ----- Natural environment simulator")
sleep(1)
print("\nCurrent supporting interactions: water - grass - sheep - wolves\n")
sleep(2)
print("Created by Calvin Xu")
sleep(1)
print("-" * 43)
sleep(2)

while True:
    try:
        print("\nPlease input parameters: initial amount, amount of each growth, ")
        print("amount of each depletion, and amount of each hunt for animals.\n")
        sleep(1)
        print("--Separate with coma.--\n")
        sleep(2)
        pond_set = input("Parameters for your pond: ").split(' ')
        grassland_set = input("Parameters for your grassland: ").split(' ')
        herd_set = input("Parameters for your herd of sheep: ").split(' ')
        pack_set = input("Parameters for your pack of wolves: ").split(' ')

        pond = Water(int(pond_set[0]), int(pond_set[1]), int(pond_set[2]))
        grassland = Grass(int(grassland_set[0]), int(grassland_set[1]), int(grassland_set[2]))
        herd = Sheep(int(herd_set[0]), int(herd_set[1]), int(herd_set[2]), int(herd_set[3]))
        pack = Wolf(int(pack_set[0]), int(pack_set[1]), int(pack_set[2]), int(pack_set[3]))
    except ValueError:
        print("\nInvalid parameters. Input again.")
        print(dedent("""
                    Example parameters:
                    pond: 1000 100 120
                    grassland 700 40 70
                    herd 100 20 25 3
                    pack 10 4 5 3
                    """))
        exit(0)


    time = int(input("\nRounds of simulation? "))

    water = []
    grass = []
    sheep = []
    wolves = []

    for i in range(1, time + 1):
        pond.grow()
        grassland.grow()
        being(grassland, pond, herd)
        if herd.amount > 0:
            herd.hunt(grassland)
            herd.hunt(pond)
        else:
            pass
        being(herd, pond, pack)
        if pack.amount > 0:
            pack.hunt(pond)
            pack.hunt(herd)
        else:
            pass
        nature()
        nature()
        print(f"\n------Status Report: Iteration {i}------\n")
        print("Pond: ", pond.amount)
        water.append(pond.amount)
        print("Grassland: ", grassland.amount)
        grass.append(grassland.amount)
        print("Sheep herd: ", herd.amount)
        sheep.append(herd.amount)
        print("Wolf pack: ", pack.amount)
        wolves.append(pack.amount)
        print()
        print("-"* 25)
        print("\n")

    logging.info(f"Ecosim simulation data ({time} iterations):\n")
    logging.info(f"Parameters: Water {pond_set}, Grass {grassland_set}, Sheep {herd_set}, Wolves {pack_set}\n")
    logging.info("Water historical data: {}\n\n".format(water))
    logging.info("Grass historical data: {}\n\n".format(grass))
    logging.info("Sheep historical data: {}\n\n".format(sheep))
    logging.info("Wolves historical data: {}\n\n".format(wolves))

    print("Simulation complete. All data exported to data.log.\n")
    print("-" * 25)
