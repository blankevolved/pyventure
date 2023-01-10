# The Steps
#
# 1. Design the story and game world - make a story and locations
#  
# 2. Create a basic structure - add game logic, I/O loop, functions for player actions, 
# skills, UI, saving/loading ect
#
# 3. Add details and interactions - functions to handle specific actions, 
# npcs, picking up items, puzzles
#
# 4. Testing/Debugging - clean up the game


# The Story
#
# We fight a dragon at the end, that will be in a seprate realm/world, 
# which will need to be unlocked,
# with key items, level cap, certain progess obtained
# 
# 
# 
#


# Notes
#
# locations are realms
# 
#

import os

def clear_screen():
    pass

class Realm(object):

    def __init__(self, name:str, areas:dict={}):
        self.name   = name
        self.areas  = areas

    def add_area(self, key:str):
        self.areas[key] = {}

    def add_area_atr(self, area:str, key:str, atr):
        try:
            self.areas[area][key] = atr
        except KeyError:
            print(f'Area "{area}" dosent exist, creating new area called "{area}".')
            self.add_area(area)

class Player(object):
    def __init__(self, name:str):
        self.name = name
        self.stats = {}
        for r in REALMS:
            self.realms_list = {}
            self.realms_list[r] = False
    
    def get_stats(self):
        return 'Stats:'

    def event_loop(self, input_object):
        if input_object == 'stats':
            print(self.get_stats())

        if input_object == 'travel':
            print(self.realms_list)


REALMS = {
    'overworld':Realm('Overworld')
}

OVERWORLD = REALMS['overworld']

OVERWORLD.add_area('plains')

player = Player(None)

name = input('Input your name: ')

player.name = name
player.realms_list['overworld'] = True

def main():
    print(player.realms_list)
    inp = input('>>> ')
    player.event_loop(inp)


while True:
    main()