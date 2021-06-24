from models.zone import Zone
from models.concerns import Animatable
# import animations.basics
# import animations.compounds

class Effect(Animatable):
    def __init__(self, name=None, arguments={}):
        super().__init__()
        self.id = id
        self.name = name
        self.arguments = arguments
        self.animation_for(self.name)

    def stage(self, zone=Zone):
        if self.animation_class == None:
            return

        self.animation = self.animation_class({ "range": zone.range(), **self.arguments })

    def render(self):
        if self.animation:
            self.animation.render()