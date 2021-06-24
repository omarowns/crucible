import time
from rpi_ws281x import Color
from animations.interfaces import *

class ClearAnimation(ClearableAnimation):
    def render(self):
        self.clear()

class StaticAnimation(SegmentableAnimation, ColorableAnimation, EndWaitableAnimation):
    def render(self):
        for i in range(*self.range):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        time.sleep(self.end_wait_ms/1000.0)