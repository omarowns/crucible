class AnimationFactory():
    from inspect import getmembers as implementations
    from importlib import import_module
    import animations
    from strip import Strip

    def  __init__(self):
        self.strip = Strip()

    def build(self, renderer_class, rest = {}):
        if self.animation_class(renderer_class):
            self.animation = self.animation_class(renderer_class)(self.strip, args = rest)

    def render(self):
        self.animation.render()

    def animation_class(self, renderer_class):
        if renderer_class in implementations(animations.basics):
            getattr(import_module('animations.basics'), renderer_class)
        if renderer_class in implementations(animations.compounds):
            getattr(import_module('animations.compounds'), renderer_class)

from models.effect import Effect
class EffectFactory():

    @classmethod
    def build(self, name=None, args = {}):
        Effect(name=name, args=args)