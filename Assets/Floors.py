
from TitleScreen import combat_ui, resting_hub_ui, ability_ui, backpack_ui, peripheral, game_over, shop, health_bar, energy, floor_01_info, floor_02_info, floor_03_info, floor_04_info, final_floor_info, prayer_stone, player_stats
import time
import random as rng
from Assets import enemies as enemy
from Assets import equipment as equip
"""Floor encounters"""

"""
Shows every setting listed:
- Resting hub
- Floor (1-5)
"""

''' RESTING HUB '''
prayer_limit = ['Strength', 'Dexterity', 'Intellect', 'Luck']
def resting_hub(player):
    '''input type: obj,int'''
    '''return type: None'''
    """Resting hub for player to relax"""
    # Keep player at current health and energy for difficulty purposes, and reset their class counters
    if(player.class_flag[0] == 1): # reset warrior's rage
        player.rage = 0
    elif(player.class_flag[3] == 1): # reset thief gouge
        player.gouge_count = 0

    print("We're safe for now...")
    # Prompt available choices: 'Quit game', 'shop', 'Reenter Tower', 'backpack', 'change equipment'
    while(True):
        resting_hub_ui() # show resting hub UI
        # show player peripherals
        peripheral(player)
        choice = input("Make a choice: ")
        if(choice.lower() == 's'): # Player chooses shop
            # show shop UI
            print("Moving to shop now....")
            time.sleep(5)
            # Show shop options with UI
            while(True):
                shop() # shop UI
                print(f"{player.name}'s gold ⛁: {player.coin} g") # show player's currency
                print(f"{player.name}'s backpack: {player.backpack}") # show player's backpack
                action = input("What will you buy?: ") # prompt for user choice

                if(action == '1'): # full heal option
                    # check player currency
                    if(player.coin < 20):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif(player.health == player.max_health): # if player already has max hp
                        print("You are already at full health!")
                        time.sleep(3)
                        continue
                    else: # update player currency
                        player.coin-= 20
                        # perform full heal
                        print(f"{player.name} has been fully healed!")
                        player.health = player.max_health
                        time.sleep(3)
                        continue
                elif(action == '2'): # full energy option
                    # check player currency
                    if (player.coin < 15):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif(player.energy == player.max_energy): # player already has max ep
                        print("You are already fully energized!")
                        time.sleep(3)
                        continue
                    else:
                        player.coin -= 15
                        print(f"{player.name} has been fully energized!")
                        continue
                elif(action == '3'): # basic health potion option
                    if(player.coin < 15):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif(len(player.backpack) == 4): # player has no backpack space
                        print("Your bag is full! Only 4 items can fit in it.")
                        time.sleep(3)
                        continue
                    else: # update player currency and backpack
                        print(f"{player.name} has purchased a Basic health potion!")
                        time.sleep(3)
                        player.coin -= 15
                        player.backpack.append("Basic health potion (Recover 100 hp)")
                elif(action == '4'): # Basic energy potion option
                    if (player.coin < 10):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif (len(player.backpack) == 4):  # player has no backpack space
                        print("Your bag is full! Only 4 items can fit in it.")
                        time.sleep(3)
                        continue
                    else:  # update player currency and backpack
                        print(f"{player.name} has purchased a Basic energy potion!")
                        time.sleep(3)
                        player.coin -= 10
                        player.backpack.append("Basic energy potion (Recover 50 ep)")
                elif(action == '5'): # Greater health potion option
                    if (player.coin < 25):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif (len(player.backpack) == 4):  # player has no backpack space
                        print("Your bag is full! Only 4 items can fit in it.")
                        time.sleep(3)
                        continue
                    else:  # update player currency and backpack
                        print(f"{player.name} has purchased a Greater health potion!")
                        time.sleep(3)
                        player.coin -= 25
                        player.backpack.append("Greater health potion (Recover 200 hp)")
                elif(action == '6'): # Greater energy potion option
                    if (player.coin < 20):
                        print("You don't have enough gold!")
                        time.sleep(3)
                        continue
                    elif (len(player.backpack) == 4):  # player has no backpack space
                        print("Your bag is full! Only 4 items can fit in it.")
                        time.sleep(3)
                        continue
                    else:  # update player currency and backpack
                        print(f"{player.name} has purchased a Greater energy potion!")
                        time.sleep(3)
                        player.coin -= 20
                        player.backpack.append("Basic energy potion (Recover 100 ep)")
                elif(action.lower() == 'b'): # back to resting hub
                    print("Returning back to resting hub...")
                    time.sleep(5)
                    break
                else: # invalid choice
                    print("Invalid option. Please try again.")
        elif(choice.lower() == 'b'): # Player chooses backpack
            # show backpack contents
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            if (len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                action = '4'
                break  # if your backpack is empty, it should not punish you.
            else:  # view backpack contents
                while (True):
                    backpack_ui(player)  # show backpack ui contents
                    action = input("Action: ")  # player makes a choice
                    choices = [i for i in player.backpack]
                    if (int(action) in range(len(player.backpack) + 1)):  # make a choice within bag
                        equip.potion_dictionary(player,
                                                choices[int(action) - 1])  # retrieve choice in consumable dictionary
                        break  # end turn
                    elif (action == str(len(choices) + 1)):  # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break  # break out of the loop
                if (action == '4'):
                    continue  # bring back to resting_hub ui
        elif(choice.lower() == 'p'): # Player chooses prayer stone
            prayer_stone(player,prayer_limit) # call prayer stone
            continue
        elif(choice.lower() == 'i'): # Player chooses player info
            # show player info
            player_stats(player)
            continue
        elif(choice.lower() == 'e'): # Player chooses to return to the tower
            # return them back to floor 1, make sure to preserve their floor score
            print("Returning to the tower...")
            time.sleep(3) # time delay for immersion
            return # bring them back to current encounter
        elif(choice.lower() == 'q'): # quit game
            game_over() # show game over and terminate game
        else: # invalid choice
            print("Invalid choice. Please try again.")


'''Floor 1 Encounter'''
def floor_01(player):
    '''input type: obj'''
    '''return type: bool'''
    """ Player and enemy object are put into combat """
    # Create enemy object
    opponent = enemy.floor_01_enemy("Billy the Bully")

    # Check 1st floor flag if encounter already finished at some point
    if(player.floor_flag[0] == 1):
        # Floor 1 has finished at some point. Update enemy health and energy rate
        opponent.health = 150
        opponent.energy_rate = 10
        nerf = 0.5
        print(f"{opponent.name} has awakened once more, but is severely weakened...")
    else: # first encounter, attack power of enemy is standard
        nerf = 1

    '''Start the encounter'''
    print("Loading Floor 1...\n")
    time.sleep(5)
    print(f"{opponent.name} approaches you...\n")
    time.sleep(3)

    # Player always starts first
    while(True):
        # display combat ui
        combat_ui()
        time.sleep(0.5)
        # display player peripherals
        peripheral(player)
        # display enemy peripherals
        peripheral(opponent)
        # prompt player choice
        action = input("Action: ")
        if(action.lower() == 'a'): # player chooses to 'attack'
            while(True):
                # show all abilities
                ability_ui(player)
                # prompt for choice within abilities and make sure they have sufficient energy to spend
                action = input("Action: ")
                if(action == '1' and player.energy >= player.cost[0]): # 1st ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break # end turn
                elif(action == '2' and player.energy >= player.cost[1]): # 2nd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break
                elif(action == '3' and player.energy == player.max_energy): # 3rd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break # end turn
                elif(action == '4'): # Player goes back
                    break # bring back to combat_ui
                else:
                    print("you either picked a wrong choice or not enough energy!")

            # Show enemy health after attack was performed
            health_bar(opponent)
            # Check if enemy is dead
            if(opponent.health <= 0):
                print(f"{opponent.name} has been slain!")
                time.sleep(5)
                # Victory, return True
                return True # return True
            # Check if player went 'back' to combat_ui
            if(action == '4'):
                continue # bring back to combat_ui
        elif(action.lower() == 'b'): # player chooses to access backpack
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            time.sleep(3)
            if(len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                continue # if your backpack is empty, it should not punish you.
            else: # view backpack contents
                while(True):
                    backpack_ui(player) # show backpack ui contents
                    action = input("Action: ") # player makes a choice
                    choices = [i for i in player.backpack]
                    if(int(action) in range(len(player.backpack)+1)): # make a choice within bag
                        equip.potion_dictionary(player,choices[int(action)-1]) # retrieve choice in consumable dictionary
                        time.sleep(3)
                        break # end turn
                    elif(action == str(len(choices)+1)): # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break # break out of the loop

            # player changed their mind and headed back to combat_ui
            if(action == '4'):
                continue # bring back to combat_ui
            else:
            # player ends their turn
                print(f"{player.name} finishes their turn...")
        elif(action.lower() == 'e'):
            # Player chooses an escape attempt
            if(player.escape() and player.floor_flag[0] == 0):
                # successful escape: return to hub
                resting_hub(player)
                # Player has returned to the tower, recover enemy stats
                opponent = enemy.floor_01_enemy("Billy the Bully")
                continue # redo encounter
            elif(player.floor_flag[3] == 1): # final encounter version of floor 1
                print("Renjiro's chamber is sealed! There is no escape!")
                time.sleep(3)
                continue # go back to combat_ui
            else: # failed escape
                pass
        elif(action.lower() == 's'): # player skips turn due to lack of energy and/or lack of items
            print(f"{player.name} skips their turn...")
            pass # skip player turn
        elif(action.lower() == 'i'): # player chooses floor info
            # display floor info
            floor_01_info()
            # prompt user to go back
            action = input("Input any button to continue.")
            continue # bring back to combat_ui
        elif(action.lower() == 'q'): # player quits the game
            print("Game Over!")
            exit() # terminate the game
        else: # Player makes an invalid choice. bring them back to combat_ui
            print("Invalid choice. Please try again.")
            continue

        time.sleep(2)
        # Update player energy at the end of their turn.
        print(f"{player.name} regenerates {player.energy_rate} energy...\n")
        player.energy += player.energy_rate
        # check if it is over energy
        if(player.energy > player.max_energy):
            player.energy = player.max_energy

        time.sleep(5) # Put a delay timer here for turn transition

        ## START ENEMY TURN ##
        print(f"{opponent.name} readies themselves...\n")
        time.sleep(3)
        # check player dodge chance
        if(player.dodge()):
            dodge = 0  # successful dodge
            print(f"{player.name} successfully dodged!")
            time.sleep(1)
        else:
            dodge = 1  # unsuccessful dodge
            print(f"{player.name} failed to dodge!")
            time.sleep(1)

        # Check if they have max energy to perform ultimate
        if(opponent.energy == opponent.max_energy):
            # always perform ultimate if max energy is achieved
            for i in opponent.ultimate.keys():
                time.sleep(3)
                print(f"{opponent.name} unleashes their ultimate! ", i, "!\n")
                # attack player
                player.health -= (opponent.ultimate[i]*(player.attire - player.int*0.05))*nerf*dodge
                time.sleep(3)
                print(f"{opponent.name} attacks for {(opponent.ultimate[i]*(player.attire - player.int*0.05))*nerf*dodge}!\n")
            # update opponent energy after ultimate
                opponent.energy = 0
            # show player health
                health_bar(player)
            # check if player is slain
                time.sleep(3)
            if(player.health <= 0):
                print(f"{player.name} has been slain!\n")
                # game over
                time.sleep(3)
                game_over()# terminate game, consider doing a continue?
        else: # regular enemy turn
            # all enemy ability choices are based on a roll
            roll = [i for i in opponent.abilities.keys()][rng.randint(0,1)]
            # attack player
            # add a delay here
            player.health -= (opponent.abilities[roll]*(player.attire-player.int*0.05))*nerf*dodge
            time.sleep(3)
            print(f"{opponent.name} strikes {player.name} with {roll} for {(opponent.abilities[roll]*(player.attire - player.int*0.05))*nerf*dodge}!\n")
            # Show updated player health
            health_bar(player)
            time.sleep(3)
            # check if player has been slain
            if(player.health <= 0):
                print(f"{player.name} has been slain!\n")
                time.sleep(5)
                game_over() # terminate game

            # Otherwise, enemy regenerates energy, compensates for over energy
            opponent.energy += opponent.energy_rate
            if(opponent.energy > opponent.max_energy):
                opponent.energy = opponent.max_energy
                time.sleep(3)
            elif(opponent.energy == opponent.max_energy):
                print(f"{opponent.name} has reached max energy!\n")
                energy(opponent)
            time.sleep(3)
            print(f"{opponent.name} backs up....\n")
            # End of opponent turn, back to player turn

'''Floor 2 Encounter'''
def floor_02(player):
    '''input type: object'''
    '''return type: bool'''
    """ Player and enemy object are put into combat """
    # Create enemy object
    opponent = enemy.floor_02_enemy("Debbie Downer")

    # Check 2nd floor flag if encounter already finished at some point
    if (player.floor_flag[1] == 1):
        # Floor 2 has finished at some point. Update enemy health and energy rate
        opponent.health = 250
        opponent.energy_rate = 12.5
        nerf = 0.5
        print(f"{opponent.name} has awakened once more, but is severely weakened...")
    else:
        nerf = 1

    '''Start the encounter'''
    print("Loading Floor 2...\n")
    time.sleep(5)
    print(f"{opponent.name} approaches you...\n")
    time.sleep(3)

    # Player always starts first
    while(True):
        # display combat ui
        combat_ui()
        time.sleep(0.5)
        # display player peripherals
        peripheral(player)
        # display enemy peripherals
        peripheral(opponent)
        # prompt player choice
        action = input("Action: ")
        if (action.lower() == 'a'):  # player chooses to 'attack'
            while (True):
                # show all abilities
                ability_ui(player)
                # prompt for choice within abilities and make sure they have sufficient energy to spend
                action = input("Action: ")
                if (action == '1' and player.energy >= player.cost[0]):  # 1st ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '2' and player.energy >= player.cost[1]):  # 2nd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break
                elif (action == '3' and player.energy == player.max_energy):  # 3rd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '4'):  # Player goes back
                    break  # bring back to combat_ui
                else:
                    print("you either picked a wrong choice or not enough energy!")

            # Show enemy health after attack was performed
            health_bar(opponent)
            # Check if enemy is dead
            if (opponent.health <= 0):
                print(f"{opponent.name} has been slain!")
                time.sleep(5)
                # Victory, return True
                return True  # return True
            # Check if player went 'back' to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
        elif (action.lower() == 'b'):  # player chooses to access backpack
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            time.sleep(3)
            if (len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                continue  # if your backpack is empty, it should not punish you.
            else:  # view backpack contents
                while (True):
                    backpack_ui(player)  # show backpack ui contents
                    action = input("Action: ")  # player makes a choice
                    choices = [i for i in player.backpack]
                    if (int(action) in range(len(player.backpack) + 1)):  # make a choice within bag
                        equip.potion_dictionary(player,
                                                choices[int(action) - 1])  # retrieve choice in consumable dictionary
                        time.sleep(3)
                        break  # end turn
                    elif (action == str(len(choices) + 1)):  # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break  # break out of the loop

            # player changed their mind and headed back to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
            else:
                # player ends their turn
                print(f"{player.name} finishes their turn...")
        elif (action.lower() == 'e'):
            # Player chooses an escape attempt
            if (player.escape() and player.floor_flag[1] == 0):
                # successful escape: return to hub
                resting_hub(player)
                # player stays with current health and energy, opponent however resets
                opponent = enemy.floor_02_enemy("Debbie Downer")
                continue
            elif(player.floor_flag[3] == 1):  # final encounter version of floor 2
                print("Renjiro's chamber is sealed! There is no escape!")
                time.sleep(3)
                continue  # go back to combat_ui
            else:
                pass
        elif (action.lower() == 's'):  # player skips turn due to lack of energy and/or lack of items
            print(f"{player.name} skips their turn...")
            pass  # skip player turn
        elif (action.lower() == 'i'):  # player chooses floor info
            # display floor info
            floor_02_info()
            # prompt user to go back
            action = input("Input any button to continue.")
            continue  # bring back to combat_ui
        elif (action.lower() == 'q'):  # player quits the game
            print("Game Over!")
            exit()  # terminate the game
        else:  # Player makes an invalid choice. bring them back to combat_ui
            print("Invalid choice. Please try again.")
            continue

        time.sleep(2)
        # Update player energy at the end of their turn.
        print(f"{player.name} regenerates {player.energy_rate} energy...\n")
        player.energy += player.energy_rate
        # check if it is over energy
        if (player.energy > player.max_energy):
            player.energy = player.max_energy

        time.sleep(5)  # Put a delay timer here for turn transition

        ## START ENEMY TURN ##
        print(f"{opponent.name} readies themselves...\n")
        time.sleep(3)
        # check player dodge chance
        if (player.dodge()):
            dodge = 0  # successful dodge
            print(f"{player.name} successfully dodged!")
            time.sleep(1)
        else:
            dodge = 1  # unsuccessful dodge
            print(f"{player.name} failed to dodge!")
            time.sleep(1)

        # Check if they have max energy to perform ultimate
        if (opponent.energy == opponent.max_energy):
            # always perform ultimate if max energy is achieved
            for i in opponent.ultimate.keys():
                time.sleep(3)
                print(f"{opponent.name} unleashes their ultimate! ", i, "!\n")
                # attack player
                player.health -= (opponent.ultimate[i]*player.attire*(player.int*0.05))*nerf*dodge
                time.sleep(3)
                print(f"{opponent.name} attacks for {(opponent.ultimate[i]*player.attire*(player.int*0.05))*nerf*dodge}!\n")
                time.sleep(2)

            print(f"{player.name}'s energy has been drained for {opponent.drain} points! \n")
            player.energy -= opponent.drain # drain player energy as part of ultimate

            # Update opponent energy after ultimate
            opponent.energy = 0
            if(player.energy < 0):
                player.energy = 0 # correction for negative energy
                time.sleep(2)
                # show player peripherals
                peripheral(player)
                # check if player is slain
                time.sleep(3)
            if(player.health <= 0):
                print(f"{player.name} has been slain!\n")
                # game over
                time.sleep(3)
                game_over()  # terminate game, consider doing a continue?
        else:  # regular enemy turn
            # all enemy ability choices are based on a roll
            roll = [i for i in opponent.abilities.keys()][rng.randint(0, 1)]
            # attack player
            # add a delay here
            player.health -= (opponent.abilities[roll]*(player.attire-player.int*0.05))*nerf*dodge
            time.sleep(3)
            print(f"{opponent.name} strikes {player.name} with {roll} for {(opponent.abilities[roll]*(player.attire-player.int*0.05))*nerf*dodge}!\n")
            # Show updated health
            health_bar(player)
            time.sleep(3)
            # check if player has been slain
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                time.sleep(5)
                game_over()  # terminate game

            # Otherwise, enemy regenerates energy, compensates for over energy
            opponent.energy += opponent.energy_rate
            if (opponent.energy > opponent.max_energy):
                opponent.energy = opponent.max_energy
                time.sleep(3)
            elif(opponent.energy == opponent.max_energy):
                print(f"{opponent.name} has reached max energy!\n")
                energy(opponent)
                time.sleep(3)
            print(f"{opponent.name} backs up....\n")
            # End of opponent turn, back to player turn


'''Floor 3 Encounter'''
def floor_03(player):
    '''input type: Object'''
    '''return type: bool'''
    """ Player and enemy object are put into combat """
    # Create enemy object
    opponent = enemy.floor_03_enemy("Slippery Sam")

    # Check 3rd floor flag if encounter already finished at some point
    if (player.floor_flag[2] == 1):
        # Floor 1 has finished at some point. Update enemy health and energy rate
        opponent.health = 275
        opponent.energy_rate = 20
        nerf = 0.5
        print(f"{opponent.name} has awakened once more, but is severely weakened...")
    else:
        nerf = 1

    '''Start the encounter'''
    print("Loading Floor 3...\n")
    time.sleep(5)
    print(f"{opponent.name} approaches you...\n")
    time.sleep(3)

    # Player always starts first
    while(True):
        # display combat ui
        combat_ui()
        time.sleep(0.5)
        # display player peripherals
        peripheral(player)
        # display enemy peripherals
        peripheral(opponent)
        # prompt player choice

        if(opponent.poison_flag == 1): # check poison flag
            print(f"{player.name} suffers 10 poison damage!")
            # update player health
            player.health -= opponent.poison
            # update poison counter
            opponent.poison_counter += 1
            if(opponent.poison_counter == 3): # after the 3rd turn, turn off flag to be renewed
                opponent.poison_flag = 0
            time.sleep(3)

        action = input("Action: ")
        if (action.lower() == 'a'):  # player chooses to 'attack'
            while (True):
                # show all abilities
                ability_ui(player)
                # prompt for choice within abilities and make sure they have sufficient energy to spend
                action = input("Action: ")
                if (action == '1' and player.energy >= player.cost[0]):  # 1st ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '2' and player.energy >= player.cost[1]):  # 2nd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break
                elif (action == '3' and player.energy == player.max_energy):  # 3rd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '4'):  # Player goes back
                    break  # bring back to combat_ui
                else:
                    print("you either picked a wrong choice or not enough energy!")

            # Show enemy health after attack was performed
            health_bar(opponent)
            # Check if enemy is dead
            if (opponent.health <= 0):
                print(f"{opponent.name} has been slain!")
                time.sleep(5)
                # Victory, return True
                return True  # return True
            # Check if player went 'back' to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
        elif (action.lower() == 'b'):  # player chooses to access backpack
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            time.sleep(3)
            if (len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                continue  # if your backpack is empty, it should not punish you.
            else:  # view backpack contents
                while (True):
                    backpack_ui(player)  # show backpack ui contents
                    action = input("Action: ")  # player makes a choice
                    choices = [i for i in player.backpack]
                    if (int(action) in range(len(player.backpack) + 1)):  # make a choice within bag
                        equip.potion_dictionary(player,
                                                choices[int(action) - 1])  # retrieve choice in consumable dictionary
                        time.sleep(3)
                        break  # end turn
                    elif (action == str(len(choices) + 1)):  # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break  # break out of the loop

            # player changed their mind and headed back to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
            else:
                # player ends their turn
                print(f"{player.name} finishes their turn...")
        elif (action.lower() == 'e'):
            # Player chooses an escape attempt
            if (player.escape() and player.floor_flag[2] == 0):
                # successful escape: return to hub
                resting_hub(player)
                # player stays with current health and energy, opponent however resets
                opponent = enemy.floor_03_enemy("Slippery Sam")
                continue # redo encounter
            elif(player.floor_flag[3]==1): # final encounter version of floor 3
                print("Renjiro's chamber is sealed! There is no escape!")
                time.sleep(3)
                continue # go back to combat_ui
            else:
                pass
        elif (action.lower() == 's'):  # player skips turn due to lack of energy and/or lack of items
            print(f"{player.name} skips their turn...")
            pass  # skip player turn
        elif (action.lower() == 'i'):  # player chooses floor info
            # display floor info
            floor_03_info()
            # prompt user to go back
            action = input("Input any button to continue.")
            continue  # bring back to combat_ui
        elif (action.lower() == 'q'):  # player quits the game
            print("Game Over!")
            exit()  # terminate the game
        else:  # Player makes an invalid choice. bring them back to combat_ui
            print("Invalid choice. Please try again.")
            continue

        time.sleep(2)
        # Update player energy at the end of their turn.
        print(f"{player.name} regenerates {player.energy_rate} energy...\n")
        player.energy += player.energy_rate
        # check if it is over energy
        if (player.energy > player.max_energy):
            player.energy = player.max_energy

        time.sleep(5)  # Put a delay timer here for turn transition

        ## START ENEMY TURN ##
        print(f"{opponent.name} readies themselves...\n")
        time.sleep(3)
        # Check player dodge chance
        if (player.dodge()):
            dodge = 0  # successful dodge
            print(f"{player.name} successfully dodged!")
            time.sleep(1)
        else:
            dodge = 1  # unsuccessful dodge
            print(f"{player.name} failed to dodge!")
            time.sleep(1)

        # Check if they have max energy to perform ultimate
        if (opponent.energy == opponent.max_energy):
            # always perform ultimate if max energy is achieved
            for i in opponent.ultimate.keys():
                time.sleep(3)
                print(f"{opponent.name} unleashes their ultimate! ", i, "!\n")
                # attack player
                player.health -= (opponent.ultimate[i]*(player.attire - player.int*0.05))*nerf*dodge
                time.sleep(3)
                print(f"{opponent.name} attacks for {(opponent.ultimate[i]*(player.attire - player.int*0.05))*nerf*dodge}!\n")
                time.sleep(2)

            print(f"{player.name}'s has has been poisoned for 3 turns! \n")
            # change poison flag to 1 for poison status
            opponent.poison_flag = 1
            # set up poison counter
            opponent.poison_counter = 0

            # Update opponent energy after ultimate
            opponent.energy = 0
            time.sleep(2)
            # show player health
            health_bar(player)
            # check if player is slain
            time.sleep(3)
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                # game over
                time.sleep(3)
                game_over()  # terminate game, consider doing a continue?
        else:  # regular enemy turn
            # all enemy ability choices are based on a roll
            roll = [i for i in opponent.abilities.keys()][rng.randint(0, 1)]
            # attack player
            # add a delay here
            player.health -= (opponent.abilities[roll]*(player.attire-player.int*0.05))*nerf*dodge
            time.sleep(3)
            print(f"{opponent.name} strikes {player.name} with {roll} for {(opponent.abilities[roll]*(player.attire-player.int*0.05))*nerf*dodge}!\n")
            # Show updated peripherals
            health_bar(player)
            time.sleep(3)
            # check if player has been slain
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                time.sleep(5)
                game_over()  # terminate game

            # Otherwise, enemy regenerates energy, compensates for over energy
            opponent.energy += opponent.energy_rate
            if (opponent.energy > opponent.max_energy):
                opponent.energy = opponent.max_energy
                time.sleep(3)
            elif(opponent.energy == opponent.max_energy):
                print(f"{opponent.name} has reached max energy!\n")
                energy(opponent)
                time.sleep(3)
            print(f"{opponent.name} backs up....\n")
            # End of opponent turn, back to player turn


'''Floor 4 Encounter'''
def floor_04(player):
    '''input type: Object'''
    '''return type: bool'''
    """ Player and enemy object are put into combat """
    # Create enemy object
    opponent = enemy.floor_04_enemy("Furious Fred")

    # Check 4th floor flag if encounter already finished at some point
    if (player.floor_flag[3] == 1):
        # Floor 1 has finished at some point. Update enemy health and energy rate
        opponent.health = 300
        opponent.energy_rate = 12.5
        nerf = 0.5
        print(f"{opponent.name} has awakened once more, but is severely weakened...")
    else:
        nerf = 1

    '''Start the encounter'''
    print("Loading Floor 4...\n")
    time.sleep(5)
    print(f"{opponent.name} approaches you...\n")
    time.sleep(3)

    # Player always starts first
    while(True):
        # display combat ui
        combat_ui()
        time.sleep(0.5)
        # display player peripherals
        peripheral(player)
        # display enemy peripherals
        peripheral(opponent)
        # prompt player choice
        action = input("Action: ")
        if (action.lower() == 'a'):  # player chooses to 'attack'
            while (True):
                # show all abilities
                ability_ui(player)
                # prompt for choice within abilities and make sure they have sufficient energy to spend
                action = input("Action: ")
                if (action == '1' and player.energy >= player.cost[0]):  # 1st ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '2' and player.energy >= player.cost[1]):  # 2nd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break
                elif (action == '3' and player.energy == player.max_energy):  # 3rd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '4'):  # Player goes back
                    break  # bring back to combat_ui
                else:
                    print("you either picked a wrong choice or not enough energy!")

            # Show enemy health after attack was performed
            health_bar(opponent)
            # Check if enemy is dead
            if (opponent.health <= 0):
                print(f"{opponent.name} has been slain!")
                time.sleep(5)
                # Victory, return True
                return True  # return True
            # Check if player went 'back' to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
        elif (action.lower() == 'b'):  # player chooses to access backpack
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            time.sleep(3)
            if (len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                continue  # if your backpack is empty, it should not punish you.
            else:  # view backpack contents
                while (True):
                    backpack_ui(player)  # show backpack ui contents
                    action = input("Action: ")  # player makes a choice
                    choices = [i for i in player.backpack]
                    if (int(action) in range(len(player.backpack) + 1)):  # make a choice within bag
                        equip.potion_dictionary(player,
                                                choices[int(action) - 1])  # retrieve choice in consumable dictionary
                        time.sleep(3)
                        break  # end turn
                    elif (action == str(len(choices) + 1)):  # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break  # break out of the loop

            # player changed their mind and headed back to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
            else:
                # player ends their turn
                print(f"{player.name} finishes their turn...")
        elif (action.lower() == 'e'):
            # Player chooses an escape attempt
            # successful escape: return to hub
            if(player.escape()): # successful escape: return to hub
                resting_hub(player)
                 # player stays with current health and energy, opponent however resets
                opponent = enemy.floor_04_enemy("Furious Fred")
                continue # redo encounter
            elif(player.floor_flag[3]==1):  # final encounter version of floor 4
                print("Renjiro's chamber is sealed! There is no escape!")
                time.sleep(3)
                continue # go back to combat_ui
            else:
                pass
        elif (action.lower() == 's'):  # player skips turn due to lack of energy and/or lack of items
            print(f"{player.name} skips their turn...")
            pass  # skip player turn
        elif (action.lower() == 'i'):  # player chooses floor info
            # display floor info
            floor_04_info()
            # prompt user to go back
            action = input("Input any button to continue.")
            continue  # bring back to combat_ui
        elif (action.lower() == 'q'):  # player quits the game
            print("Game Over!")
            exit()  # terminate the game
        else:  # Player makes an invalid choice. bring them back to combat_ui
            print("Invalid choice. Please try again.")
            continue

        time.sleep(2)
        # Update player energy at the end of their turn.
        print(f"{player.name} regenerates {player.energy_rate} energy...\n")
        player.energy += player.energy_rate
        # check if it is over energy
        if (player.energy > player.max_energy):
            player.energy = player.max_energy

        time.sleep(5)  # Put a delay timer here for turn transition

        ## START ENEMY TURN ##
        print(f"{opponent.name} readies themselves...\n")
        time.sleep(3)
        # Check player dodge chance
        if (player.dodge()):
            dodge = 0  # successful dodge
            print(f"{player.name} successfully dodged!")
            time.sleep(1)
        else:
            dodge = 1  # unsuccessful dodge
            print(f"{player.name} failed to dodge!")
            time.sleep(1)

        # Check if they have max energy to perform ultimate
        if (opponent.energy == opponent.max_energy):
            # always perform ultimate if max energy is achieved
            for i in opponent.ultimate.keys():
                time.sleep(3)
                print(f"{opponent.name} unleashes their ultimate! ", i, "!\n")
                print(f"{opponent.name} attack power increased by 50%!")
                opponent.ultimate_flag+=1 # change flag

            # Update opponent energy after ultimate
            opponent.energy = 0
            time.sleep(2)
        else:  # regular enemy turn
            # all enemy ability choices are based on a roll
            roll = [i for i in opponent.abilities.keys()][rng.randint(0, 1)]
            # attack player
            # add a delay here
            player.health -= (opponent.abilities[roll]*(player.attire - player.int*0.05) + opponent.ultimate_flag*opponent.ultimate['Enrage']*opponent.abilities[roll])*nerf*dodge
            time.sleep(3)
            print(f"{opponent.name} strikes {player.name} with {roll} for {(opponent.abilities[roll]*(player.attire - player.int*0.05) + opponent.ultimate_flag*opponent.ultimate['Enrage']*opponent.abilities[roll])*nerf*dodge}!\n")
            # Show updated health
            health_bar(player)
            time.sleep(3)
            # check if player has been slain
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                time.sleep(5)
                game_over()  # terminate game

            # Otherwise, enemy regenerates energy, compensates for over energy
            # Floor 4: Opponent gets bonus energy and boosted energy rate
            opponent.energy += (opponent.energy_rate + opponent.bonus_energy)
            print(f"{opponent.name} gets angrier and boosts their energy!")
            # show enemy energy bar
            energy(opponent)
            time.sleep(3)
            if (opponent.energy > opponent.max_energy):
                opponent.energy = opponent.max_energy
                time.sleep(3)
            elif(opponent.energy == opponent.max_energy):
                print(f"{opponent.name} has reached max energy!\n")
                energy(opponent)
                time.sleep(3)
            print(f"{opponent.name} backs up....\n")
            # End of opponent turn, back to player turn


'''Floor 5 Encounter (Final Boss)'''
def floor_05(player,final_boss_counter):
    '''input type: Object,int'''
    '''return type: bool'''
    """ Player and enemy object are put into combat """
    # Create enemy object
    opponent = enemy.final_enemy("Renjiro")

    '''Start the encounter'''
    print("Loading Final Floor...\n")
    time.sleep(5)
    print("Renjiro, The Titan approaches you...\n")
    time.sleep(3)
    print("Renjiro seals the chamber. Escape is now impossible!")
    time.sleep(2)

    # Player always starts first
    while(True):
        # display combat ui
        combat_ui()
        time.sleep(0.5)
        # display player peripherals
        peripheral(player)
        # display enemy peripherals
        peripheral(opponent)
        # prompt player choice
        action = input("Action: ")
        if (action.lower() == 'a'):  # player chooses to 'attack'
            while (True):
                # show all abilities
                ability_ui(player)
                # prompt for choice within abilities and make sure they have sufficient energy to spend
                action = input("Action: ")
                if (action == '1' and player.energy >= player.cost[0]):  # 1st ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '2' and player.energy >= player.cost[1]):  # 2nd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break
                elif (action == '3' and player.energy == player.max_energy):  # 3rd ability
                    attack = player.perform(action)
                    opponent.health -= attack
                    print(f"{player.name} strikes {opponent.name} for {attack}!")
                    break  # end turn
                elif (action == '4'):  # Player goes back
                    break  # bring back to combat_ui
                else:
                    print("you either picked a wrong choice or not enough energy!")

            # Show enemy peripherals after attack was performed
            peripheral(opponent)
            # Check if enemy is dead
            if (opponent.health <= 0):
                print(f"{opponent.name} has been slain!")
                # Victory, return True
                time.sleep(3)
                return True  # return True
            # Check if player went 'back' to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
        elif (action.lower() == 'b'):  # player chooses to access backpack
            print(f"{player.name} opens up their backpack...")
            # Check if backpack is empty
            time.sleep(3)
            if (len(player.backpack) == 0):
                print(f"{player.name}'s backpack is empty!")
                continue  # if your backpack is empty, it should not punish you.
            else:  # view backpack contents
                while (True):
                    backpack_ui(player)  # show backpack ui contents
                    action = input("Action: ")  # player makes a choice
                    choices = [i for i in player.backpack]
                    if (int(action) in range(len(player.backpack) + 1)):  # make a choice within bag
                        equip.potion_dictionary(player,
                                                choices[int(action) - 1])  # retrieve choice in consumable dictionary
                        time.sleep(3)
                        break  # end turn
                    elif (action == str(len(choices) + 1)):  # change your mind
                        print(f"{player.name} zips up their backpack.")
                        action = '4'
                        break  # break out of the loop

            # player changed their mind and headed back to combat_ui
            if (action == '4'):
                continue  # bring back to combat_ui
            else:
                # player ends their turn
                print(f"{player.name} finishes their turn...")
        elif (action.lower() == 'e'): # Player chooses an escape attempt
            # On the final floor, escape is no longer an option.
            print("Renjiro's chamber is sealed! Escape is no longer an option!")
            time.sleep(3)
            continue # redo encounter
        elif (action.lower() == 's'):  # player skips turn due to lack of energy and/or lack of items
            print(f"{player.name} skips their turn...")
            pass  # skip player turn
        elif (action.lower() == 'i'):  # player chooses floor info
            # display floor info
            final_floor_info()
            # prompt user to go back
            action = input("Input any button to continue.")
            continue  # bring back to combat_ui
        elif (action.lower() == 'q'):  # player quits the game
            print("Game Over!")
            exit()  # terminate the game
        else:  # Player makes an invalid choice. bring them back to combat_ui
            print("Invalid choice. Please try again.")
            continue

        time.sleep(2)
        # Update player energy at the end of their turn.
        print(f"{player.name} regenerates {player.energy_rate} energy...\n")
        player.energy += player.energy_rate
        # check if it is over energy
        if (player.energy > player.max_energy):
            player.energy = player.max_energy

        time.sleep(5)  # Put a delay timer here for turn transition

        ## START ENEMY TURN ##
        print(f"{opponent.name} readies themselves...\n")
        time.sleep(3)
        # Check player dodge chance
        if (player.dodge()):
            dodge = 0  # successful dodge
            print(f"{player.name} successfully dodged!")
            time.sleep(1)
        else:
            dodge = 1  # unsuccessful dodge
            print(f"{player.name} failed to dodge!")
            time.sleep(1)

        # Check if they have max energy to perform ultimate
        if (opponent.energy == opponent.max_energy):
            # always perform ultimate if max energy is achieved
            for i in opponent.ultimate.keys():
                time.sleep(3)
                print(f"{opponent.name} unleashes their ultimate! ", i, "!\n")
                print(f"{opponent.name} attacks for {(opponent.ultimate[i]*player.attire*(player.int*0.05))*dodge}!")
                player.health -= (opponent.ultimate[i]*player.attire*(player.int*0.05))*dodge


            # Update opponent energy after ultimate
            opponent.energy = 0
            time.sleep(2)
            # show player peripherals
            peripheral(player)
            time.sleep(3)
            # check if player is slain
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                # game over
                time.sleep(3)
                game_over()  # terminate game, consider doing a continue?
        else:  # regular enemy turn
            # Check if hp is low enough for stage 2
            if(opponent.health <= 1000 and final_boss_counter == 0):
                # Renjiro re-summons minions
                print(f"{opponent.name} backs off and sits on his throne....")
                time.sleep(3)
                print(f"{opponent.name} starts re-summoning his minions!")
                time.sleep(3)

                # Re-summon all previous floor enemies
                if(floor_01(player)): # re-summon floor 1
                    print(f"The thrill of battle empowers {player.name}!")
                    print(f"{player.name} gains 50 max hp and heals for 50 hp!")
                    player.max_health += 50 # give max hp bonus
                    player.health += 50 # heal for 50 hp
                    # show player health
                    health_bar(player)
                    time.sleep(3)
                if(floor_02(player)): # re-summon floor 2
                    print("A Divine force sees your valiant effort and you receive its blessing!")
                    time.sleep(1)
                    print(f"{player.name} gains 50 max ep and becomes fully energized!")
                    # grant energy bonuses
                    player.max_energy += 50
                    player.energy = player.max_energy
                    # show player energy
                    energy(player)
                    time.sleep(3)
                if(floor_03(player)): # re-summon floor 3
                    print("The Gods favor your bravery and grant you a blessing!")
                    time.sleep(1)
                    print(f"{player.name} energy rate increases by 20!")
                    # grant energy rate bonus
                    player.energy_rate+=20
                    time.sleep(3)
                if(floor_04(player)): # re-summon floor 4
                    print("The final minion has been slain!")
                    time.sleep(1)
                    print(f"{player.name} focuses power within themselves and boosts all stats by 1!")
                    # grant stat bonuses
                    player.str+=1
                    player.dex+=1
                    player.int+=1
                    player.luk+=1
                    time.sleep(3)
                opponent.stage_2() # queue in stage 2 abilities and energy rate
                final_boss_counter = 1 # increment flag only once to make sure it runs once.
                print(f"{opponent.name} has entered stage 2 with amplified abilities and energy rate!")
                time.sleep(5)
                continue # player always goes first

            # all enemy ability choices are based on a roll
            roll = [i for i in opponent.abilities.keys()][rng.randint(0, 1)]
            # attack player
            player.health -= (opponent.abilities[roll]*(player.attire-player.int*0.05))*dodge

            time.sleep(3)
            print(f"{opponent.name} strikes {player.name} with {roll} for {opponent.abilities[roll]}!\n")
            # Show updated peripherals
            peripheral(player)
            time.sleep(3)
            # check if player has been slain
            if (player.health <= 0):
                print(f"{player.name} has been slain!\n")
                time.sleep(5)
                game_over()  # terminate game

            # Otherwise, enemy regenerates energy, compensates for over energy
            opponent.energy += opponent.energy_rate
            if (opponent.energy > opponent.max_energy):
                opponent.energy = opponent.max_energy
                time.sleep(3)
            elif(opponent.energy == opponent.max_energy):
                print(f"{opponent.name} has reached max energy!\n")
                energy(opponent)
                time.sleep(3)
            print(f"{opponent.name} backs up....\n")
            # End of opponent turn, back to player turn


















