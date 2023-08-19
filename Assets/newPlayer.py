"""Player Creation"""
import TitleScreen as title
import time
import random as rng
from Assets import equipment as equip


"""Choosing a new name and a class"""
# New player class
class newPlayer:
    """ New Player with baseline abilities, starting currency, and starting consumables """
    def __init__(self,name):
        '''input type: string'''
        '''return type: None'''
        self.name = name # assign username from main
        self.coin = 50 # every player starts with 50 gold currency
        self.floor_flag = [0,0,0,0,0] # every player starts with a floor flag to mark completion
        self.class_flag = [0,0,0,0] # determines which class was picked
        self.backpack = ['Basic health potion (Recover 100 hp)','Basic energy potion (Recover 50 ep)'] # every player has a backpack with basic starting items
        # note: The backpack can only hold 4 items max.

        # Playable class flag
        self.playable = 1

    def escape(self): # Every player has the escape ability
        '''input type: None'''
        '''return type: Bool'''
        """Roll a die to see if escape was a success or fail"""
        print(f"{self.name} initiates an escape attempt...")
        time.sleep(3) # set a delay timer here
        # Perform roll for escape
        roll = rng.uniform(0,1)
        if(roll > 0.50): # Successful rolls are above 50%
            print("Successful escape!")
            return True # return true
        else: # failed roll
            print("Failed escape!")
            return False # return false


""" All playable classes"""

'''Warrior class'''
class Warrior(newPlayer): # Takes in parent class for baseline abilities
    def __init__(self,name):
        super().__init__(name) # call from parent class
        # Start assigning stats
        self.str = 6 # Strength
        self.dex = 1 # Dexterity
        self.int = 1 # Intellect
        self.luk = 2 # Luck

        # Assigning health points and energy points
        self.health = 200 # expendable health
        self.energy = 100 # expendable energy
        self.max_health = 200 # max health
        self.max_energy = 100 # max energy
        self.energy_rate = 10 # energy rate per turn

        # Warrior rage counter
        self.rage = 0

        # Assigning gear
        self.attire = equip.chainmail() # Warrior starting attire
        self.weapon = equip.saber() # Warrior starting weapon

        # Name of each warrior ability
        self.abilities = ['Forward Slash (30 EP)', 'Sustained Rage (50 EP)', 'Execute (MAX EP)']

        # Warrior ability cost
        self.cost = [30,50,100]

        # Set class flag for Warrior
        self.class_flag[0] = 1

    '''Every class gets a dodge chance, scales with DEX'''
    def dodge(self):
        return True if rng.random() < (0.10 + self.dex*0.05) else False

    ''' Warrior Abilities '''
    def forward_slash(self):
        '''input type: self'''
        '''return type: int'''
        """Perform forward slash with class multipliers, uses 30 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0,1) + self.luk*(0.05)*(self.weapon[1])
        if(roll > 0.5): # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else: # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + (rage bonus
        attack = (50)*crit*(self.weapon[0]) + (self.str*5) + (self.rage)*(0.50)*(50)

        # decrement rage counter if it was used
        if(self.rage != 0):
            self.rage = 0

        # Change player energy
        self.energy -= 30
        print(f"{self.name} uses Forward slash! \n")
        return(int(attack)) # return the attack value

    def sustained_rage(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform sustained rage with class multipliers, uses 50 EP"""
        if(self.rage > 3): # if rage is capped
            print(f"{self.name} becomes too overwhelmed with rage! Resetting their rage!")
            self.rage = 1
        else: # update rage counter, caps out at 3 for a total of 150% more damage if not used
            self.rage += 1

        # Change player energy
        self.energy -= 50

        print(f"{self.name} uses Sustained Rage increasing their attack power by 50%! \n") # combat text
        time.sleep(1)
        # Check if max rage
        if (self.rage == 3):
            print(f"{self.name} achieved max rage!")
            time.sleep(2)
        print(f"{self.name} smashes the ground and shakes everything nearby! \n")
        time.sleep(3)
        return (10)  # return the attack value

    def execute(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform execute, uses 100 (ALL) EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.5):  # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1

        # Check if rage counter is maxed for improved ultimate
        if(self.rage == 3):
            print(f"{self.name} unleashes ALL THEIR RAGE!")
            time.sleep(2)
            # Perform improved ultimate: (Base attack)*(crit)*(weapon crit damage)*rage + (improved str damage)
            attack = (100)*crit*(self.weapon[0])*self.rage + (self.rage*self.str*5)
            # Update rage counter
            self.rage = 0
        else: # standard attack
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + (rage bonus)
            attack = (100) * crit * (self.weapon[0]) + (self.str*5) + (self.rage)*(0.50)*(50)
            # Update rage counter
            self.rage = 0
        # Change player energy
        self.energy = 0
        print(f"{self.name} uses their ultimate! Execute! \n") # combat text
        return (int(attack*(1+rng.uniform(0,0.5))))  # Has a chance to do up to 50% more damage

    def perform(self,choice):
        '''input type: string ONLY 1,2,3'''
        '''return type: int'''
        """Perform ability of the class"""
        # Perform ability based on player choice
        if(choice == "1"): # Execute first ability
            return self.forward_slash()
        elif(choice == "2"): # Execute second ability
            return self.sustained_rage()
        elif(choice == "3"): # Execute third ability
            return self.execute()

''' Bowman Class '''
class Bowman(newPlayer): # Takes in parent class for baseline abilities
    def __init__(self,name):
        super().__init__(name) # call from parent class
        # Start assigning stats
        self.str = 3 # Strength
        self.dex = 3 # Dexterity
        self.int = 1 # Intellect
        self.luk = 3 # Luck

        # Assigning health points and energy points
        self.health = 175 # expendable health
        self.energy = 150 # expendable energy
        self.max_health = 175 # max health
        self.max_energy = 150 # max energy
        self.energy_rate = 20 # energy rate per turn

        # Assigning gear
        self.attire = equip.archer_garment() # Bowman starting attire
        self.weapon = equip.bow() # Bowman starting weapon

        # Name of each bowman ability
        self.abilities = ['Sniper Shot (25 EP)', 'Explosive Shot (70 EP)', 'Arrow Rain (MAX EP)']

        # Bowman ability cost
        self.cost = [25,70,150]

        # Bowman class meter
        self.accuracy = 0

        # Set class flag for Bowman
        self.class_flag[1] = 1

    '''Every class gets a dodge chance, scales with DEX'''
    def dodge(self):
        return True if rng.random() < (0.10 + self.dex*0.05) else False

    ''' Bowman Abilities '''
    def sniper_shot(self):
        '''input type: self'''
        '''return type: int'''
        """Perform sniper shot with class multipliers, uses 25 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0,1) + self.luk*(0.05)*(self.weapon[1])
        if(roll > 0.5): # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else: # standard hit
            crit = 1
        # bowman accuracy bonus
        acc_roll = rng.randint(1,5)
        self.accuracy += acc_roll
        self.accuracy %= 6

        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + (accuracy)
        attack = (50)*crit*(self.weapon[0]) + (self.str*5) + (self.accuracy)*(10)*crit
        # Change player energy
        self.energy -= 25
        print(f"{self.name} uses Sniper Shot! \n")
        time.sleep(1)
        print(f"{self.name} gains {acc_roll} focus!")
        time.sleep(1)
        return(int(attack)) # return the attack value

    def explosive_shot(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform explosive shot with class multipliers, uses 70 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.5):  # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1

        # bowman accuracy bonus
        acc_roll = rng.randint(1,5)
        self.accuracy += acc_roll
        self.accuracy %= 6

        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + (accuracy bonus)
        attack = (100) * crit * (self.weapon[0]) + (self.str*5) + (self.accuracy*10*crit)
        # Change player energy
        self.energy -= 70
        print(f"{self.name} uses Explosive Shot! \n") # combat text
        time.sleep(1)
        print(f"{self.name} gains {acc_roll} focus!")
        time.sleep(1)
        return (int(attack))  # return the attack value

    def ArrowRain(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform Arrow Rain, uses 150 (ALL) EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.5):  # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + (accuracy)
        if(self.accuracy == 5): # better ultimate
            attack = int((100) * crit * (self.weapon[0]) + (self.str*5))*self.accuracy
            # reset accuracy counter
            self.accuracy = 0
        else: # standard ultimate
            attack = (125) * crit * (self.weapon[0]) + (self.str*5) + (self.accuracy)*10*crit

        # Change player energy
        self.energy = 0
        print(f"{self.name} uses their ultimate! Arrow Rain! \n") # combat text
        time.sleep(1)
        return (int(attack*(1+rng.uniform(0,0.25))))  # Has a chance to do up to 25% more damage

    def perform(self,choice):
        '''input type: string ONLY 1,2,3'''
        '''return type: int'''
        """Perform ability of the class"""
        # Perform ability based on player choice
        if(choice == "1"): # Execute first ability
            return self.sniper_shot()
        elif(choice == "2"): # Execute second ability
            return self.explosive_shot()
        elif(choice == "3"): # Execute third ability
            return self.ArrowRain()

''' Mage class '''
class Mage(newPlayer): # Takes in parent class for baseline abilities
    def __init__(self,name):
        super().__init__(name) # call from parent class
        # Start assigning stats
        self.str = 0 # Strength
        self.dex = 2 # Dexterity
        self.int = 6 # Intellect
        self.luk = 2 # Luck

        # Assigning health points and energy points
        self.health = 150 # expendable health
        self.energy = 200 # expendable energy
        self.max_health = 150 # max health
        self.max_energy = 200 # max energy
        self.energy_rate = 30 # energy rate per turn

        # Elemental shift flag - Dictates if mage is using fire or ice abilities
        self.elemental = 2 # ODD - Fire, EVEN - Ice
        # Fire is more powerful, but uses significantly more ep
        # Ice is less powerful, but uses significantly less ep

        # Assigning gear
        self.attire = equip.wizard_robe() # Mage starting attire
        self.weapon = equip.staff() # Mage starting weapon

        # Name of each mage ability (Starts with ice)
        self.abilities = ['Ice Lance (30 EP)', 'Elemental Shift (50 EP)', 'Elemental Storm (200 EP)']

        # Mage ability cost
        self.cost = [30,50,200]

        # Set class flag for Mage
        self.class_flag[2] = 1

    '''Every class gets a dodge chance, scales with DEX'''
    def dodge(self):
        return True if rng.random() < (0.10 + self.dex*0.05) else False

    ''' Mage Abilities '''
    def ice_lance(self):
        '''input type: self'''
        '''return type: int'''
        """Perform ice lance with class multipliers, uses 30 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0,1) + self.luk*(0.05)*(self.weapon[1])
        if(roll > 0.5): # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else: # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage)
        attack = (45)*crit*(self.weapon[0]) + (self.str*5)
        # Change player energy
        self.energy -= 30
        print(f"{self.name} casts Ice Lance! \n")
        return(int(attack)) # return the attack value

    def incinerate(self):
        '''input type: self'''
        '''return type: int'''
        """Perform incinerate with class multipliers, uses 60 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0,1) + self.luk*(0.05)*(self.weapon[1])
        if(roll > 0.40): # successful critical strike chance, fire mage has better crit chance
            crit = 2
            print("Critical strike!")
        else: # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage)
        attack = (70)*crit*(self.weapon[0]) + (self.str*5)
        # Change player energy
        self.energy -= 60
        print(f"{self.name} casts Incinerate! \n")
        return(int(attack)) # return the attack value

    def elemental_shift(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform elemental shift to change abilities, uses 50 EP"""
        print(f"{self.name} uses Elemental shift! \n")  # combat text
        # update elemental flag for next time this is called
        self.elemental += 1
        if(self.elemental%2 == 1): # ODD = FIRE, EVEN = ICE
            # assign fire abilities and respective costs and energy rate
            self.abilities = ['Incinerate (60 EP)', 'Elemental Shift (50 EP)', 'Elemental Storm (MAX EP)']
            self.cost = [60,50,200]
            self.energy_rate -= 10
            print(f"🔥 {self.name} engulfs their surroundings in flames! 🔥")
            time.sleep(1)
            print(f"🔥 {self.name} takes on the power of flames! 🔥")
            time.sleep(3)
        else:
            # assign ice abilities and respective costs and energy rate
            self.abilities = ['Ice Lance (30 EP)', 'Elemental Shift (50 EP)', 'Elemental Storm (MAX EP)']
            self.cost = [30,50,200]
            self.energy_rate += 10
            print(f"❆ {self.name} shrouds their surroundings in ice! ❆")
            time.sleep(1)
            print(f"❆ {self.name} takes on the power of ice! ❆")
            time.sleep(3)

        # Change player energy
        self.energy -= 50
        return(10) # return 10 because the transition damages the enemy


    def ElementalStorm(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform Elemental Storm, uses 200 (ALL) EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.45):  # successful critical strike chance, slightly better crit chance for mage
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1
            # Perform attack - (base attack power)*(critical strike)*(critical damage) + (INT bonus damage)
        attack = (100) * crit * (self.weapon[0]) + (self.int*5)
        # Change player energy
        self.energy = 0
        print(f"{self.name} uses their ultimate! Elemental Storm! \n") # combat text
        return (int(attack*(1+rng.uniform(0,0.65))))  # Has a chance to do up to 50% more damage

    def perform(self,choice):
        '''input type: string ONLY 1,2,3'''
        '''return type: int'''
        """Perform ability of the class"""
        # Perform ability based on player choice
        if(choice == "1" and self.elemental%2 == 0): # Execute first ability (Ice)
            return self.ice_lance()
        elif(choice == "1" and self.elemental%2 == 1): # Execute first ability (Fire)
            return self.incinerate()
        elif(choice == "2"): # Execute second ability
            return self.elemental_shift()
        elif(choice == "3"): # Execute third ability
            return self.ElementalStorm()

''' Thief Class '''
class Thief(newPlayer): # Takes in parent class for baseline abilities
    def __init__(self,name):
        super().__init__(name) # call from parent class
        # Start assigning stats
        self.str = 1 # Strength
        self.dex = 3 # Dexterity
        self.int = 1 # Intellect
        self.luk = 5 # Luck

        # Assigning health points and energy points
        self.health = 175 # expendable health
        self.energy = 125 # expendable energy
        self.max_health = 175 # max health
        self.max_energy = 125 # max energy
        self.energy_rate = 25 # energy rate per turn

        # Assigning gear
        self.attire = equip.shrouded_armor() # Thief starting attire
        self.weapon = equip.dagger() # Thief starting weapon

        # Name of each thief ability
        self.abilities = ['Back Stab (30 EP)', 'Gouge (40 EP)', 'Shuriken Storm (MAX EP)']

        # Thief ability cost
        self.cost = [30,40,125]

        # Thief gouge counter
        self.gouge_count = 0

        # Set class flag for Thief
        self.class_flag[3] = 1

    '''Every class gets a dodge chance, scales with DEX'''
    def dodge(self): # Thief has a better dodge chance compared to the rest of the classes
        return True if rng.random() < (0.15 + self.dex*0.05) else False

    ''' Thief Abilities '''
    def back_stab(self):
        '''input type: self'''
        '''return type: int'''
        """Perform back stab with class multipliers, uses 30 EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0,1) + self.luk*(0.05)*(self.weapon[1])
        if(roll > 0.4): # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else: # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage)
        attack = (20)*(rng.randint(1,2))*crit*(self.weapon[0]) + (self.str*5)
        # Change player energy
        self.energy -= 30
        print(f"{self.name} uses Back Stab! \n")
        return(int(attack)) # return the attack value

    def gouge(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform gouge with class multipliers, uses 40 EP"""

        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.5):  # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1
        # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage) + gouge bonus
        # Change gouge counter
        self.gouge_count += 1

        # Gouge caps out at 3, otherwise reset it back to 1
        if (self.gouge_count > 3):
            self.gouge_count = 1
            attack = (30) * crit * (self.weapon[0]) + (self.str*5) + self.gouge_count*(12)*crit
        else:
            attack = (30) * crit * (self.weapon[0]) + (self.str*5) + self.gouge_count*(12)*crit
        # Change player energy
        self.energy -= 40
        print(f"{self.name} uses Gouge! \n") # combat text
        return (int(attack))  # return the attack value

    def ShurikenStorm(self):
        '''input type: self'''
        '''return type: int'''
        """ Perform Shuriken Storm, uses 125 (ALL) EP"""
        # Roll for critical strike chance, scales with LUK, and weapon crit chance
        roll = rng.uniform(0, 1) + self.luk * (0.05) * (self.weapon[1])
        if (roll > 0.4):  # successful critical strike chance
            crit = 2
            print("Critical strike!")
        else:  # standard hit
            crit = 1
            # Perform attack - (base attack power)*(critical strike)*(critical damage) + (STR crit damage)
        attack = []
        print(f"{self.name} uses their ultimate! Shuriken Storm! \n")  # combat text
        time.sleep(2)
        for i in range(6): # it's a flurry of 5 shurikens thrown
            throw = int(15*(1+rng.uniform(0,0.25))*(self.weapon[0]))*crit + (self.str*5)
            attack.append(throw)
            time.sleep(0.5)
            print(f"{self.name} throws for {throw} !")
        time.sleep(2)

        # Change player energy
        self.energy = 0
        return (sum(attack))  # The summation of all the throws

    def perform(self,choice):
        '''input type: string ONLY 1,2,3'''
        '''return type: int'''
        """Perform ability of the class"""
        # Perform ability based on player choice
        if(choice == "1"): # Execute first ability
            return self.back_stab()
        elif(choice == "2"): # Execute second ability
            return self.gouge()
        elif(choice == "3"): # Execute third ability
            return self.ShurikenStorm()



def new_player(name):
    '''input type: string'''
    '''return type: object'''
    """new player creation"""

    '''Class selection '''
    while(True):
        print(f"Choose a path...{name}")
        title.class_choice_UI() # call class selection screen

        # prompt user for choice
        choice = "" # blank choice
        choice = input(": ")
        if(choice == '1'): # User picks the warrior
            title.warrior_prev() # Show warrior class preview before user makes choice
            while(True): # User commits to a choice
                choice = input("Commit to this path? (Y/N): ")
                if(choice.lower() == 'y'): # User commits to their choice
                    print(f"You are now {name}, the warrior!")
                    # call warrior object
                    choice = Warrior(name)
                    return choice # bring it back to the main app
                elif(choice.lower() == 'n'): # User changes their mind
                    new_player(name) # execute new player again

        if(choice == '2'): # User picks the bowman
            title.bowman_prev() # Show bowman class preview before user makes choice
            while(True): # User commits to a choice
                choice = input("Commit to this path? (Y/N): ")
                if(choice.lower() == 'y'): # User commits to their choice
                    print(f"You are now {name}, the bowman!")
                    # call bowman object
                    choice = Bowman(name)
                    return choice # bring it back to main app
                elif(choice.lower() == 'n'): # User changes their mind
                    new_player(name) # execute new player again

        if(choice == '3'): # User picks the mage
            title.mage_prev() # Show mage class preview before user makes choice
            while(True): # User commits to a choice
                choice = input("Commit to this path? (Y/N): ")
                if(choice.lower() == 'y'): # User commits to their choice
                    print(f"You are now {name}, the mage!")
                    # call mage object
                    choice = Mage(name)
                    return choice # bring it back to main app
                elif(choice.lower() == 'n'): # User changes their mind
                    new_player(name) # execute new player again

        if(choice == '4'): # User picks the thief
            title.thief_prev() # Show thief class preview before user makes choice
            while(True): # User commits to a choice
                choice = input("Commit to this path? (Y/N): ")
                if(choice.lower() == 'y'): # User commits to their choice
                    print(f"You are now {name}, the thief!")
                    # call thief object
                    choice = Thief(name)
                    return choice # bring it back to main app
                elif(choice.lower() == 'n'): # User changes their mind
                    new_player(name) # execute new player again
        else: # mis-input
            print("Invalid choice. Please try again.")


