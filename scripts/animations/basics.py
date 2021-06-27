import time
from rpi_ws281x import Color
from animations.interfaces import *

class ClearAnimation(ClearableAnimation):
    def render(self):
        self.clear()

class StaticAnimation(RangeableAnimation, ColorableAnimation, WaitableAnimation):
    def render(self):
        for i in self.range:
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        self.wait()

class RandomColorAnimation(StaticAnimation):
    def render(self):
        self.color = self.randomColor()
        super()

class DynamicRandomColorAnimation(StaticAnimation):
    def render(self):
        for i in self.range:
            self.strip.setPixelColor(i, self.randomColor())
        self.strip.show()
        self.wait()

class SingleDynamicRandomColorAnimation(DynamicRandomColorAnimation):
    def render(self):
        randomPos = random.randint(self.led_start, self.led_end)
        self.strip.setPixelColor(randomPos, self.randomColor())
        self.strip.show()
        self.wait()

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

class CometAnimation(RangeableAnimation, ColorableAnimation):
    def __init__(self, args):
        super().__init__(args=args)
        self.comet_color = Color(*args.get("comet_color"))
        self.comet_size = args.get("comet_size", 2)

    def render(self):
        for position in self.range:
            import pdb; pdb.set_trace()
            for _x in range(self.comet_size):
                self.strip.setPixelColor(position + 1, self.comet_color)

            if self.fade_amount:
                for i in self.range:
                    if (random.randint(0, 10) > 5):
                        self.color = self.fadeToBlackBy(color=self.strip.getPixelColor(i), amount=self.fade_amount)
            self.strip.show()


class ColorWipeAnimation(RangeableAnimation, ColorableAnimation, WaitableAnimation):
    def render(self):
        for i in self.range:
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)

class ReverseColorWipeAnimation(ColorWipeAnimation, ReversableAnimation):
    def __init__(self, args):
        super().__init__(args=args)

class FreezeAnimation(TimeoutableAnimation):
    def render(self):
        self.timeout()