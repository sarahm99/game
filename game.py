import sys
from time import sleep
import random
 
safe_open = False
player_health = 3
keys_collected = 0
key_picked_up = False
 
def menu_screen():
    print("Press 1 to begin\n2 for a help menu\nq to quit")
    y = input()
    if y == "1":
        begin()
    elif y == "2":
        help_menu()
    elif y == "q":
        quit()
       
def quit():
    sys.exit()
 
def help_menu():
    print("In game, type /inventory in the terminal at safe points to open your inventory.  Type 'q' to quit the game.")
    menu_screen()
 
def keys_to_zone_4():
    if keys_collected == 3:
        print("Good job.")
        zone4_sarah()
    elif keys_collected == 2:
        print("You have collected 2 keys")
        starting_room_repeat()
    elif keys_collected == 1:
        print("You have collected 1 key.")
        starting_room_repeat()
# Introduces user to the main objective
def begin():
    print("")
    print("The objective of this game is to escape.  Investigate, find objects and be mindful of your decisions.")
    print("")
# Introduces game mechanics before introducing player to main part of the game.
    print("During the game, you will be able to input certain commands in the terminal at most points in the game to check the current state of something.\nTo check your inventory space, type '/inventory'.")
    intro_text_2()
 
# def game_end_door_text():
#     print("You find a door that has 5 locks in total.\nThe top lock has a key inside it already.\nThe rest of the locks are empty.")
 
def intro_text_2():
    print("A sudden loud noise of thunder wakes you up, and you lie confused in an unknown surrounding, disorientated and stiff frozen.  Where am i?  What is happening?  The thunder gets louder and louder and with every lightening your heart starts racing faster and faster.\nAll of a sudden you notice two doors.\nYou thought you were having a nightmare but your nightmare became a reality.  Will you be able to escape?")
    prompt_1()
 
# Empty list called inventory to act as our inventory system
Inventory = []
 
def add_item(item):
    Inventory.append(item)
    print(f"{item} has been added into your inventory.")
 
 
# Lists all items a player currently has
def inventory_list():
    global Inventory
    print("Currently, you have:")
    for item in Inventory:
        print(item)
 
def prompt_1():
    global Inventory
    print("As you regain consciousness, you notice a knife laying next to you on the bed you woke up on, as if you were meant to see it.  Although, you feel apprehension in handling a weapon right now.  It may be a good idea to not be armed")
    def question():
        global x_prompt_1
        x_prompt_1 = input("Do you pick up the knife (1) or leave it (2)?")
        if x_prompt_1 == "1":
            add_item("knife")
            starting_room()
        elif x_prompt_1 == "2":
            print("You decide it is wiser to appear unarmed.")
            starting_room()
        elif x_prompt_1 == "/inventory":
            inventory_list()
            question()
        else:
            question()
        return x_prompt_1
    question()
 
def dresser_prompt():
    global Inventory
    print("You head towards the dresser and open each drawer.\nAt the bottom, you find a tattered, old piece of paper.\nIt reads simply:\n10 steps down,\nContinue until you come across a door with a clock on it\nTurn right and walk 5 steps forward\nThen open the door with the mirror.")
    print("Considering the circumstances, You are very hesitant to be doing anything like this.\nHowever, you have a choice between\nFollowing the instructions(1)\nInvestigating yourself(2)")
    def response_func():
        response = input()
        if response == "1":
            zone_name_3_tania()
        elif response == "2":
            starting_room_repeat()
        else:
            print("Misinput.  Please type something that was requested.")
            response_func()
    response_func()
       
 
def dresser_prompt_repeat():
    print("You have investigated this already.")
 
def end_door():
    print("You see a door with 3 locks on it.  One has a key in it already, but the rest are empty.  What could this mean?")
    response_func_starting_room()
def end_door_repeat():
    print("The strange door with 3 locks.")
    response_func_starting_room()
def door_to_hallway_1():
    print("Despite the poor lighting, you notice that this door has no lock on it, only a handle.")
 
 
def hallway_1():
    print("You enter a dim, foreboding hallway.  Like the room before, there is barely any light except what can get through the 3 boarded up windows in front of you.\nYou look right and see nothing but blackness until after where the little light can get to.")
    print("Do you want to continue down here? (Y or N): ")
    response = input()
    if response == "Y":
        zone_2_gabrielle()
    elif response == "N":
        print("You decided it's too dangerous\nWhat would you like to do next? Look behind you (1) or return to starting room(2)")
        response3 = input()
        if response3 == "1":
            hallway_left()
        elif response3 == "2":
            starting_room_repeat()
 
def hallway_1_repeat():
    print("The first hallway outside the starting room.")
    print("Do you want to go left (1) or right (2)?")
    response = input()
    if response == "1":
        hallway_left_repeat()
    elif response == "2":
        zone_2_gabrielle()
 
def hallway_left_repeat():
    print("You are back in the hallway where you found the flashlight.\nWhat would you like to do? (1) Go down the staircase or move into the starting room (2)")
    response = input()
    if response == "1":
        room_beneath_staircase()
    elif response == "2":
        starting_room_repeat()
 
def hallway_left():
    global Inventory
    print("You decide to walk left cautiously.\nSoon after walking, you hear a click, see a bright light and footsteps heading downwards, the sound slowly fading away.\nWith no other options, you are forced to approach the glowing item.\nTo your surprise, it is a flashlight, and, investigating further, you see 4 numbers on a very small piece of paper taped to the object.\n4561.\nHaving no use for this, you immediately think of what to do next.")
    add_item("flashlight")
    add_item("note code - 4561")
    print("Shining the light forward, you see a staircase leading down into a lightless room.  Do you choose to go down (1) or head back (2)")
    def response_func():
        response = input()
        if response == "1":
            room_beneath_staircase()
        elif response == "2":
            hallway_1_repeat()
        elif response == "/inventory":
            inventory_list()
            response_func()
        elif response == "q":
            quit()
        else:
            print("Do you choose to go down (1) or head back (2)")
            response_func()
    response_func()
 
def starting_room():
    global Inventory
    print("You feel terrified.  Someone placed you here and placed that knife next to you.\nYou're desperate attempts at remembering anything before this is futile.  You know something is around here.  You're unsure of what it is and you feel as if you're being watched.\nYou need to investigate.  You look around and can see a dresser (1), two doors(2, 3), a light (4) and the bed you woke up on (5).\nWhat do you want to walk up to?")
    print("Or... try your luck with 'Gamble'.")
    global response_func_starting_room, keys_collected
    def response_func_starting_room ():
        global keys_collected
        response = input()
        if response == "1":
            dresser_prompt()
        elif response == "2":
            end_door()
        elif response == "12345":
            keys_to_zone_4()
        elif response == "Gamble":
            rand_box()
        elif response == "3":
            door_to_hallway_1()
            print("Do you want to go through?  It seems like the only way forward. (Y) or (N)")
            response2 = input()
            if response2 == "Y":
                hallway_1()
            else:
                response_func_starting_room()
        elif response == "4":
            print("The only light source in the room - a small lightbulb.  It keeps flickering.")
            response_func_starting_room()
        elif response == "5":
            print("The bed you woke up on.  It is filthy and isolated in the corner of the room.\nYou tear the sheets apart and find nothing.\nLooking under the bed, you find a key.")
            add_item("KeyFromStartingRoom")
            keys_collected += 1
            keys_to_zone_4()
            response_func_starting_room()
        elif response == "/inventory":
            inventory_list()
            response_func_starting_room()
        elif response == "6" and not room_beneath_staircase():
            print("You cannot perform this action yet.")
            response_func_starting_room()
        elif response == "6" and room_beneath_staircase():
            room_beneath_staircase_repeat()
        elif response == "q":
            quit()
        else:
            print("Incorrect input.  Please input what was requested")
            response_func_starting_room()
    response_func_starting_room()
 
x = random.randint(1,10)
 
def try_again():
    print("Do you want to try again? (Y) or (N)")
    response = input()
    if response == "Y":
        response_func_beginning()
    elif response == "N":
        starting_room_repeat()
 
def rand_box():
    print("The way this works is that you input your number between 1 and 10.  It is compared to the randomly generated number, and if equal, you are awarded a key, otherwise you ")
    print("To leave this game, enter q.")
    global response_func_beginning
    def response_func_beginning():
        global player_health, keys_collected
        response = int(input("What is your number: "))
        if x == response:
            print("Hmphh...\nYou've earned a key")
            add_item("key")
            keys_collected += 1
            keys_to_zone_4()
            try_again()
        elif x != response:
            print("Ouch.  What a shame.  Your gamble didn't pay off.  You might have to put some thought into finishing the game rather than rely on chance.")
            player_health -= 1
            if player_health == 0:
                quit()
            elif player_health == 1:
                print("Careful now...")
                try_again()
            else:
                print(f"You have {player_health} life/lives remaining")
                try_again()
        elif x == "q":
            starting_room_repeat()
    response_func_beginning()
 
def options_hallway_left():
    global Inventory
    print("The dark hallway.")
    print("Proceed forward (1) or return back (2)?")
    def response_func():
        response = input()
        if response == "1":
            zone_2_gabrielle()
        elif response == "2":
            hallway_1_repeat()
        elif response == "/inventory":
            inventory_list()
        elif response == "q":
            quit()
    response_func()
 
def starting_room_repeat():
    print("The room you woke up in.")
    print("You are back in the starting room.\nWhat would you like to investigate?\n1 - dresser\n 2 - locked door\n 3 - hallway\n5 - bed\n6 - return to the room beneath the staircase")
    print("Or.. type 'Gamble' to try your luck.")
    response_func_starting_room()
 
# def game_over_win():
#     if key_zone_5():
#         print("You've escaped!")
#     else:
#         print("You have not finished yet.")
       
 
# def game_over_defeat():
#     x = input("You've lost your lives\nDo you want to restart (1) or quit? (q): ").lower()
#     if x == "1":
#         intro_text_2()
#     elif x == "q":
#         quit()
#     else:
#         print("Misinput detected.  Quitting game")
#         quit()
 
 
def room_beneath_staircase():
    global Inventory
    print("You slowly walk down the staircase, using your flashlight to ensure you don't miss your step.\nSustaining an injury would drastically reduce the likelihood of surviving whatever this is.  There is dead silence, except of the sound of your breath and your steps.\nYou arrive at bottom and pan your flashlight from left to right.\nIts an empty concrete basement. \nYou noticed 3 doors, one on your left (1), one on your right (2) and the last in front (3).\nWhich would you like to go through?")
    def response_func():
        response = input()
        if response == "1":
            zone_name_3_tania()
            Instruction_description()
            instruction_start()
            step_instruction_description()
            step_instruction_1()
            instruction_1()
            instruction_2()
            instruction_3()
        elif response == "2":
            print("This door is exactly the same as the door with the locks on it in the starting room.  This could prove convenient.")
            response_func()
        elif response == "3":
            zone_5_zain()
        elif response == "/inventory":
            inventory_list()
            response_func()
        elif response == "q":
            quit()
        elif response == "help":
            print("/inventory for your current posessions\nq to quit.")
            response_func()
    response_func()
       
def room_beneath_staircase_repeat():
    print("You are in the room at the bottom of the staircase.")
    print("1 - left door\n2 - right door")
    response_func_starting_room()
 
 
def zone_5_zain():
    global Inventory, player_health
    if x_prompt_1 == "2":
        print("You were threatened by a monster, but after viewing that you're defenceless, he leaves you be.")
    elif x_prompt_1 == "1":
        print("You lose a life due to the monster detecting the knife on you.  You were seen as a threat.")
        player_health -= 1
        print(f"You have {player_health} life/lives remaining.")
    print("You are now in a hallway.  It is decrepit.  Using your flashlight, you are able to spot one door.  Press 1 to enter it.")
    def response_func():
        response = input()
        if response == "/inventory":
            inventory_list()
            response_func()
        elif response == "1":
            zone_5_room1()
        elif response == "q":
            quit()
    response_func()
    # if "knife" not in Inventory:
    #     print("Not seeing a threat, the monster ignores you.")
def zone_5_beginning_repeat():
    print("The room with the safe.")
    response_zone_5_room1()
   
def zone_5_room1():
    global Inventory
    print("The room is cluttered.  You spot a safe (1) at the corner of the room and a new door (2) leading to a room further down.")
    response_zone_5_room1()
 
def response_zone_5_room1():
    response = input()
    if response == "1":
        safe_puzzle()
    if response == "/inventory":
        inventory_list()
    elif response == "2":
        zone_5_room2()
    response_zone_5_room1()
 
def safe_puzzle():
    global safe_open
    print("You walk towards the safe.  It can be opened with four numbers.")
    safe_number = input()
    if safe_number == "4561":
        print("The safe opens.  It reveals that there is a riddle nearby you must find.")
        print("You back out of this function")
        safe_open = True
        response_zone_5_room1()
    else:
        print("Incorrect.")
        print("Enter 1 to attempt again.")
        response_zone_5_room1()
 
def zone_5_room2_repeat():
    print("The second room with the safe.")
    zone_5_room1()
 
def final_puzzle():
    global keys_collected
    print("I am something people love or hate. I change people's appearances and thoughts. If a person takes care of them self I will go up even higher. To some people, I will fool them. To others, I am a mystery. Some people might want to try and hide me but I will show. No matter how hard people try I will never go down. What am I?")
    response2 = input().capitalize()
    if response2 == "Age":
        add_item("Keyfromzone4")
        keys_collected += 1
        keys_to_zone_4()
    else:
        print("The room starts to collapse.")
        print("You are too deep to return from where you came from and are crushed.")
        quit()
 
def zone_5_room2():
    global final_puzzle, zone_5_room2_repeat, safe_open
    print("You enter an empty room.  The only object in here is a box.  Walking up to it, you see a note that warns you to not trigger this until you are absolutely sure.  Do you continue? (Y) or (N)")
    response = input()
    if response == "Y" and safe_open:
        final_puzzle()
    elif response == "Y" and safe_open == False:
        print("You need to complete an objective in the last room before starting this puzzle.  You walk back there.")
        zone_5_room1()
    elif response == "N":
        print("You remain in the current room.")
        zone_5_room1()
    else:
        print("Out of fear, you return to the last room.  It may have been the wiser choice.")
        zone_5_room2_repeat()
 
# def keys():
#     if final_puzzle():
#         add_item("Zone5Key")
       
 
# /* Gabrielle coding zone 2/
 
def zone_2_gabrielle():
    def zone_2_room_1():
        global player_health, visited_room_1, visited_room_2, Inventory, keys_collected
        visited_room_1 = True
        print("\n")
        print("The room is wet and dark. You take caution as there is loose bricks. ")
        print("Something glistens in the corner and it catches your eye ")
        print("Will you check it out? ")
   
        print("\noptions")
        print("Yes (1)")
        print("No (2)")
   
        keychoices = input()
        if keychoices == "1":
            print("Hey! You found another key and place it in your inventory")
            add_item("Keyfromzone2")
            keys_collected += 1
            keys_to_zone_4()
        elif keychoices == "2":
        # if visited_room_2 == False:
            print("You decide not to look and choose to go to the other room, hoping to have more luck")
            zone_2_room_2()
        else:
            zone_2_room_1()
    def zone_2_room_2():
        global player_health, visited_room_1, visited_room_2, Inventory
        visited_room_2 = True
        print("\n")
        print("You step into the room on your left ")
        print("As you walk further into the room, the floorboards creak underneath you ")
        print("Will you continue to explore this room? ")
        print("\n")
   
   
        print("\noptions")
        print("1. Yes")
        print("2. No")
   
        badchoice = input(" ")
        if badchoice == "1":
            print("Oh no! The floorboards give way and you fall through.  You die a slow, painful death.")
            quit()
        if badchoice == "2" and visited_room_1 == False:
            print("You decide to leave the room, and explore the other room, hoping to have better luck there")
            zone_2_room_1()
        elif badchoice == "2":
            print("You fall into a trap.  You have nothing in your inventory to escape.  You die slowly.")
            quit()
        else:
            return
    def zone_2(fname):
        global player_health, visited_room_1, visited_room_2
    #zone2desc
        print("\n")
        print("You reach the start of what appears to be a hallway ")
        print("The hallway is very dark and creepy, you are unable to see what lies ahead, which sends chills down your spine ")
        print("You decide to check your inventory for a flashlight ")
        print("\n")
    #zone2desc
   
        print("\noption")
        print("Open your inventory.")
   
        choice = input("Will you open your inventory? (Y) or (N)")
        if choice == "Y":
            inventory_list()
        else:
            print("You must open your inventory")
   
        flashlight = input("Do you have the flashlight? (Y) or (N)")
        if flashlight == "Y":
            print("You grab the flashlight and turn it on, ready to proceed down the hallway")
        elif flashlight == "N":
            print("You do not have the flashlight. You become lost and unable to find your way back...")
            sleep(1)
            quit()
   
    #zone2desc
        print("\n")
        print("With your flashlight in hand, you set off down the hallway, looking for any doors or exits that may be of use ")
        print("The hallway seems to stretch on forever and ever ")
        print("After what feels like miles of walking, you finally reach the end of the hallway, and spot that there are two rooms: one to your left and one to your right ")
        print("\n")
    #zone2desc
   
        print("\noptions")
        print("1. Explore the room to your right")
        print("2. Explore the room to your left")
   
        choices = input("Which way will you go? ")
        if choices == "1":
            print("You enter the room to your right")
            zone_2_room_1()
        elif choices == "2":
            print("You enter the room to your left")
            zone_2_room_2()
        else:
            print("You're indecisiveness leads you to being killed from behind")
            quit()
       
    visited_room_1 = False
    visited_room_2 = False      
    zone_2("")
   
# /* Tania coding zone 3/
def zone_name_3_tania():
        #zone 3 description start
    print("Welcome to zone 3")
    sleep (0.1)
    print("You have made it this far. Well Done!!!")
    sleep (0.1)
    print("This new zone might be making you feel nervous but dont worry your nearly there to letting yourself out of this nightmare.")
    sleep (0.1)
    print("Keep a look out for the key, read your instructions carefully.")
    sleep (0.1)
    print("Come on you got this!!")
    sleep (0.8)
    # zone 3 description end
    Instruction_description()
#instruction description start
def Instruction_description():
    print ("Here are your instructions, follow them carefully and good luck")
#instruction description end
    instruction_start()
#instructions start      
def instruction_start():
        print("These are your instructions, refer back to these steps to complete each step")
        print("Follow instructions")
        print("1. Go down 10 steps")
        print("2. Turn left until you notice a door with a clock on it")
        print("3. Turn right and walk and walk 5 steps forward")
        print("4. Open the door with the mirror")
#instruction end
        step_instruction_description()
#step instruction description
def step_instruction_description():
    print ("As your taking each step your feeling more and more anxious, you can feel your heart racing")    
#step instruction description end
    step_instruction_1()
#steps instructions start
def step_instruction_1():
    print ("step 1")
    sleep (0.2)
    print ("step 2")
    sleep (0.2)
    print ("step 3")
    sleep (0.2)
    print ("step 4")
    sleep (0.2)
    print ("step 5")
    sleep (0.2)
    print ("step 6")
    sleep (0.2)
    print ("step 7")
    sleep (0.2)
    print ("step 8")
    sleep (0.2)
    print ("step 9")
    sleep (0.2)
    print ("step 10")
    instruction_1()
#step instruction end
def instruction_1():
    def tania_response():
        instructions = int(input("you have two options 1 to attempt to open the door or 2 to step back"))
        if instructions == 1:
            print(f"Congratulations, you found the red clock! Continue with the instructions")
            instruction_2()
        elif instructions == 2:
            print (f"You have not found the door you have lost your life")
            quit()
        else:
            print("You made an incorrect choice and have lost your life")
            quit()
    tania_response()
def instruction_2():
    global player_health
    def tania_response():
        instructions = input ("Which direction do you wish to go now? forward, left or right").lower()
        if instructions == "forward":
            print("Congratulations, you have reached the door with the mirror")
            instruction_3()
            return "door with mirror"
        elif instructions == "left":
            print("Incorrect choice you are being returned to the clock room")
            player_health -= 1
            print(f"You have {player_health} life/lives remaining.")
            instruction_1()
        elif instructions == "right":
            print("Incorrect choice you are being returned to the clock room")
            player_health -= 1
            print(f"You have {player_health} life/lives remaining.")
            instruction_1()
        else:
            player_health = player_health - 1
            if player_health < 1:
                print("game over")
                exit()
            print("Incorrect choice, you have lost a life")
    tania_response()
 # lives = 3
# # initialise the number of lives to be 3
def instruction_3():
    def tania_response2():
        global player_health, keys_collected
        print("You have a 50/50 chance of finding a key or losing a life.  Type in smallest wardrobe or big wardrobe to attempt this.")
        response = input()
        if response == "smallest wardrobe":
            print("You've found the key.\nFinding the key places you back into the starting room.")
            add_item("Keyfromzone3")
            keys_collected += 1
            keys_to_zone_4()
            # print("Debug")
        elif response == "big wardrobe":
            player_health -= 1
            if player_health == 0:
                print("You are dead")
                quit()
            elif player_health < 3:
                print(f"You lost a life.\n{player_health} life/lives remaining")
                print("You are back at the start of the encounter")
                instruction_1()
    tania_response2()
           
            # /*sarah coding zone 4/
def sarah_choices():
    global keys_collected, key_picked_up
    print("\nYou wisely decide to retreat to the safety of the hallway.")
    print("You manage to escape the ghost and catch your breath.")
    print("Your current health:", player_health)
 
 
    print("\nAs you quickly scan the blurrily lit hallway outside the end room, your eyes catch sight of a small bottle resting on a nearby table. Intrigued, you cautiously approach and pick it up.")
    print("You find a bottle labeled 'Ghost Repellent Spray'. It might be useful against the ghost!")
 
    choice = input("Do you want to pick up the Ghost Repellent Spray? (Yes): ")
    if choice.lower() == 'yes':
        print("\nYou pick up the Ghost Repellent Spray.")
   
        print("With a mixture of hope and anxiety, you re-enter the room. The ghost launches another attack.")
 
        choice = input("Do you want to use the ghost repellent spray against the ghost? (Yes): ")
    else:
        print("Your hesitancy leads to the ghost killing you.")
        quit()
    if choice.lower() == 'yes':
        print("\nReacting quickly, you spray it with the repellent, causing it to disappear. Relief washes over you.")
        print("You walk towards the box and find the final key.")
        print("Congratulations! You collected all the keys and escaped!")
        quit()
    else:
        print("You misinputted leading to a mistake being made in this deadly scenario.  You died.")
        quit()            
def zone4_sarah():
    global keys_to_zone_4
    def zone_4():
        global player_health, keys_collected, key_picked_up
        print("\nAs you push the heavy and creaking door, a shiver runs down your spine, sending a chill through your body. With cautious steps, you enter the room, your senses on high alert, every nerve tingling with anticipation.")
        print("Suddenly, a flickering light stutters to life and you notice strange symbols decorate the walls. In the middle of the room, a box sits ominously. You stand on the precipice of discovery, the weight of the room's history pressing down upon you, urging you to uncover its mysteries... or escape before it's too late.")
        print("As you cautiously approach the enigmatic box in the middle of the room, with a hesitant hand, you reach out towards the box. Before you can react, a cold, spectral presence appears before you. The ghost lets out a loud scream, freezing you in place with fear. Time seems to stand still as you weigh your options.")
        print("With adrenaline coursing through your veins, you must make a decision that will determine your fate in this haunted house. Do you stand and face the ghost, or do you turn and run, desperate to avoid its grasp and live to see another day?")
        print("\n")
   
        print("\nChoices:")
        print("1. Attempt to fight back")
        print("2. Escape and retreat to the safety of the hallway outside the end room")
   
        choice = input("Enter your choice (1, 2): ")
   
        if choice == '1':
            print("\nYou decide to fight the ghost!")
            print("The ghost is too powerful and overwhelms you.You lost a life!")
            player_health -= 1
            if player_health == 0:
                print("Game over.")
                quit()
            else:
                print("Your current health:", player_health)
                print("You are forced to retreat into the hallway")
                sarah_choices()
        elif choice == '2':
            sarah_choices()
    zone_4()
 
 
 
 
menu_screen()
 