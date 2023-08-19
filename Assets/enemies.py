import random as rng
"""All enemies"""
"""
Description:
Shows all enemies for each respective floor with all their abilities and stats
"""


'''Floor 1 - Billy the Bully'''
class floor_01_enemy:
    # define constructor
    def __init__(self,name):
        self.name = name

        # Assign enemy stats
        self.health = 300 # enemy hp
        self.max_health = 300 # max enemy hp
        self.energy = 0 # enemy energy
        self.energy_rate = 20 # energy recovery rate per turn
        self.max_energy = 100 # max energy


        # Assign enemy abilities
        self.abilities = {'Unfriendly Jab':25, 'Name Calling':30}
        self.ultimate = {'Terrible Tackle':75} # enemy ultimate if 100 energy is reached

        # Playable class flag
        self.playable = 0

'''Floor 2 - Debbie Downer'''
class floor_02_enemy:
    # define constructor
    def __init__(self,name):
        self.name = name

        # Assign enemy stats
        self.health = 500 # enemy hp
        self.max_health = 500 # max enemy hp
        self.energy = 0 # enemy energy
        self.energy_rate = 25 # energy recovery rate per turn
        self.max_energy = 100 # max energy


        # Assign enemy abilities
        self.abilities = {'Fierce Slap':30, 'Power Kick':40}
        self.ultimate = {'Impending doubt':100} # enemy ultimate if 100 energy is reached
        self.drain = 20 # as part of their ultimate, they drain player for 20 energy

        # Playable class flag
        self.playable = 0


'''Floor 3 - Slippery Sam'''
class floor_03_enemy:
    # define constructor
    def __init__(self,name):
        self.name = name

        # Assign enemy stats
        self.health = 550 # enemy hp
        self.max_health = 550 # max enemy hp
        self.energy = 0 # enemy energy
        self.energy_rate = 40 # energy recovery rate per turn
        self.max_energy = 200 # max energy


        # Assign enemy abilities
        self.abilities = {'Swift Smack':25, 'Blinding Smack':40}
        self.ultimate = {'Tidal Wave':100} # enemy ultimate if 100 energy is reached
        self.poison_flag = 0 # poison flag to mark poison status
        self.poison_counter = 0 # poison counter to count for 3 turns
        self.poison = 10 # as part of their ultimate, they poison player for 10 hp each turn for 4 turns

        # Playable class flag
        self.playable = 0

'''Floor 4 - Furious Fred'''
class floor_04_enemy:
    # define constructor
    def __init__(self,name):
        self.name = name

        # Assign enemy stats
        self.health = 1000 # enemy hp
        self.max_health = 1000 # max enemy hp
        self.energy = 0 # enemy energy
        self.energy_rate = 25 # energy recovery rate per turn
        self.max_energy = 125 # max energy


        # Assign enemy abilities
        self.abilities = {'Devastating Punch':30, 'Furious uppercut':50}
        self.ultimate = {'Enrage':1.50} # enemy ultimate if 100 energy is reached
        # Ultimate grants 50% more damage indefinitely and stacks per ultimate
        self.ultimate_flag = 0 # flag that determines how many has stacked
        self.bonus_energy = 15 # They get bonus energy per turn

        # Playable class flag
        self.playable = 0


'''Floor 5 - Renjiro, The Titan'''
class final_enemy:
    # define constructor
    def __init__(self, name):
        self.name = name

        # Assign enemy stats
        self.health = 2000  # enemy hp
        self.max_health = 2000  # max enemy hp
        self.energy = 0  # enemy energy
        self.energy_rate = 25  # energy recovery rate per turn
        self.max_energy = 500  # max energy

        # Playable class flag
        self.playable = 0

        # Assign enemy abilities - stage 1 (500 < hp <= 1000)
        self.abilities = {'Double Lance': 25*rng.randint(1,2), 'Ion Cannon': int(50*(1+rng.uniform(0,0.5)))}
        self.ultimate = {'Mega Flare': 1000}  # enemy ultimate if 100 energy is reached
        # player has finite amount of turns to take down boss otherwise it's an automatic game over

    # Assign enemy abilities and increase energy rate- stage 2 (hp <= 500)
    def stage_2(self):
        '''input type: None'''
        '''return type: None'''
        self.abilities = {'Relinquishing stomp': 30*rng.randint(1,3), 'Vaporizing Cannon':int(50*(1+rng.uniform(0,0.75))) }
        self.energy_rate += 10
