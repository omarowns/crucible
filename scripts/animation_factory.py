from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class AnimationFactory():
    _AVAILABLE_FACTORIES = {
        "ClearAnimation": ClearAnimation,
        "StaticAnimation": StaticAnimation
    }

    def  __init__(self):
        self.strip = Strip()

    def render(self, renderer_class, rest = None):
        animation = self._AVAILABLE_FACTORIES[renderer_class](self.strip, args = rest)
        print(f'AnimationFactory::render::DEBUG: animation:{animation}')
        animation.render