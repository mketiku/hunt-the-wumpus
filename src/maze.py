# import random
from room import room
from agents import adventurer, wumpus


class maze(object):
    '''
    A cave of rooms which contains the wumpus
    Adventurer begins at the start location
    '''

    def __init__(self, cavefile):
        self.room = []
        self.wumpus = wumpus(10)  # TODO make random
        self.player = adventurer('Adventurer', self.default_arrows,
                                 self.default_location)
        self.description = "The Wumpus' Cave"
        self.cavefile = cavefile
        self.load_cave()

    def load_cave(self):
        of = open(self.cavefile, 'r')
        for l in of.readlines():
            num, t1, t2, t3, name = l.strip().split(',')
            print("loading rooms[%s]: %s" % (num, name))
            self.rooms.append(room(name, int(t1), int(t2), int(t3), int(num)))
        of.close()

        self.rooms[self.default_location].mark_visited()

    def move(self, tunnel):
        '''
        Moves the player from the current cabe along the specified tunnel.
        The new location must be marked as visited and the appropriate
        action taken if the new location is not empty.
        '''
        self.rooms[tunnel].mark_visited()
        self.get_adventurer().set_location(tunnel)
        return ("ok")

    def shoot(self, tunnel):
        if self.get_adventurer().can_shoot():
            if self.wumpus.get_location() == tunnel:
                print("AAAARGH!")
                self.wumpus.shoot()
            else:
                print("woosh...")
                self.get_adventurer().shoot()
        else:
            print("You have no arrows to shoot")

    def describe_room(self, rooms):
        ''' Displays the current cave name and the names of the adjacent caves
        if those caves have been visited'''
        message = "You are currently in " + self.rooms[room].get_name()
        adjacent_rooms = self.rooms[room].get_adjacent()
        for r in adjacent_rooms:
            if self.rooms[r].is_visited():
                message += "\n     (" + str(r) + ")" + self.rooms[r].get_name()
            else:
                message += "\n     (" + str(r) + ") unknown"
        return message

    def get_room(self):
        return self.rooms[room]

    def get_adventurer(self):
        return self.player

    def get_wumpus(self):
        return self.wumpus
