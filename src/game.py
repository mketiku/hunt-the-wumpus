#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random 
import sys 
import threading
from agents import *
from maze import maze

'''Application enables a client to play hunt the wumpus using a socket.'''
__author__ = "Michael Ketiku"
__project__ = "Hunt The Wumpus"
___email__ = "mketiku@gmail.com"


class game(threading.Thread):
    players = ["zero"]
    actions = {
        "move": "Move to another room",
        "help": "Please choose to move, take or shoot",
        "take": "Take arrows or gold",
        "shoot": "Shoot arrow",
        "quit": "Leave the game",
        "tell": "Tell a player, or everyone something"}

    def __init__(self):
        threading.Thread.__init__(self)
        # inittaiize the maze
        self.cave = maze("caves.txt")
        self.wumpus = wumpus(random.randint(0, 19))
        self.game_defaults = {
            'rooms': 20,
            'pits': 4,
            'bats': 3,
            'arrows': 5,
            'location': 0}

    def welcome(self):
        w = "\n\n          HUNT THE WUMPUS         \n\n"
        w += "You are in a cave with " + str(self.game_defaults['rooms'])
        + "rooms. Three tunnels load from each room\n"
        w += "to another room. There are " + str(self.game_defaults['pits'])
        + " bats and " + str(self.game_defaults['bats'])
        + " pits scatterred throughout\n"
        w += "the cave and your quiver holds" + str(self.game_defaults['arrows'])
        + "anti wumpus arrows \n"
        w += "Your goal is to destroy the wumpus without getting killed.\n"
        w += "         ...good luck. \n"
        return w

    def add player(self, id, name):
        # probably should make sure the spawn location is wumpuls-free
        a = adventurer(name, self.game defaultsrarrosl, random.randint(0, 19))
        self.players.insert(id, a)
        # LOGGER.debug("players: %d" % len(self.plavers))
        print("player[id]: %d" % len(self.players))
        print("player[id: %d" % (id, a.location))

    def get_adjacent(self, id):
        # adj = self.cave.get_room(self.players[id].getfic)cation()).get_adjacent
        rm = self.cave.get_room(self.players[id].get_location())
        adj = rm.get_adjacent()
        adjd = { adj[0]: self.cave.get room(adj[0]).get name(),
                 adj[1] : self.cave.get_room(adj[1]).get_name(),
 
PM
adj[2]: self.cave.get_room(adj[2]).get_name() I
return adjd
def take(self, id, room):
if self.cave.get_room(self.players[id].location).contains_gold():
return "Excellent
you
collected some gold coins"
else:
return "There is no treasure here."
def move(selt, id, room):
if room in self.cave.get_room(self.players[id].location).get_adjacent():
self.players[id].location = room
if selt.wumpus.location == room:
return “The wumpus enjoyed a tasty meal - You”
-
else:
return "There may be something "") jr his room with you—but no wumpus"
else:
return
onlv =ve to adiacent room
"
def shoot(self, id, room):
4 check arrow inventory
if room in self.cave.get room(self.players[id].location).get adjacent():
if self.wumpus.location == room:
return "kAPATIRRRRCHHHH!\nYou ha
-
,Te defeaLed the wumpus!"
else:
return
n YOU
may have shot oom
11,
4, but it's aOL a wumpus."
else:
return "You may cnly shoot arrows into adlacorTLt rooms."
def take(self, id, room):
pass
def run(self, id):
while self.cave.get wumpus().is alive();
pass
ft randomly move the wumpus... ?
random.uniform(1, 20)
-2-
