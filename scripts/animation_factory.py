from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class AnimationFactory():
    def  __init__(self):
        self.strip = Strip()

    def render(self, renderer_class, led_start=None, led_end=None, color_args=None):
        renderer_class(self.strip, led_start=led_start, led_end=led_end, base_color_args=color_args).render

    def clear(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()