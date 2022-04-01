"""class Character -> Enemy, Friend"""


class Character:
    defeated = 0
    all_enemies = {}

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.phrase = None

    def set_conversation(self, phrase):
        self.phrase = phrase

    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        print(f'[{self.name} says]: {self.phrase}')

    def get_defeated(self):
        Character.defeated += 1
        return Character.defeated


class Enemy(Character):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.status = 'enemy'
        Character.all_enemies[self.name.lower()] = self

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, fight_with):
        if fight_with == self.weakness:
            return True
        else:
            return False


class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.status = 'friend'
        self.help = False

    def set_power(self, enemy):
        if not self.help:
            if enemy.lower() in Character.all_enemies.keys():
                self.help = True
                self.phrase = 'I already helped you'
                return f'Weakness - {Character.all_enemies[enemy].weakness}'
            return False
        else:
            return 'I already helped you'


