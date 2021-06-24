import time
from rpi_ws281x import Color
from interfaces import *

class ClearAnimation(SegmentableAnimation):
    def render(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

class StaticAnimation(SegmentableAnimation, ColorableAnimation, EndWaitableAnimation):
    def render(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        time.sleep(self.end_wait_ms/1000.0)