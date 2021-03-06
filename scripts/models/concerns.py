from inspect import getmembers as implementations
from importlib import import_module
from typing import DefaultDict
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

        klasses = [klass for klass in [klass for klass in self.animation_classes if hasattr(klass, "__name__") and callable(klass)] if klass.__name__ == name]
        if len(klasses) == 1:
            self.animation_class = klasses[0]

        self.animation_class

    def load_animation_classes(self):
        try:
            import_module('animations.basics')
            import_module('animations.compounds')
            
            self.animation_classes = set([])

            for (klass, _) in implementations(getattr(import_module('animations'), 'basics')):
                try:
                    self.animation_classes.add(getattr(import_module('animations.basics'), klass))
                except:
                    pass

            for (klass, _) in implementations(getattr(import_module('animations'), 'compounds')):
                try:
                    self.animation_classes.add(getattr(import_module('animations.compounds'), klass))
                except:
                    pass

            self.animation_classes = [*self.animation_classes]
        except:
            self.animation_classes = []

class StageableAnimation(Animatable):
    def stage(self):
        if self.animation_class == None:
            if not self.load_animation_class(self.name):
                return

        self.animation = self.animation_class(args={ "zone": self.zone, **self.arguments})

class RenderableAnimation(StageableAnimation):
    def __init__(self, arguments={}):
        super().__init__()

    def render(self, zone=None):
        if bool(self.zone):
            self.zone = zone or self.zone
            self.stage()
        if bool(self.animation):
            self.animation.render()

class HasZone():
    def __init__(self, arguments={}) -> None:
        super().__init__()
        self.zone = None
        if arguments.get("zone_id"):
            self.zone = Zone.find_by("id", arguments.get("zone_id")) or Zone.find_by("name", arguments.get("zone_id"))
        self.zone = self.zone or Zone.find_by("id", 1)