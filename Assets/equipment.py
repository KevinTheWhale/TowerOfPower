import random as rng
import time
""" All equipment, consumables, and spoils """

""" Weapons """

# Default warrior weapon
def saber():
    return([1.05,1.00]) # [critical damage bonus, critical chance bonus], [5% critical damage, 0% crit chance]

# Default bowman weapon
def bow():
    return([1.00,1.05]) # [0% crit damage, 5% crit bonus]

# Default mage weapon
def staff():
    return([1.05,1.05])

# Default thief weapon
def dagger():
    return([1.05,1.10])

# Bonus warrior weapon
def ancient_saber():
    return([1.20,1.10])

# Bonus bowman weapon
def eagle_bow():
    return([1.10,1.10])

# Bonus mage weapon
def nirvana():
    return([1.10,1.20])

# Bonus thief weapon
def hydra_shard():
    return([1.05,1.30])



""" Attire """

# Default warrior attire
def chainmail():
    return(0.90) # damage reduction, in this case, it's a 10% damage reduction

# Default bowman attire
def archer_garment():
    return(0.95) # 5% damage reduction

# Default mage attire
def wizard_robe():
    return(1.0) # 0% damage reduction

# Default thief attire
def shrouded_armor():
    return(0.95) # 5% damage reduction


# Bonus warrior attire
def ancient_cuirass():
    return(0.80) # 20% damage reduction

# Bonus bowman attire
def eagle_garment():
    return(0.90) # 10% damage reduction

# Bonus mage attire
def sorcerer_robe():
    return(0.95)  # 5% damage reduction

# Bonus thief attire
def shadowed_armor():
    return(0.90) # 10% damage reduction

""" Consumables """

# Basic health pot
def hp_pot(player):
    '''input type: Object'''
    '''return type: None'''
    # Restores 100 hp
    player.health += 100
    print(f"{player.name} uses a Basic health potion! It heals for 100!")
    if(player.health > player.max_health): # compensate for over-healing
        player.health = player.max_health
    return

# Greater health pot
def greater_hp(player):
    '''input type: object'''
    '''return type: None'''
    # Restores 200 hp
    player.health += 200
    print(f"{player.name} uses a Greater health potion! It heals for 200!")
    if (player.health > player.max_health):  # compensate for over-healing
        player.health = player.max_health
    return

# Basic energy pot
def ep_pot(player):
    '''input type: object'''
    '''return type: None'''
    # Restores 50 energy
    player.energy += 50
    print(f"{player.name} uses a Basic energy potion! It restores 50 energy!")
    if(player.energy > player.max_energy): # compensate for over-energy
        player.energy = player.max_energy
    return

# Greater energy pot
def greater_ep(player):
    '''input type: object'''
    '''return type: None'''
    # Recover 100 energy
    player.energy += 100
    print(f"{player.name} uses a Greater energy potion! It restores 100 energy!")
    if (player.energy > player.max_energy):  # compensate for over-energy
        player.energy = player.max_energy
    return

# Phoenix down - Cheat death
def phoenix_down(player):
    '''input type: object'''
    '''return type None'''
    player.health = 0.5*player.max_health # upon death, restore half of max hp


# Consumables dictionary
def potion_dictionary(player,choice):
    '''input type: object, string'''
    '''return type: None'''
    '''Use consumable in accordance to choice'''
    # note: ONlY correct strings can be queued in
    if(choice == 'Basic health potion (Recover 100 hp)'):
        hp_pot(player) # use consumable
        # update their backpack
        player.backpack.remove('Basic health potion (Recover 100 hp)')
        return # return nothing
    elif(choice == 'Basic energy potion (Recover 50 ep)'):
        ep_pot(player)
        player.backpack.remove('Basic energy potion (Recover 50 ep)')
        return
    elif(choice == 'Greater health potion (Recover 200 hp)'):
        greater_hp(player)
        player.backpack.remove('Greater health potion (Recover 200 hp)')
        return
    elif(choice == 'Greater energy potion (Recover 100 ep)'):
        greater_ep(player)
        player.backpack.remove('Greater energy potion (Recover 100 ep)')
        return
    elif(choice == 'Phoenix Down'):
        # Cheat death
        pass



""" Rewards """
# Floor 1 rewards
def floor_01_reward():
    '''input type: None'''
    '''return type: int'''
    return(50) # 50 gold for the reward

# Floor 2 rewards
def floor_02_reward():
    '''input type: None'''
    '''return type: int'''
    return(100) # 100 gold for the reward

# Floor 3 rewards
def floor_03_reward():
    '''input type: None'''
    '''return type: int'''
    return(150) # 150 gold for the reward

# Floor 4 rewards
def floor_04_reward():
    '''input type: None'''
    '''return type: int'''
    return(200) # 200 gold for the reward

warrior_bonus = ['Ancient Saber','Ancient Cuirass']
bowman_bonus = ['Eagle Bow', 'Eagle Garment']
mage_bonus = ['Nirvana', 'Sorcerers Robe']
thief_bonus = ['Hydra Shard', 'Shadowed Armor']
# Bonus rolls
def bonus_reward(player): # bonus rewards
    '''input type: object'''
    '''return type: None'''
    """Grant Player Bonus Roll"""
    # Perform roll between attire or weapon
    time.sleep(3)
    print(f"{player.name} has received a bonus!")
    time.sleep(3)
    # Check which class they are
    if(player.class_flag[0] == 1): # Warrior class
        # Check for bonuses
        if(len(warrior_bonus) == 0): # no bonuses left
            print("Looks like the only thing left in the chest is some gold...")
            time.sleep(1)
            print(f"{player.name} receives 50 gold!")
            # update player currency
            player.coin += 50
        elif(len(warrior_bonus) == 2):
            roll = rng.randint(0,1)
            print(f"{player.name} receives {warrior_bonus[roll]}!")
            time.sleep(2)
            if(warrior_bonus[roll] == 'Ancient Saber'): # grant bonus weapon
                warrior_bonus.remove('Ancient Saber') # remove from bonus
                player.weapon = ancient_saber()
                return # exit bonus
            else: # grant bonus armor
                warrior_bonus.remove('Ancient Cuirass')
                player.attire = ancient_cuirass()
                return
        else: # only one bonus equipment left in the chest
            if(warrior_bonus[0] == 'Ancient Saber'):
                warrior_bonus.remove('Ancient Saber')
                player.weapon = ancient_saber()
                return
            else:
                warrior_bonus.remove('Ancient Cuirass')
                player.attire = ancient_cuirass()
                return
    elif(player.class_flag[1] == 1): # Bowman class
        if (len(bowman_bonus) == 0):  # no bonuses left
            print("Looks like the only thing left in the chest is some gold...")
            time.sleep(1)
            print(f"{player.name} receives 50 gold!")
            # update player currency
            player.coin += 50
        elif (len(bowman_bonus) == 2):
            roll = rng.randint(0, 1)
            print(f"{player.name} receives {bowman_bonus[roll]}!")
            time.sleep(2)
            if (bowman_bonus[roll] == 'Eagle Bow'):  # grant bonus weapon
                bowman_bonus.remove('Eagle Bow')  # remove from bonus
                player.weapon = eagle_bow()
                return  # exit bonus
            else:  # grant bonus armor
                bowman_bonus.remove('Eagle Garment')
                player.attire = eagle_garment()
                return
        else:  # only one bonus equipment left in the chest
            if (bowman_bonus[0] == 'Eagle Bow'):
                bowman_bonus.remove('Eagle Bow')
                player.weapon = eagle_bow()
                return
            else:
                bowman_bonus.remove('Eagle Garment')
                player.attire = eagle_garment()
                return
    elif(player.class_flag[2] == 1): # Mage class
        if (len(mage_bonus) == 0):  # no bonuses left
            print("Looks like the only thing left in the chest is some gold...")
            time.sleep(1)
            print(f"{player.name} receives 50 gold!")
            # update player currency
            player.coin += 50
        elif (len(mage_bonus) == 2):
            roll = rng.randint(0, 1)
            print(f"{player.name} receives {mage_bonus[roll]}!")
            time.sleep(2)
            if (mage_bonus[roll] == 'Nirvana'):  # grant bonus weapon
                mage_bonus.remove('Nirvana')  # remove from bonus
                player.weapon = nirvana()
                return  # exit bonus
            else:  # grant bonus armor
                mage_bonus.remove('Sorcerers Robe')
                player.attire = sorcerer_robe()
                return
        else:  # only one bonus equipment left in the chest
            if (mage_bonus[0] == 'Nirvana'):
                mage_bonus.remove('Nirvana')
                player.weapon = nirvana()
                return
            else:
                mage_bonus.remove('Sorcerers Robe')
                player.attire = sorcerer_robe()
                return
    elif(player.class_flag[3] == 1): # Thief class
        if (len(thief_bonus) == 0):  # no bonuses left
            print("Looks like the only thing left in the chest is some gold...")
            time.sleep(1)
            print(f"{player.name} receives 50 gold!")
            # update player currency
            player.coin += 50
        elif (len(thief_bonus) == 2):
            roll = rng.randint(0, 1)
            print(f"{player.name} receives {thief_bonus[roll]}!")
            time.sleep(2)
            if (thief_bonus[roll] == 'Hydra Shard'):  # grant bonus weapon
                thief_bonus.remove('Hydra Shard')  # remove from bonus
                player.weapon = hydra_shard()
                return  # exit bonus
            else:  # grant bonus armor
                thief_bonus.remove('Shadowed Armor')
                player.attire = shadowed_armor()
                return
        else:  # only one bonus equipment left in the chest
            if (thief_bonus[0] == 'Hydra Shard'):
                thief_bonus.remove('Hydra Shard')
                player.weapon = hydra_shard()
                return
            else:
                thief_bonus.remove('Shadowed Armor')
                player.attire = shadowed_armor()
                return


