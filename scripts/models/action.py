from models.repositories import ActionRepository
from models.effect import Effect

class Action():
    def __init__(self, id=None, name="", effects=[]):
        self.id = id
        self.name = name
        self.effects = [Effect(**effect) for effect in effects]

    @classmethod
    def find_by(cls, key, value):
        try:
            return cls(**cls.find_all(key, value)[0])
        except IndexError:
            None

    @classmethod
    def find_all(cls, key, value):
        try:
            return [action for action in ActionRepository().actions if action.get(key) == value]
        except:
            [None]
        