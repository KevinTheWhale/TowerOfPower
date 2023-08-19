"""Main body of the game execution"""
import random as rng
import TitleScreen as title
from Assets import newPlayer
from Assets import Floors as fl
from Assets import equipment as equip
import time
## AGENDA ##
'''
- Title Screen - DONE
- info screen - DONE
- combat screen - DONE
- Player Creation - DONE
- Abilities - Thief - DONE
- Enemies/floors - DONE
- Encounter multipliers - DONE
- Shop - DONE
- Game Over/partial resets - DONE
- Fix backpack functionality - 08/13/2023, consider having a bag limit of 4 - DONE 
- Put in timers/delays - DONE
- Incorporate all stats - DONE
- Why do bonus rolls break the game? - DONE
- Fix attack multipliers, use floor 1 formula as reference - DONE
- Add dodge for each floor - DONE
- bowman being attacked is weird at the moment - DONE
- fix bonus rewards - DONE
- Level up after first completion of each floor - DONE
- Enemy info UI - DONE
- mage can switch between ice and fire - DONE
- completion between floors is broken - app, Floors - DONE
- scrap the idea of re-running floors for now - DONE
- prayer stone - DONE
- player stats - ALMOST DONE
'''

"""Execute Title screen here"""
# User choice on whether they want to start a new game or quit.
while(True):
    title.title_screen()
    new_game = input("(Y/I/N): ")
    if(new_game.lower() == 'y'): # User chooses to start a new game
        break # break the loop and proceed forward
    elif(new_game.lower() == 'i'): # User chooses info
        while(True): # Let the player take their time reading
            title.info_screen() # Show info screen
            new_game = input("Return to main menu? (Y/N): ") # Clear their previous choice
            if(new_game.lower() == 'y'): # User chooses to return back to main menu
                new_game = "" # clear choice
                break # break out of the loop
            elif(new_game.lower() == 'n'): # User wants to keep reading
                continue # keep looping
            else: # invalid choice detected
                print("Invalid choice. Please try again. \n")
    elif(new_game.lower() == 'n'):
        print("Coward! Until next time.")
        exit() # Terminate program

""" Player Creation """
# Place restrictions on player name length to <= 8 characters
while(True):
    print("Please name your adventurer (8 character limit).")
    name = input("Name yourself now: ") # prompt for player's name
    if(len(name) > 8):
        print("Error. Name is too long!")
        continue # continue loop until player gets it right.
    else:
        break # break and continue

player = newPlayer.new_player(name) # Execute player object creation

""" Floor Encounters (1-5) """
'''Floor 1'''
encounter = fl.floor_01(player) # Execute 1st floor encounter
if(encounter == True and player.floor_flag[0] == 0): # Player is victorious for the first time
    # send floor one rewards
    bonus_roll = rng.uniform(0,1) # roll for bonus
    player.coin += equip.floor_01_reward() # grant currency reward


    print(f"{player.name} has earned {equip.floor_01_reward()} gold! \n")
    # change the floor flag for floor 1
    player.floor_flag[0] = 1
    # Floor 1 review UI
    title.floor_victory(player)
    time.sleep(3)
    # Level-up
    title.level_up(player)

    # Refresh player hp and ep
    player.health = player.max_health
    player.energy = player.max_energy

    # reset player class counters
    if(player.class_flag[0] == 1): # warrior
        player.rage = 0
    elif(player.class_flag[3] == 1): # thief
        player.gouge_count = 0

    if(bonus_roll > 0.50): # successful bonus roll
        equip.bonus_reward(player) # still a dictionary that can be passed.


'''Floor 2'''
encounter = fl.floor_02(player) # start second encounter
if(encounter == True and player.floor_flag[1] == 0): # Player is victorious for the first time
    bonus_roll = rng.uniform(0, 1)  # roll for bonus
    player.coin += equip.floor_02_reward()  # grant currency reward

    print(f"{player.name} has earned {equip.floor_02_reward()} gold! \n")
    # change the floor flag for floor 2
    player.floor_flag[1] = 1
    # Floor 2 review UI
    title.floor_victory(player)
    time.sleep(3)
    # Level-up
    title.level_up(player)

    # Refresh player hp and ep
    player.health = player.max_health
    player.energy = player.max_energy

    # reset player class counters
    if (player.class_flag[0] == 1):  # warrior
        player.rage = 0
    elif (player.class_flag[3] == 1):  # thief
        player.gouge_count = 0

    if (bonus_roll > 0.50):  # successful bonus roll
        equip.bonus_reward(player) # grant player bonus equipment

'''Floor 3'''
encounter = fl.floor_03(player) # start third encounter
if(encounter == True and player.floor_flag[2] == 0): # Player is victorious for the first time
    bonus_roll = rng.uniform(0, 1)  # roll for bonus
    player.coin += equip.floor_03_reward()  # grant currency reward

    print(f"{player.name} has earned {equip.floor_03_reward()} gold! \n")
    # change the floor flag for floor 3
    player.floor_flag[2] = 1
    # Floor 3 review UI
    title.floor_victory(player)

    # Level-up
    title.level_up(player)

    # Refresh player hp and ep
    player.health = player.max_health
    player.energy = player.max_energy

    # reset player class counters
    if (player.class_flag[0] == 1):  # warrior
        player.rage = 0
    elif (player.class_flag[3] == 1):  # thief
        player.gouge_count = 0

    if (bonus_roll > 0.50):  # successful bonus roll
        equip.bonus_reward(player) # grant player bonus equipment


'''Floor 4'''
encounter = fl.floor_04(player) # start fourth encounter
if(encounter == True and player.floor_flag[3] == 0): # Player is victorious for the first time
    bonus_roll = rng.uniform(0, 1)  # roll for bonus
    player.coin += equip.floor_04_reward()  # grant currency reward


    print(f"{player.name} has earned {equip.floor_04_reward()} gold! \n")
    # change the floor flag for floor 2
    player.floor_flag[3] = 1
    # Floor 4 review UI
    title.floor_victory(player)
    time.sleep(3)

    # level-up
    title.level_up(player)

    # Refresh player hp and ep
    player.health = player.max_health
    player.energy = player.max_energy

    # reset player class counters
    if (player.class_flag[0] == 1):  # warrior
        player.rage = 0
    elif (player.class_flag[3] == 1):  # thief
        player.gouge_count = 0

    if (bonus_roll > 0.50):  # successful bonus roll
        equip.bonus_reward(player) # grant player bonus equipment


'''Floor 5'''
# Allow player to go to final rest before encounter starts
if(sum(player.floor_flag) == 4): # check if previous 4 floors were complete
    # send player to final rest
    print("Moving to final rest....")
    time.sleep(5)
    title.final_rest(player)


# final boss counter for stage 2
final_boss_counter = 0
encounter = fl.floor_05(player,final_boss_counter) # start final encounter
if(encounter == True and player.floor_flag[4] == 0): # Player absolute victory
    title.total_victory(player)
    time.sleep(3)
    # terminate game
    exit()