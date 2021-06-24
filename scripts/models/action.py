from models.repositories import ActionRepository

class Action():
    def __init__(self, id=None, name="", description="", sound=None, effects=[]):
        self.id = id
        self.name = name
        self.description = description
        self.sound = sound
        self.effects = effects

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
        