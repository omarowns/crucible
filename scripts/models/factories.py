from strip import Strip
from animations.basics import *
from animations.compounds import *
from rpi_ws281x import Color

class AnimationFactory():
    _AVAILABLE_FACTORIES = {
        "ClearAnimation": ClearAnimation,
        "StaticAnimation": StaticAnimation
    }

    def  __init__(self):
        self.strip = Strip()

    def build(self, renderer_class, rest = {}):
        self._animation = self._AVAILABLE_FACTORIES[renderer_class](self.strip, args = rest)
    
    def render(self):
        self._animation.render()