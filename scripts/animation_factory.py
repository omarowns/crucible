from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class AnimationFactory():
    def  __init__(self):
        self.strip = Strip()

    def render(self, renderer_class, rest = None):
        renderer_class(self.strip, args = rest).render