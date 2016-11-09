#!/usr/bin/env python3


class room(object):
    '''A single room in the wumpus cave
    '''

    def __init__(self, name, t1, t2, t3, room):
        '''
        Constructor method
        '''
        self.name = name
        self.location = room
        self.visited = False
        self.contains_gold = False
        self.adjacent = [t1, t2, t3]

    def get_adjacent(self):
        return self.adjacent

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def contains_gold(self):
        return self.contains_gold

    def remove_gold(self):
        return self.contains_gold = False #TODO 

    # def is_visited(self):
    #     return self.visited

    # def mark_visited(self):
    #     self.visited = true
