class Weapon:
        def __init__(self, name, weapon_type, level=0):
            self.__name = name
            self.__type = weapon_type
            self.__level = level

        def upgrade(self):
            self.level += 0

        def display(self):
            print(self.__name + ' ' + self.__type + ' ' + str(self.__level))

def run():
    the_catch = Weapon('The Catch', 'Polearm')
    cool_steel = Weapon('Cool Steel', 'Sword')
    the_catch.display()
    cool_steel.display()