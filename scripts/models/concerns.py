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
        
        self.load_animation_class(name)

    def load_animation_class(self, name):
        self.animation_class = None

        for klass in self.animation_classes:
            if name == klass.__name__:
                self.animation_class = klass

        self.animation_class

    def load_animation_classes(self):
        try:
            import_module('animations.basics')
            import_module('animations.compounds')
            
            self.animation_classes = set([])

            for (klass, _) in implementations(getattr(import_module('animations'), 'basics')):
                self.animation_classes.add(getattr(import_module('animations.basics'), klass))

            for (klass, _) in implementations(getattr(import_module('animations'), 'compounds')):
                self.animation_classes.add(getattr(import_module('animations.compunds'), klass))

            self.animation_classes = [*self.animation_classes]
        except:
            self.animation_classes = []

class StageableAnimation(Animatable):
    def __init__(self):
        super().__init__()
        self.staged = False

    def stage(self, zone=Zone, name={}, arguments={}):
        self.stage_animation_with_zone(zone, name, arguments)
        self.staged = True and bool(self.animation)

    def stage_animation_with_zone(self, zone=Zone, name=None, arguments = {}):
        if self.animation_class == None:
            if not self.load_animation_class(name):
                return

        self.animation = self.animation_class({ "range": zone.range(), **arguments})

class RenderableAnimation(StageableAnimation):
    def __init__(self):
        super().__init__()

    def render(self):
        if self.staged:
            self.animation.render()