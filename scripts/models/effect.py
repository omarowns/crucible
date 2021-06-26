from models.concerns import RenderableAnimation

class Effect(RenderableAnimation):
    def __init__(self, name=None, arguments={}):
        super().__init__()
        self.id = id
        self.name = name
        self.arguments = arguments
        self.zone = None
        self.animation_for(self.name)