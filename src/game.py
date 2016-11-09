#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''Application enables a client to play hunt the wumpus using a socket.'''
__author__ = "Michael Ketiku"
__project__ = "Hunt The Wumpus"
___email__ = "mketiku@gmail.com"


import random 
import sys 
import threading
from agents import *
from maze import maze

class game()