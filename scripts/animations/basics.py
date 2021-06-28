import time
from rpi_ws281x import Color
from animations.interfaces import *

class ClearAnimation(ClearableAnimation):
    def render(self):
        self.clear()

class StaticAnimation(ColorableAnimation, WaitableAnimation):
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

class BreatheAnimation(ColorableAnimation, StepableAnimation, WaitableAnimation):
    def render(self):
        brightness_steps = list(range(0, 255))
        brightness_steps = [*brightness_steps, *brightness_steps[::-1]]

        self.color = self.color or Color(255, 255, 255)
        self.fill()
        self.strip.setBrightness(0)
        self.strip.show()

        for bright_i in range(0, len(brightness_steps), self.steps):
            self.strip.setBrightness(brightness_steps[bright_i])
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
            self.wait()
        brightness = 0
        while brightness <= original_brightness:
            self.strip.setBrightness(brightness)
            self.strip.show()
            brightness += self.steps
            self.wait()

class CometAnimation(ColorableAnimation, WaitableAnimation):
    def __init__(self, args):
        super().__init__(args=args)
        self.comet_color = Color(*args.get("comet_color"))
        self.comet_size = args.get("comet_size", 2)

    def drawComet(self, position):
        for comet_i in range(self.comet_size):
            t_position = position + comet_i
            t_position = (t_position < 0 and 0) or t_position
            t_position = (t_position > self.led_end and self.led_end) or t_position
            self.strip.setPixelColor(t_position, self.comet_color)

    def render(self):
        for position in self.range:
            self.drawComet(position)
            self.decreaseRandomPixelsBrightness(amount=self.fade_amount)
            self.strip.show()
            self.wait()

        self.range.reverse()
        for position in self.range:
            self.drawComet(position)
            self.decreaseRandomPixelsBrightness(amount=self.fade_amount)
            self.strip.show()
            self.wait()


class ColorWipeAnimation(ColorableAnimation, WaitableAnimation):
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