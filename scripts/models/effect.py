from animations.factories import AnimationFactory
from models.zone import Zone

class Effect():
    def __init__(self, name=None, arguments={}):
        self.id = id
        self.name = name
        self.arguments = arguments

    def stage(self, zone=Zone):
        self.animation = AnimationFactory().build(self.name, { "range": zone.range(), **self.arguments })

    def render(self):
        if self.animation:
            self.animation.render()
