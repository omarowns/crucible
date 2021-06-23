from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class Renderer():
    def  __init__(self):
        self.strip = Strip()

    def render(self, renderer_class, led_start, led_end, rest):
        renderer_class.call(self.strip, led_start, led_end, **rest)

    def clear(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()