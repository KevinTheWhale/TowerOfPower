"""Main title screen"""
import math
import time
import random as rng
"""Title screen function"""
def title_screen():
    print("|--------------------------------------------------------|")
    print("|   ▢▢▢▢▢▢▢         -------         ▢▢▢▢▢▢▢        |")
    print("|       ▢             /       \        ▢        ▢       |")
    print("|       ▢            | ()   () |       ▢▢▢▢▢▢▢        |")
    print("|       ▢             \   ^   /        ▢                 |")
    print("|       ▢              |||||||         ▢                 |")
    print("|       ▢              |||||||         ▢                 |")
    print("|-----Tower---------------OF------------Power-------------|")
    print("|---------------------------------------------------------|")
    print("|----|New Game (Y)|--------------------|Quit (N)|---------|")
    print("|-----------------------|Info (I)|------------------------|")

""" Info Screen - Shows general information """
def info_screen():
    print("|--------------------------------------------------------|")
    print("| Welcome to Tower of Power!                             |")
    print("| Fight your way through multiple floors and collect     |")
    print("| rewards that strengthen your player along the way.     |")
    print("|--------------------------------------------------------|")
    print("| Stats:                                                 |")
    print("| Strength   (STR) - Dictates critical damage            |")
    print("| Dexterity  (DEX) - Dictates dodge chance               |")
    print("| Intellect  (INT) - Dictates damage mitigation          |")
    print("| Luck       (LUK) - Dictates critical chance            |")
    print("|--------------------------------------------------------|")

"""Resting Hub Screen"""
def resting_hub_ui():
    print("|----------We're safe for now......----------------------|")
    print("|---|S. Shop|--------------|B. Backpack|-----------------|")
    print("|--------------------------------------------------------|")
    print("|---|P. Prayer Stone|------|E. Return to tower|----------|")
    print("|--------------------------------------------------------|")
    print("|---|I. Player Info|-------|Q. Quit game|----------------|")


"""Class Selection Screen"""
def class_choice_UI():
    print("|---------------------------------------------------------|")
    print("| (1) - WARRIOR                        (2) - BOWMAN       |")
    print("| (3) - MAGE                           (4) - THIEF        |")
    print("|---------------------------------------------------------|")

""" Class previews """
def warrior_prev(): # Warrior class preview
    print("|---------------------------------------------------------|")
    print("| The Warrior is a fierce war machine capable of doing    |")
    print("| massive damage to their opponents. While they are strong|")
    print("| they lack dexterity, making them prone to all attacks.  |")
    print("|---------------------------------------------------------|")
    print("| Warrior Stat weight:                                    |")
    print("| Strength    (STR): 6                                    |")
    print("| Dexterity   (DEX): 1                                    |")
    print("| Intellect   (INT): 1                                    |")
    print("| Luck        (LUK): 2                                    |")
    print("| Health points(HP): 200                                  |")
    print("| Energy points(EP): 100                                  |")
    print("|---------------------------------------------------------|")

def bowman_prev(): # bowman class preview
    print("|---------------------------------------------------------|")
    print("| The Bowman is a sharpshooter. Specializing in ranged    |")
    print("| combat gives them the edge on most foes.                |")
    print("| While they are at a distance, they are still vulnerable.|")
    print("|---------------------------------------------------------|")
    print("| Bowman Stat weight:                                     |")
    print("| Strength    (STR): 3                                    |")
    print("| Dexterity   (DEX): 3                                    |")
    print("| Intellect   (INT): 1                                    |")
    print("| Luck        (LUK): 3                                    |")
    print("| Health points(HP): 175                                  |")
    print("| Energy points(EP): 150                                  |")
    print("|---------------------------------------------------------|")

def mage_prev(): # mage class preview
    print("|---------------------------------------------------------|")
    print("| The Mage is a powerful sorcerer. Using their intellect  |")
    print("| to understand their foes and reduce the damage they take|")
    print("| Their attacks use slightly more energy.                 |")
    print("|---------------------------------------------------------|")
    print("| Mage Stat weight:                                       |")
    print("| Strength    (STR): 0                                    |")
    print("| Dexterity   (DEX): 2                                    |")
    print("| Intellect   (INT): 6                                    |")
    print("| Luck        (LUK): 2                                    |")
    print("| Health points(HP): 150                                  |")
    print("| Energy points(EP): 200                                  |")
    print("|---------------------------------------------------------|")

def thief_prev(): # Thief class preview
    print("|---------------------------------------------------------|")
    print("| The Thief is a master of stealth and see the weaknesses |")
    print("| of their foes, making their attacks potentially         |")
    print("| devastating. They are very prone to all attacks.        |")
    print("|---------------------------------------------------------|")
    print("| Thief Stat weight:                                      |")
    print("| Strength    (STR): 1                                    |")
    print("| Dexterity   (DEX): 3                                    |")
    print("| Intellect   (INT): 1                                    |")
    print("| Luck        (LUK): 5                                    |")
    print("| Health points(HP): 175                                  |")
    print("| Energy points(EP): 125                                  |")
    print("|---------------------------------------------------------|")

""" Enemy Information """

# Billy the Bully
def floor_01_info():
    """input type: none"""
    '''return type: none'''
    """Show description of floor 1 enemy"""
    print("|---------------------------------------------------------|")
    print("| Floor 1: Billy the Bully (300 hp)                       |")
    print("|---------------------------------------------------------|")
    print("| Abilities:                                              |")
    print("| Unfriendly Jab - Strikes player funny bone for 25 hp    |")
    print("| Name Calling - Cause emotional turmoil for 30 hp        |")
    print("|---------------------------------------------------------|")
    print("| Ultimate:                                               |")
    print("| Terrible Tackle - At full energy, hurls entire body at  |")
    print("|                   opponent for 75 hp.                   |")
    print("|---------------------------------------------------------|")

# Debbie Downer
def floor_02_info():
    """input type: none"""
    '''return type: none'''
    """Show description of floor 2 enemy"""
    print("|---------------------------------------------------------|")
    print("| Floor 2: Debbie Downer (500 hp)                         |")
    print("|---------------------------------------------------------|")
    print("| Abilities:                                              |")
    print("| Fierce Slap - Literally just slaps the player for 30 hp |")
    print("| Power Kick - Kicks the player for 40 hp                 |")
    print("|---------------------------------------------------------|")
    print("| Ultimate:                                               |")
    print("| Impending Doubt - At full energy, Debbie sends a wave   |")
    print("|                   of negative energy that strikes for   |")
    print("|                   100 hp and drains 20 ep.              |")
    print("|---------------------------------------------------------|")

# Slippery Sam
def floor_03_info():
    """input type: none"""
    '''return type: none'''
    """Show description of floor 3 enemy"""
    print("|---------------------------------------------------------|")
    print("| Floor 3: Slippery Sam (550 hp)                          |")
    print("|---------------------------------------------------------|")
    print("| Abilities:                                              |")
    print("| Swift Smack - Strikes at fast speeds for 25 hp          |")
    print("| Blinding Smack - Strikes at blinding speeds for 40 hp   |")
    print("|---------------------------------------------------------|")
    print("| Ultimate:                                               |")
    print("| Tidal Wave - At full energy, Sam unleashes a tidal wave |")
    print("|              that strikes the player for 100 hp and     |")
    print("|              poisons them for 10 hp for 4 turns.        |")
    print("|---------------------------------------------------------|")

# Furious Fred
def floor_04_info():
    """input type: none"""
    '''return type: none'''
    """Show description of floor 4 enemy"""
    print("|---------------------------------------------------------|")
    print("| Floor 4: Furious Fred (1000 hp)                         |")
    print("|---------------------------------------------------------|")
    print("| Abilities:                                              |")
    print("| Devastating Punch - Heavily strikes for 30 hp           |")
    print("| Furious Uppercut - Heavily uppercuts for 50 hp          |")
    print("| Insatiable Rage - As the fight progresses, Fred gains   |")
    print("|                   energy progressively faster.          |")
    print("|---------------------------------------------------------|")
    print("| Ultimate:                                               |")
    print("| Enrage - At full energy, Fred goes into a blind rage    |")
    print("|          that amplifies his attacks by an additional    |")
    print("|          50% that ignores armor and damage mitigation.  |")
    print("|          This effect stacks until he is defeated.       |")
    print("|---------------------------------------------------------|")

# Renjiro
def final_floor_info():
    """input type: none"""
    '''return type: none'''
    """Show description of final floor enemy"""
    print("|---------------------------------------------------------|")
    print("| Final Floor: Renjiro, The Titan (2000 hp)               |")
    print("|---------------------------------------------------------|")
    print("| Abilities:                                              |")
    print("| Double Lance - Strikes for 25 hp and has a 50% to strike|")
    print("                 twice.                                   |")
    print("| Ion Cannon - Blasts for 50-75 hp.                       |")
    print("| Desperate instincts - At 50% hp, Renjiro amplifies      |")
    print("|                       themselves by gaining stronger    |")
    print("|                       abilities and gains energy faster.|")
    print("|---------------------------------------------------------|")
    print("| Ultimate:                                               |")
    print("| Mega Flare - At full energy, Renjiro unleashes a        |")
    print("|              devastating attack that unmakes the        |")
    print("|              universe, instantly causing a game over.   |")
    print("|---------------------------------------------------------|")






"""In-combat UI"""
def combat_ui():
    print("|-----|A. Attack|------|B. Backpack|-----|E. Escape|-----|")
    print("|-----|S. Skip Turn|---|I. Floor info|---|Q. Quit game|--|")

""" Shop UI"""
def shop():
    '''input type: None'''
    '''return type: None'''
    """ Player shop to refresh consumables """
    """
    Available options:
    - Full heal (20 gold)
    - Full energy (15 gold)
    - Basic health pot (15 gold)
    - Basic energy pot (10 gold)
    - Greater health pot (25 gold)
    - Greater energy pot (20 gold)
    - Back to resting hub
    """
    print("|---------------------------------------------------------|")
    print("|----------------------| SHOP |---------------------------|")
    print("| |1. Full heal (Restores current hp to full) (20 gold)|  |")
    print("| |2. Full energy (Restores current ep to full) (25 gold)||")
    print("| |3. Basic health potion (15 gold) |                     |")
    print("| |4. Basic energy potion (10 gold) |                     |")
    print("| |5. Greater health potion (25 gold) |                   |")
    print("| |6. Greater energy potion (20 gold) |                   |")
    print("|---------------------------------------------------------|")
    print("| B. Back                                                 |")

""" PRAYER STONE UI """
def prayer_stone(player,limit):
    """input type: object,list"""
    """return type: none"""
    """Allows player to purchase a stat but can only purchase that specific stat once"""
    print("|---------------------------------------------------------|")
    print("|                    Prayer Stone                         |")
    # Prompt player choice
    while(True):
        print("|---------------------------------------------------------|")
        print("|--|1. Strength|-|2. Dexterity|-|3. Intellect|-|4. Luck|--|")
        print("|-----------------------|B. Back|-------------------------|")
        print("Provide an offering of 100 g to boost a specific stat once...")
        print(f"Coin: {player.coin} g")
        if (player.coin < 100):  # player doesn't have enough currency
            print("It seems you do not have enough coin to offer....")
            time.sleep(3)
            print("Returning you back...")
            time.sleep(3)
            return
        elif(len(limit) == 0): # choices exhausted
            print("You received all the blessings....")
            time.sleep(3)
            print("Returning to resting hub...")
            time.sleep(1)
            return
        action = input("Make your choice: ")
        try:
            if(action.lower() == 'b'): # user chooses to go back
                print("Farewell adventurer....")
                time.sleep(3)
                return
            action = int(action)
            if(action == 1): # player chooses strength
                if('Strength' in limit): # check if it's in the list
                    limit.remove('Strength') # remove it since you can only boost it once
                    player.str += 1 # update stat
                    print(f"{player.name}'s Strength has increased by 1!")
                    player.coin -= 100 # update player currency
                    time.sleep(3)
                else: # Player already boosted it once
                    print("You already boosted this stat...")
                    time.sleep(1)
                    continue # go back to selection ui
            elif(action == 2): # player chooses dexterity
                if('Dexterity' in limit):
                    limit.remove('Dexterity')
                    player.dex+=1
                    print(f"{player.name}'s Dexterity has increased by 1!")
                    player.coin -= 100
                    time.sleep(3)
                else:
                    print("You already boosted this stat...")
                    continue
            elif(action == 3): # player chooses intellect
                if('Intellect' in limit):
                    limit.remove('Intellect')
                    player.int+=1
                    print(f"{player.name}'s Intellect has increased by 1")
                    player.coin -= 100
                    time.sleep(3)
                else:
                    print("You already boosted this stat...")
                    continue
            elif(action == 4): # player chooses luck
                if('Luck' in limit):
                    limit.remove('Luck')
                    player.luk+=1
                    print(f"{player.name}'s Luck has increased by 1")
                    player.coin-=100
                    time.sleep(3)
                else:
                    print("You already boosted this stat...")
                    continue
            else:
                print("Invalid input. Please try again.")
                continue
        except ValueError: # invalid choice non-numeric
            print("Invalid input. Please try again.")
            time.sleep(1)



""" FINAL REST UI """
def final_rest(player):
    """input type: Object"""
    """return type: none"""
    """This is player's final chance before the final boss to purchase items and stats"""
    print("|---------------------------------------------------------|")
    print("|--------------------| Final Rest |-----------------------|")
    print("| |1. Random Stat Boost (100 g)|                          |")
    print("| |2. Random Attribute Boost (200 g)|                     |")
    print("| |3. Basic health potion (15 g)|                         |")
    print("| |4. Basic energy potion (10 g)|                         |")
    print("| |5. Greater health potion (25 g)|                       |")
    print("| |6. Greater energy potion (20 g)|                       |")
    print("|---------------------------------------------------------|")
    print("| S. View Player Stats          B. Proceed to Final Floor |")
    # prompt user choice
    while(True):
        print(f"Coin: {player.coin} g")
        print(f"{player.name}'s backpack: {player.backpack}")
        action = input("Choice: ")
        if(action == '1' and player.coin >= 100): # player chooses random stat to boost
            print(f"{player.name} chooses a random stat to boost!")
            time.sleep(1)
            player.coin -= 100 # update player currency
            roll = rng.randint(1,4) # roll stat
            if(roll == 1): # str
                player.str += 1 # grant stat boost
                print(f"{player.name}'s strength has increased by 1!")
                time.sleep(3)
                continue
            elif(roll == 2): # dex
                player.dex += 1
                print(f"{player.name}'s dexterity has increased by 1!")
                time.sleep(3)
                continue
            elif(roll == 3): # int
                player.int += 1
                print(f"{player.name}'s intellect has increased by 1!")
                time.sleep(3)
                continue
            else: # luk
                player.luk += 1
                print(f"{player.name}'s luck has increased by 1!")
                time.sleep(3)
                continue
        elif(action == '2' and player.coin >= 200): # player chooses random attribute
            print(f"{player.name} chooses to boost a random attribute!")
            time.sleep(1)
            player.coin -= 200
            roll = rng.randint(1,3)
            if(roll == 1): # max hp increases by 100
                print(f"{player.name}'s max hp has increased by 100!")
                player.max_health+=100
                player.health = player.max_health
                time.sleep(1)
                print(f"{player.name}'s hp is now {player.max_health}!")
                time.sleep(3)
                continue
            elif(roll == 2): # max ep increases by 50
                print(f"{player.name}'s max ep has increased by 50!")
                player.max_energy += 50
                player.energy = player.max_energy
                time.sleep(1)
                print(f"{player.name}'s ep is now {player.max_energy}!")
                time.sleep(3)
                continue
            else: # energy rate increases by 15
                print(f"{player.name}'s energy rate is increased by 15!")
                player.energy_rate+=15
                time.sleep(1)
                print(f"{player.name}'s energy rate is now {player.energy_rate}!")
                time.sleep(3)
                continue
        elif(action == '3' and player.coin >= 15): # player purchases basic health potion
            if(len(player.backpack) == 4):
                print("You don't have enough space! Backpack limit is 4 items!")
                time.sleep(3)
                continue
            else: # update backpack
                print(f"{player.name} purchases a Basic health potion!")
                player.coin -= 15
                player.backpack.append('Basic health potion (Recover 100 hp)')
                time.sleep(2)
                continue
        elif(action == '4' and player.coin >= 10): # player purchases basic energy potion
            if (len(player.backpack) == 4):
                print("You don't have enough space! Backpack limit is 4 items!")
                time.sleep(3)
                continue
            else:
                print(f"{player.name} purchases a Basic energy potion!")
                player.coin -= 10
                player.backpack.append('Basic energy potion (Recover 50 ep)')
                time.sleep(2)
                continue
        elif(action == '5' and player.coin >= 25): # player chooses greater hp pot
            if (len(player.backpack) == 4):
                print("You don't have enough space! Backpack limit is 4 items!")
                time.sleep(3)
                continue
            else:
                print(f"{player.name} purchases a Greater health potion!")
                player.coin -= 25
                player.backpack.append('Greater health potion (Recover 200 hp)')
                time.sleep(2)
                continue
        elif(action == '6' and player.coin >= 20): # player chooses greater ep pot
            if (len(player.backpack) == 4):
                print("You don't have enough space! Backpack limit is 4 items!")
                time.sleep(3)
                continue
            else:
                print(f"{player.name} purchases a Greater energy potion!")
                player.coin -= 20
                player.backpack.append('Greater energy potion (Recover 100 ep)')
                time.sleep(2)
                continue
        elif(action.lower() == 'b'): # player goes back
            print("Warning: This is your last chance to purchase any last minute items.")
            time.sleep(1)
            while(True):
                action = input("Are you sure you want to continue? (Y/N): ")
                if(action.lower() == 'y'): # player proceeds to final floor
                    print("Moving to the final floor...")
                    time.sleep(3)
                    return # return to main app
                elif(action.lower() == 'n'): # player changes mind and stays
                    action = 4
                    break
                else: # invalid choice
                    print("Invalid choice. Please try again.")
                    time.sleep(1)
            if(action == 4): # player changes mind and stays in final rest
                continue
        elif(action.lower() == 's'): # player chooses to view stats
            player_stats(player) # call player stats ui
            continue
        else: # invalid input or not enough coin
            print("You either do not have enough coin or you made an invalid choice.")
            time.sleep(1)

def player_stats(player):
    '''input type: object'''
    '''return type: none'''
    """View player stats"""
    print("|---------------------------------------------------------|")
    print(f"{player.name}")
    if(player.class_flag.index(1) == 0): # identify class by index
        print("Class: Warrior")
    elif(player.class_flag.index(1) == 1):
        print("Class: Bowman")
    elif(player.class_flag.index(1) == 2):
        print("Class: Mage")
    else:
        print("Class: Thief")
    # show player stats
    print("|---------------------------------------------------------|---------------------------------------------------------|")
    print("| Stats:                                                  | Equipment:                                              |")
    print(f"| Strength: {player.str}                                  |                                                         |")
    print(f"| Dexterity: {player.dex}                                 |                                                         |")
    print(f"| Intellect: {player.int}                                 |                                                         |")
    print(f"| Luck: {player.luk}                                      |                                                         |")
    print("|---------------------------------------------------------|")
    print(f"| HP: {player.health}                                              |")
    print(f"| EP: {player.energy}                                              |")
    print(f"| Energy Rate: {player.energy_rate}                             |")
    print("|---------------------------------------------------------|---------------------------------------------------------|")
    action = input("Input any key to continue.")
    return


"""Abilities UI"""
def ability_ui(player):
    '''input type: object'''
    '''return type: None'''
    """Show all player abilities during combat"""
    print("|---------------------------------------------------------|")
    print(f"| 1. {player.abilities[0]}                                ")
    print(f"| 2. {player.abilities[1]}                                ")
    print(f"| 3. {player.abilities[2]}                                ")
    print(f"| 4. Back                                                 ")
    print("|---------------------------------------------------------|")

"""player backpack ui"""
def backpack_ui(player):
    '''input type: object'''
    '''return type: None'''
    """ Shows all contents of backpack including currency"""
    print("|---------------------------------------------------------|")
    print(f"Gold ⛁: {player.coin} g")
    for i,j in enumerate(player.backpack):
        print(i+1,j)
    print(len(player.backpack)+1,"Back")
    print("|---------------------------------------------------------|")


""" Game Over Screen """
def game_over():
    '''input type: None'''
    '''return type: None'''
    """Show game over when game has been quit or player has been slain"""
    print("|---------------------------------------------------------|")
    print("|          G A M E                     O V E R            |")
    print("|---------------------------------------------------------|")
    exit() # terminate game

"""Floor completion UI"""
def floor_victory(player):
    '''input type: Object'''
    '''return type: None'''
    """ Show stats of floor completion"""
    print("|---------------------------------------------------------|")
    print(f"|             Floor {sum(player.floor_flag)} Review       ")
    print(f"|   Current gold ⛁: {player.coin} g                       ")
    print("|---------------------------------------------------------|")

"""Final Floor Victory UI"""
def total_victory(player):
    """input type: object"""
    """return type: None"""
    """Show final victory UI"""
    print("|---------------------------------------------------------|")
    print(f"{player.name} has conquered the tower!")
    print("|---------------------------------------------------------|")
    print("|                  CONGRATULATIONS !                      |")
    print("|               THANK YOU FOR PLAYING !                   |")
    print("|---------------------------------------------------------|")

""" Level Up UI """
def level_up(player):
    '''input type: object'''
    '''return type: None'''
    """Player gets to boost a attribute after 1st time completion of a floor"""
    print("|---------------------------------------------------------|")
    print("|                       LEVEL UP !                        |")
    print("|              Pick an attribute to boost                 |")
    # Prompt for player choice.
    while(True):
        print("|---------------------------------------------------------|")
        print("| |H. Health points| |E. Energy points| |R. Energy Rate|  |")
        print("|---------------------------------------------------------|")
        choice = input("Choice: ")
        # Check choices
        if(choice.lower() == 'h'): # player chooses hp boost
            # adjust their max health by a flat 100 points
            print(f"{player.name} has boosted their max hp by 100!")
            player.max_health += 100
            time.sleep(2)
            print(f"Their max health is now {player.max_health} hp!")
            return # bring back to main app
        elif(choice.lower() == 'e'): # player chooses ep boost
            # adjust their max energy by a flat 50
            print(f"{player.name} has boosted their max ep by 50!")
            player.max_energy += 50
            time.sleep(2)
            print(f"Their max energy is now {player.max_energy} ep!")
            return
        elif(choice.lower() == 'r'): # player chooses ep rate boost
            # adjust their energy rate by a flat 15
            print(f"{player.name} has boosted their energy rate by 15!")
            player.energy_rate += 15
            time.sleep(2)
            print(f"Their energy rate is now {player.energy_rate} per turn!")
            return
        else: # invalid choice
            print("Invalid choice! Please try again!")




"""Player and enemy bars"""
'⬜ == 1/10'
max = 10 # upper ep/hp limit
def energy(player): # player/enemy energy bar
    '''input type: obj'''
    '''return type: None'''
    print(f"{player.name}'s Energy")
    space = math.ceil(player.energy/player.max_energy*max) # dictates how many white squares
    ep = ('⬜'*space) + ('⬚'*(max-space))
    print(ep,player.energy,'/',player.max_energy) # display energy bar

def health_bar(player): # player/enemy health bar
    '''input type: obj'''
    '''return type: None'''
    print(f"{player.name}'s Health")
    space = math.ceil(player.health / player.max_health * max)  # dictates how many hearts
    hp = ('♥'*space) + ('♡'*(max-space))
    print(hp,player.health,'/',player.max_health) # display health bar

def peripheral(player):
    '''input type: object'''
    '''return type: None'''
    print(f"{player.name}'s Health            {player.name}'s Energy          ")
    space_ep = math.ceil(player.energy / player.max_energy * max)  # dictates how many white squares
    space_hp = math.ceil(player.health / player.max_health * max)  # dictates how many hearts
    hp = ('♥' * space_hp) + ('♡' * (max - space_hp))
    ep = ('⬜' * space_ep) + ('⬚' * (max - space_ep))
    print(hp, player.health, '/', player.max_health, "   ",ep,player.energy, '/',player.max_energy)  # display health bar

    if(player.playable == 1): # check if playable class
        if(player.class_flag[0] == 1): # Warrior specific addition
            rp = ('⚡'*player.rage) + ('-'*(3-player.rage))
            if(player.rage == 3):
                rp += ' MAX'
            print(f"Rage: {rp}")
        elif(player.class_flag[1] == 1): # Bowman specific addition
            ap = ('➳'*player.accuracy)
            if(player.accuracy == 5):
                ap += ' MAX'
            print(f"Focus: {ap}")
        elif(player.class_flag[2] == 1): # Mage specific addition
            if(player.elemental%2 == 1): # check status of mage
                print("Element: Fire 🔥")
            else:
                print("Element: Ice ❆")
        elif(player.class_flag[3] == 1): # Thief specific addition, gouge counter
            gp = ('▼'*player.gouge_count) + ('▽'*(3 - player.gouge_count))
            print(f"Gouge counter: {gp}")

# 🌢

