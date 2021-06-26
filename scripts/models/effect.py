from models.zone import Zone
from models.concerns import RenderableAnimation, HasZone
# import animations.basics
# import animations.compounds

class Effect(RenderableAnimation, HasZone):
    def __init__(self, name=None, arguments={}):
        super().__init__(arguments=arguments)
        self.id = id
        self.name = name
        self.arguments = arguments
        self.animation_for(self.name)