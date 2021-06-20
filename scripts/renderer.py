from strip import Strip
from default_animations import DefaultAnimations
from rpi_ws281x import Color

class Renderer(DefaultAnimations):
    def  __init__(self):
        self.strip = Strip()

    def render(self):
        self.colorWipe(Color(*[255, 0, 0]))
        self.colorWipe(Color(*[0, 255, 0]))
        self.colorWipe(Color(*[0, 0, 255]))

    def clear(self):
        self.colorWipe(Color(0,0,0), 10)