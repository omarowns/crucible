from models.zone import Zone
from models.concerns import Animatable, StageableAnimation, RenderableAnimation
# import animations.basics
# import animations.compounds

class Effect(RenderableAnimation, StageableAnimation, Animatable):
    def __init__(self, name=None, arguments={}):
        super().__init__()
        self.id = id
        self.name = name
        self.arguments = arguments
        self.animation_for(self.name)