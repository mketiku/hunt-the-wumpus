class adventure(object):
    '''
    An adventurer who collects gold and kills wumpuses'''

    def __init__(self, name, arrows, room):
        self.alive = True
        self.arrows = arrows
        self.location = room
        self.name = name
        self.gold = 0

    def get_location(self):
        return self.location

    def set_location(self, room):
        self.location = room

    def is_alive(self):
        return self.alive

    def can_shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            return True
        else:
            return False

    def shoot(self):
        self.arrows -= 1

    def print_inventory(self):
        print("arrows: %d\ngold: %d\n" % (self.arrows, self.gold))


class bat(object):
    '''
    A bat which carries unware adventurers to new locations in the cave
    '''

    def __init__(self, id, room):
        self.id = id
        self.location = room


class wumpus(object):
    '''
    A wumpus who sleeps most of the time, smells funny and likes to eat
    careless adventurers
    '''

    def __init__(self, room):
        self.location = room
        self.alive = True
        self.sleeping = True

    def get_location(self):
        return self.location

    def set_location(self, room):
        self.location = room

    def is_alive(self):
        return self.alive

    def shoot(self):
        self.alive = False

    def wake(self):
        self.sleeping = False