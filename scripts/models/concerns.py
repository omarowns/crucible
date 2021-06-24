from inspect import getmembers as implementations
from importlib import import_module
from models.zone import Zone

class Animatable():
    def __init__(self):
        self.animation_classes = []
        self.animation_class = None
        self.animation = None
        self.load_animation_classes()

    def animation_for(self, name):
        if self.animation_class != None:
            return self.animation_class

        animation_classes = list(filter(lambda klass : str(klass) == name, self.animation_classes))
        
        if len(animation_classes) == 1:
            self.animation_class = animation_classes[0]

        self.animation_class

    def load_animation_class(self):
        self.animation_class = None

        effect_animation_classes = list(filter(lambda klass : str(klass) == self.name, self.animation_classes))
        if len(effect_animation_classes) == 1:
            self.animation_class = effect_animation_classes[0]

    def load_animation_classes(self):
        try:
            import_module('animations.basics')
            import_module('animations.compounds')
            
            self.animation_classes = {}

            for (klass, _) in implementations(getattr(import_module('animations'), 'basics')):
                self.animation_classes.add(getattr(import_module('animations.basics'), klass))

            for (klass, _) in implementations(getattr(import_module('animations'), 'compounds')):
                self.animation_classes.add(getattr(import_module('animations.compunds'), klass))

            self.animation_classes = list(self.animation_classes)
        except:
            self.animation_classes = []

class StageableAnimation(Animatable):
    def __init__(self):
        super().__init__()
        self.staged = False

    def stage(self, zone=Zone):
        self.stage_animation_with_zone(zone, self.arguments)
        self.staged = True and bool(self.animation)

    def stage_animation_with_zone(self, zone=Zone, arguments = {}):
        if self.animation_class == None:
            return

        self.animation = self.animation_class({ "range": zone.range(), **arguments})

class RenderableAnimation(StageableAnimation):
    def __init__(self):
        super().__init__()

    def render(self):
        if self.staged:
            self.animation.render()