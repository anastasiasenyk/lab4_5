"""class Room, Item"""
from game2 import Friend, Enemy, Character


class Room:
    """rooms"""
    def __init__(self, name):
        """
        Args:
            name: str
        """
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
        """
        Args:
            description: str
        >>> room = Room('kitchen')
        >>> room.set_description('new new')
        >>> room.description
        'new new'
        """
        self.description = description

    def link_room(self, other_room, side):
        """
        Args:
            other_room: Room
            side: str
        >>> room1 = Room('kitchen')
        >>> room2 = Room('bath')
        >>> room1.link_room(room2, 'west')
        >>> isinstance(room1.horizon['west'], Room)
        True
        """
        self.horizon[side] = other_room

    def set_character(self, character):
        """
        Args:
            character: Enemy/Friend
        >>> character1 = Friend('name', 'description')
        >>> room1 = Room('kitchen')
        >>> room1.set_character(character1)
        >>> isinstance(room1.character, Character)
        True
        """
        self.character = character

    def set_item(self, item):
        """
        Args:
            item: Item
        >>> room1 = Room('kitchen')
        >>> item1 = Item('new')
        >>> room1.set_item(item1)
        >>> isinstance(room1.item, Item)
        True
        """
        self.item = item

    def get_details(self):
        """
        >>> room1 = Room('kitchen')
        >>> room1.get_details()
        kitchen
        --------------------
        None
        """
        other_room = ''
        for side in self.horizon.keys():
            if self.horizon[side]:
                other_room += f'\nThe {self.horizon[side].name} is {side}'
        print(
            f'{self.name}\n--------------------\n{self.description}{other_room}'
        )

    def get_item(self):
        """
        Returns: Item
        >>> room1 = Room('kitchen')
        >>> item1 = Item('new')
        >>> room1.set_item(item1)
        >>> isinstance(room1.get_item(), Item)
        True
        """
        return self.item

    def get_character(self):
        """
        Returns: Character
        >>> character1 = Friend('name', 'description')
        >>> room1 = Room('kitchen')
        >>> room1.set_character(character1)
        >>> isinstance(room1.get_character(), Character)
        True
        """
        return self.character

    def move(self, side):
        """
        Args:
            side: str
        Returns: bool|Room
        >>> room1 = Room('kitchen')
        >>> room2 = Room('bath')
        >>> room1.link_room(room2, 'west')
        >>> room2 == room1.move('west')
        True
        """
        if self.horizon[side] is None:
            return False
        return self.horizon[side]


class Item:
    """name description of item"""
    def __init__(self, name):
        """
        Args:
            name: str
        >>> item = Item('new')
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Args:
            description: str
        >>> item = Item('new')
        >>> item.set_description('fail')
        >>> item.description
        'fail'
        """
        self.description = description

    def get_name(self):
        """
        Returns: str
        >>> item = Item('new')
        >>> item.get_name()
        'new'
        """
        return self.name

    def describe(self):
        """
        as __str__
        >>> item = Item('new')
        >>> item.describe()
        The [new] is here - None
        """
        print(f'The [{self.name}] is here - {self.description}')
