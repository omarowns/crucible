from inspect import getmembers as implementations
from importlib import import_module

class Animatable():
    def __init__(self):
        self.animation_classes = []
        self.animation_class = None
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