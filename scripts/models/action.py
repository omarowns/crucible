from repositories import ActionRepository
from effect import Effect

class Action():
    def __new__(cls):
        cls.repository = ActionRepository()

    def __init__(self, id=None, name="", effects=[]):
        self.id = id
        self.name = name
        self.effects = [Effect(**effect) for effect in effects]

    @classmethod
    def find_by(cls, key, value):
        cls(**[action for action in cls.repository.actions if action.get(key) == value][0])
        