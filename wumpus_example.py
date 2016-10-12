#-----Use this for the start for any new program---------#
import sys, time , random , math, os

# set up pygame

# Global window definitions



# set up the colors as global constants
BLACK = (0,0,0)
WHITE =  (255,255,255)
YELLOW = (255,255,0)
LIGHTYELLOW = (128,128,0)
RED = (255, 0 ,0)
LIGHTRED = (128,0,0)
BLUE = (0, 0, 255)
SKYBLUE = (135,206,250)
GREEN = (0,255,0)
LIGHTGREEN = (152,251,152)
AQUAMARINE = (123,255,212)
LIGHTBROWN = (210,180,140)
LIGHTGREY = (211,211,211)
DIMGREY = (105,105,105)
VIOLET = (238,130,238)
SALMON = (250,128,114)
GOLD = (255,165,0)
CHOCLATE = (210,105,30)
BACKGROUND = CHOCLATE

WINDOWWIDTH = 1250
WINDOWHEIGHT = 750
MAZE_TOPLEFT = (50,150)   # Top left corner of the maze area
MAZE_WIDTH = 1000
MAZE_HEIGHT = 600



ROOMS_V = 5
ROOMS_H = 5


#Used if the program uses keys
#pygame.key.set_repeat(WINDOWWIDTH,WINDOWHEIGHT)


# this set the background to so it won't be black
# you can choose the color of your preference
# right now it is commented out
'''
background_rect = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
pygame.draw.rect(windowSurface,BACKGROUND,background_rect,0)
'''
# Widget class for all widgets,  its  function is mainly to hold the
# dictionary of all widget objects by name as well as the application
# specific handler function. And support isclicked to
# see if cursor is clicked over widget.
class Maze(object):
    #col = x
    #row = y
    starting_col = 2
    starting_row = 4
    def __init__(self):
    # Maze initialization method called when maze is created

        
        return  # return from Maze.__init__

    def build(self,difficulty = 'M'):
    # Maze.build function called at the Maze object level to build a maze.
        if difficulty == 'E':
            temp_rooms = int(ROOMS_V / 2)
        elif difficulty == 'M':
            temp_rooms = int(ROOMS_V)
        elif difficulty == 'H':
            temp_rooms = int(ROOMS_V * 2)
        elif difficulty == 'H+':
            temp_rooms = int(ROOMS_V * 4)

        # Fill in the rooms array with the room objects
        for h in range (0,int(temp_rooms * (float(MAZE_WIDTH)/float(MAZE_HEIGHT)))):
            Room.rooms.append([])  # this creates the second dimension
            for v in range(0,temp_rooms):
                room = Room(size=int(float(MAZE_HEIGHT)/float(temp_rooms)),row=v,col=h)
                Room.rooms[h].append(room)
                Room.unused_rooms.append(room)
        
        # generator doesn't mark the starting room because it is used for branches
        # so mark the starting room as solid white
    def reset(self):
    # Maze method to reset the room array to initial condition
        Room.unused_rooms = []  # empty the unused rooms list
        for col in range (0,ROOMS_H):
            for row in range(0,ROOMS_V):
                room = Room.rooms[col][row]
                Room.unused_rooms.append(room)
                room.room_color = BACKGROUND
                room.state = None;
                room.contents = []  # reset to no contents
                #initialize the state of the walls, True means they are up
                room.n_wall = True
                room.s_wall = True
                room.e_wall = True
                room.w_wall = True
                room.draw()

        return # return from Maze.reset
    #class to hold the rooms
class Room(object):
    
    rooms = []  # holds the doubly indexed list of room objects
    unused_rooms = [] # single indexed list of the unused rooms
    
    def __init__(self,size=20,row=0,col=0):
    #Room initialization method called when room is created.  Column and row
    # give the position in the array
        self.room_color = BACKGROUND  # chose the paint colors
        self.wall_color = BLACK
        self.size = size  # size of the room in pixels
        #print(self.size)
        self.col = col    # column coordinate
        self.row = row   # row coordinate
        self.state = None   # usage state of the room
        self.contents = [] # contents list to empty

        #initialize the state of the walls, True means they are up
        self.n_wall = False
        self.s_wall = False
        self.e_wall = False
        self.w_wall = False

        #define a rectangle for this room and save it
        left = int(float((WINDOWWIDTH-MAZE_WIDTH)/2.)
                   +int(self.col*float(size)))
        top =  int(float((WINDOWHEIGHT-MAZE_HEIGHT)/2)
                   +int(self.row*float(size)))
        #self.rect = pygame.Rect(left,top,size,size)
        
        #Player.dimensions = (size-1,size-1)
        #I use the - in order to make the redraw easier.
        #This way we only have to draw a square with the same dimensions.
        #self.draw()  # draw the room

        return  # return from Room.__init__
    def walk(self,direction='N',wall_check=True):
    #Maze method to walk out of a room
    # if walk_check is False, you can walk through walls (used for initial
    # maze setup). Returns false if we can't go that way, also returns updated
    # room object.
    
        moved = False  # establish default
        col = self.col # initial col
        row = self.row
        if ( (direction == 'N') &
             (self.row >0) ):
            if( (not self.n_wall) |  (not wall_check)):
                 row -=1
                 moved = True
        if ( (direction == 'S') &
             (self.row < (ROOMS_V-1) ) ):
            if( (not self.s_wall) |  (not wall_check)):
                 row +=1
                 moved = True
        if ( (direction == 'W') &
             (self.col >0) ):
            if( (not self.w_wall) |  (not wall_check)):
                 col -=1
                 moved = True
        if ( (direction == 'E') &
             (self.col < (ROOMS_H-1) ) ):
            if( (not self.e_wall) |  (not wall_check)):
                 col +=1
                 moved = True
#        print('dir,N,S,E,W= ',direction,self.n_wall,self.s_wall,
#              self.e_wall,self.w_wall)

        return moved,col,row  # returned with indication of success or failure

    def knock_out_walls(direction,room,old_room):
    # General purpose function to clear the walls from which we entered a room.
    # direction is the direction we were going when we entered.
    # room is current room object. old_room is the room we entered from.
 

        if direction == 'N':
            old_room.n_wall = False
            room.s_wall = False
        elif direction == 'S':
            old_room.s_wall = False
            room.n_wall = False
        elif direction == 'E':
            old_room.e_wall = False
            room.w_wall = False
        elif direction == 'W':
            old_room.w_wall = False
            room.e_wall = False
        Room.draw(old_room) # redraw both rooms
        Room.draw(room)

        return # return from knock_out_walls
    
class Player(object):  # create Player object
    
    players = [] # list to hold all the players
        
    def move_all(direction):
        for player in Player.players():
            player.move(direction)
            
    def __init__(self,direction = 'N'):

        
        self.direction = direction

        #print(Maze.starting_col)
        #print(Maze.starting_row)
        self.room = Room.rooms[Maze.starting_col][Maze.starting_row]
        
        Player.players.append(self)

        
        return # return from player.__init__

    def move(self,direction='E'):
    # move the rat in the indicated direction
        #print("Self.direction is:",direction)
        status,col,row = self.room.walk(direction)
        #print("Self.status is:",status)
        #See room.walk()
            
        if status: # move was legal
            self.col = col
            self.row = row
            self.room = Room.rooms[col][row] # get new room he is in
            #print("Col, Row is:",col,row)
            #Do all hazard related computations
            Hazard.evaluate(self)

            return status   # return whether move occurred or not\
        else:
            print("Your body slams against a wall")
    def change_room(self,room):#Quck utility to change rooms
        self.room = room
        

        
    # see if there is cheese in room, if so, pick up cheese, change room color
    # to background and return true
        #for hazard in 

class Hazard(object):
    hazards = []
    
    def evaluate(player):
        for hazard in Hazard.hazards:
            delta_x =  abs(player.row - hazard.cords[0])#See notebook
            delta_y =  abs(player.col - hazard.cords[1])#See notebook
            distance =  math.sqrt(delta_x**2 + delta_y**2)#Calcing distance from one room to another, see notebook
            #print(distance)
            if distance < 1.5:
                print(hazard.message_N) #Printing the message unique to that hazard if the player is within 1 square of it.
                if hazard.room == player.room: #if we are in the same room as the hazard...
                    #print("Enter room with bats")
                    hazard.handler(player) #Activite the hazard 
                
    def __init__(self,handler,cords,near_message,far_message):
        self.handler = handler
        #self.name = name
        
        self.cords = cords

        self.message_N = near_message
        self.message_F = far_message
        self.room = Room.rooms[self.cords[0]][self.cords[1]] 
        Hazard.hazards.append(self)
    



def Bats(player):
    print("As you fumble around in the dark you feel a force of some kind...")
    print("Bats! They have picked you up and are draggin you to and fro!")
    print("You have completley lost your bearings!")
    random_col = random.randrange(0,5) #The bats take the playe to a random room.
    random_row = random.randrange(0,5)
    #print("Random operations in bat handler are",random_col,random_row)
    player.change_room(Room.rooms[random_col][random_row]) #assigning the player the random room
    
##--------------End of classes-------------##
##--------------Begginning of genral pourpce functions##


dungon = Maze()

dungon.build()
# Do note that the *index* is one less, #
# So starts at 0,0 and goes to 4,4 #
# But it is still a 5x5 grid #
user = Player()

bat_1 = Hazard(Bats,(random.randrange(0,5),random.randrange(0,5)),
"The pungent oder of rotten fruit and the sound of sqeaks \n is apparent", "Far smell bats")


os.system('clear')


print('#-------------------------------------------------------#')
print('You enter a dusty cave, this is where they say it lives.')
print('The village has asked a momentous task of you, you are ')
print('to slay the mighty wumpus!')
print('#-------------------------------------------------------#')
time.sleep(5)
while True:
    print("type 'help' for help, 'exit' to exit, and 'begin' to start")
    Uinput = input()
    if Uinput == 'info':
        print("Game designed by Darwin Clark, with additional concept design by Darwin Geiselbrecht")
    if Uinput == 'exit':
        sys.exit()
    if Uinput == 'begin':
        print("type move to move")
        Uinput = input()
        if Uinput == 'move':
            print("what direction? [N,S,E,W]")
            while True:
                Uinput = input()
                if Uinput == 'N' or Uinput == 'S' or Uinput == 'E' or Uinput == 'W':
                    print("You stumble to the", Uinput)
                    user.move(direction = Uinput)
                else:
                    print(" You filty human, trying to break the system, you can only enter N,S,E, or W because this was written by a master programmer")
                

'''
Room.rooms[col][row]
'''
