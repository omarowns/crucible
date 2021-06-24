from inspect import getmembers as implementations
from importlib import import_module
from models.zone import Zone
# import animations.basics
# import animations.compounds

class Effect():
    def __init__(self, name=None, arguments={}):
        self.id = id
        self.name = name
        self.arguments = arguments

    def stage(self, zone=Zone):
        self.animation = self.animation_class()({ "range": zone.range(), **self.arguments })

    def render(self):
        if self.animation:
            self.animation.render()

    def animation_class(self):
        if self.name in [klass for (klass, _) in implementations(getattr(import_module('animations'), 'basics'))]:
            getattr(import_module('animations.basics'), self.name)
        if self.name in [klass for (klass, _) in implementations(getattr(import_module('animations'), 'compounds'))]:
            getattr(import_module('animations.compounds'), self.name)

