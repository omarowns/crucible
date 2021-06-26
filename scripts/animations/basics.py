import time
from rpi_ws281x import Color
from animations.interfaces import *

class ClearAnimation(ClearableAnimation):
    def render(self):
        self.clear()

class StaticAnimation(RangeableAnimation, ColorableAnimation, EndWaitableAnimation):
    def render(self):
        for i in range(*self.range):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        self.endWait()

class BlinkAnimation(RangeableAnimation, StepableAnimation, WaitableAnimation):
    def render(self):
        original_brightness = self.strip.getBrightness()
        brightness = original_brightness
        while brightness >= 0:
            self.strip.setBrightness(brightness)
            self.strip.show()
            brightness -= self.steps
            time.sleep(self.wait_ms/1000.0)
        brightness = 0
        while brightness <= original_brightness:
            self.strip.setBrightness(brightness)
            self.strip.show()
            brightness += self.steps
            time.sleep(self.wait_ms/1000.0)

class ColorWipeAnimation(RangeableAnimation, ColorableAnimation, WaitableAnimation):
    def render(self):
        for i in range(*self.range):
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)

class FreezeAnimation(TimeoutableAnimation):
    def render(self):
        self.timeout()