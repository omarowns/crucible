from strip import Strip
from rpi_ws281x import Color

class Renderer():
    def  __init__(self):
        self

    def render(self):
        Strip().colorWipe(Color(*[255, 0, 0]))
        Strip().colorWipe(Color(*[0, 255, 0]))
        Strip().colorWipe(Color(*[0, 0, 255]))

    def clear(self):
        Strip().colorWipe(Color(0,0,0), 10)