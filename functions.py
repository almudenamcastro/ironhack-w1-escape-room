
import re


## Game functions

def linebreak(n=1):
    """
    Print a line break
    """
    print("\n"*n)

def start_game(game_state, object_relations):
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.\nYou don't remember why you are here and what had happened before. \nYou feel some unknown danger is approaching. \nYou must SCAPE, NOW!")
    
    linebreak(1)

    play_room(game_state["current_room"], game_state, object_relations)

def play_room(room, game_state, object_relations):
    """
    Play a room. 
    First check if the room being played is the target room.
      If it is, the game will end with success. 
      Otherwise, let player either explore (list all items in this room) or examine an item found here.
    """
    
    game_state["current_room"] = room
    linebreak(1)
    print("You are now in the " + game_state["current_room"]["name"])

    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
        
    else:
        intended_action = input("What would you like to do? Type 'explore' or 'examine'? ").strip()
        if intended_action == "explore":
            explore_room(room, object_relations)
            examine_item(input("What would you like to examine? ").strip(), game_state, object_relations)

        elif intended_action == "examine":
            examine_item(input("What would you like to examine? ").strip(), game_state, object_relations)
            
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'. ")
            play_room(room, game_state, object_relations)
        linebreak()
        

def explore_room(room, object_relations):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("In the " + room["name"] + ", you find: " + ", ".join(items))

def get_next_room_of_door(door, current_room, object_relations):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name, game_state, object_relations):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if re.search(item_name, item["name"]): # the user input is contained in the item name
            output = "You examine " + item["name"] + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room, object_relations)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break
    # user enters an object htat is not in the current room

    if(output is None):
        print("The item you requested is not found in the current room.")
        play_room(current_room, game_state, object_relations)

    # user inspects a door and they have the proper key
    if next_room:
        play_room(next_room, game_state, object_relations)

    else:
        examine_item(input("What would you like to examine? ").strip(), game_state, object_relations)


# Define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

