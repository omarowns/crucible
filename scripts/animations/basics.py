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

class BlinkAnimation(SegmentableAnimation, StepableAnimation, WaitableAnimation):
    def render(self):
        original_brightness = self.strip.getBrightness()
        brightness = original_brightness
        while brightness >= 0:
            brightness -= self.steps
            self.strip.setBrightness(brightness)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)
        while brightness <= original_brightness:
            brightness += self.steps
            self.strip.setBrightness(brightness)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)

class ColorWipe(SegmentableAnimation, ColorableAnimation, WaitableAnimation):
    def render(self):
        for i in range(*self.range):
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)