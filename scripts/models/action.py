from models.repositories import ActionRepository

class Action():
    def __init__(self, id=None, name="", description="", loop=None, sound=None, effects=[]):
        self.id = id
        self.name = name
        self.description = description
        self.loop = loop
        self.sound = sound
        self.effects = effects

    def is_loopable(self) -> bool:
        return self.loop != None

    def loop_iterations(self) -> int:
        return self.loop

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
        