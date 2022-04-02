"""class Character -> Enemy, Friend"""


class Character:
    """talk defeated"""
    defeated = 0
    all_enemies = {}

    def __init__(self, name, description):
        """
        Args:
            name: str
            description: str
        >>> isinstance(Character('',''), Character)
        True
        """
        self.name = name
        self.description = description
        self.phrase = None

    def set_conversation(self, phrase):
        """
        Args:
            phrase: str
        >>> person1 = Character('Tom', 'from TomAnd Jerry')
        >>> person1.set_conversation('black cat crossed road')
        >>> person1.phrase
        'black cat crossed road'
        """
        self.phrase = phrase

    def describe(self):
        """
        description
        >>> person1 = Character('Tom', 'from TomAnd Jerry')
        >>> person1.describe()
        Tom is here!
        from TomAnd Jerry
        """
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        """
        talk phrase
        >>> person1 = Character('Tom', 'from TomAnd Jerry')
        >>> person1.set_conversation('black cat crossed road')
        >>> person1.talk()
        [Tom says]: black cat crossed road
        """
        print(f'[{self.name} says]: {self.phrase}')

    def get_defeated(self):
        """
        Returns: int
        >>> person1 = Character('Tom', 'from TomAnd Jerry')
        >>> person1.get_defeated()
        1
        """
        Character.defeated += 1
        return Character.defeated


class Enemy(Character):
    """Enemy -> Character"""

    def __init__(self, name, description):
        """
        Args:
            name: str
            description: str
        >>> enemy1 = Enemy('jerry', 'tomAndjerry')
        >>> isinstance(enemy1, Character)
        True
        """
        super().__init__(name, description)
        self.weakness = None
        self.status = 'enemy'
        Character.all_enemies[self.name.lower()] = self

    def set_weakness(self, weakness):
        """
        Args:
            weakness: str
        >>> enemy1 = Enemy('jerry', 'tomAndjerry')
        >>> enemy1.set_weakness('you')
        >>> enemy1.weakness
        'you'
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Args:
            fight_with: str
        >>> enemy1 = Enemy('jerry', 'tomAndjerry')
        >>> enemy1.set_weakness('you')
        >>> enemy1.fight('you')
        True
        """
        if fight_with == self.weakness:
            return True
        else:
            return False


class Friend(Character):
    """Friend -> Character"""

    def __init__(self, name, description):
        """
        Args:
            name: str
            description: str
        >>> isinstance(Friend('jerry', 'tomAndjerry'), Character)
        True
        """
        super().__init__(name, description)
        self.status = 'friend'
        self.help = False

    def set_power(self, enemy):
        """
        Args:
            enemy: str
        Returns: str|bool
        >>> friend1 = Friend('jerry', 'tomAndjerry')
        >>> enemy1 = Enemy('Tom', 'tomAndjerry')
        >>> enemy1.set_weakness('you')
        >>> friend1.set_power('Tom')
        'Weakness - you'
        """
        enemy = enemy.lower()
        if not self.help:
            if enemy in Character.all_enemies.keys():
                self.help = True
                self.phrase = 'I already helped you'
                return f'Weakness - {Character.all_enemies[enemy].weakness}'
            return False
        else:
            return 'I already helped you'
