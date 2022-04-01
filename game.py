"""class Room, Item"""


class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.horizon = {
            'south': None,
            'north': None,
            'west': None,
            'east': None
        }
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, other_room, side):
        self.horizon[side] = other_room

    def set_character(self, character):
        """
        Args:
            character: Enemy
        """
        self.character = character

    def set_item(self, item):
        """
        Args:
            item: Item
        """
        self.item = item

    def get_details(self):
        other_room = ''
        for side in self.horizon.keys():
            if self.horizon[side]:
                other_room += f'\nThe {self.horizon[side].name} is {side}'
        print(
            f'{self.name}\n--------------------\n{self.description}{other_room}'
        )

    def get_item(self):
        return self.item

    def get_character(self):
        return self.character

    def move(self, side):
        if self.horizon[side] is None:
            return False
        return self.horizon[side]


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')
