from inspect import getmembers as implementations
from importlib import import_module
import time
import random
from rpi_ws281x import Color
from strip import Strip

class Stripable():
    def __init__(self, args={}):
        super().__init__()
        self.strip = Strip()

class Animation(Stripable):
    def __init__(self, args={}):
        super().__init__(args=args)

class SegmentableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.led_start = args.get("led_start", 0)
        self.led_end = args.get("led_end", self.strip.numPixels())

class ZonableAnimation(SegmentableAnimation):
    def __init__(self, args={}):
        super().__init__(args=args)
        self.zone = args.get("zone")

class RangeableAnimation(ZonableAnimation):
    def __init__(self, args={}):
        super().__init__(args=args)
        if self.zone:
            self.range = [*range(*self.zone.range)]
        else:
            self.range = [*range(*args.get("range", [self.led_start, self.led_end]))]

class ReversableAnimation(RangeableAnimation):
    def __init__(self, args={}):
        super().__init__(args=args)
        self.range.reverse()

class ColorableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.color = Color(*args.get("color_args", [0,0,0]))
        self.fade_amount = args.get("fade_amount", None)
    
    def randomColor(self):
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def colorWheel(self, position = 0):
        if position < 85:
            return Color(position * 3, 255 - position * 3, 0)
        elif position < 170:
            position -= 85
            return Color(255 - position * 3, 0, position * 3)
        else:
            position -= 170
            return Color(0, position * 3, 255 - position * 3)
    
    def colorBlend(self, color1=0, color2=0, blend=0):
        if blend == 0:
            return color1
        if blend == 255:
            return color2
        
        w1 = (color1 >> 24) & 0xff
        r1 = (color1 >> 16) & 0xff
        g1 = (color1 >>  8) & 0xff
        b1 =  color1        & 0xff

        w2 = (color2 >> 24) & 0xff
        r2 = (color2 >> 16) & 0xff
        g2 = (color2 >>  8) & 0xff
        b2 =  color2        & 0xff

        w3 = ((w2 * blend) + (w1 * (255 - blend))) / 256
        r3 = ((r2 * blend) + (r1 * (255 - blend))) / 256
        g3 = ((g2 * blend) + (g1 * (255 - blend))) / 256
        b3 = ((b2 * blend) + (b1 * (255 - blend))) / 256

        return ((w3 << 24) | (r3 << 16) | (g3 << 8) | (b3))
    
    def fadeToBlackBy(self, color=None, amount=0):
        return self.fadeToBy(target=0, color=color, amount=amount)
    
    def fadeToWhiteBy(self, color=None, amount=0):
        return self.fadeToBy(target=255, color=color, amount=amount)
    
    def fadeToBy(self, target=0, color=None, amount=0):
        white   = (color >> 24) & 0xff
        red     = (color >> 16) & 0xff
        green   = (color >>  8) & 0xff
        blue    =  color        & 0xff

        # Limit the target fade to min 0 and max 255 (black and white)
        target = (target < 0 and 0) or (target > 255 and 255) or target
        # Restrict to only 0 or 255
        if target < (255 - target):
            target = 0
        else:
            target = 255

        Fade = {
            0: lambda c, a: (c - a > 0 and c - a) or 0,
            255: lambda c, a: (c + a > 255 and c + a) or 255,
        }
                
        white_faded = Fade[target](white, amount)
        red_faded = Fade[target](red, amount)
        green_faded = Fade[target](green, amount)
        blue_faded = Fade[target](blue, amount)

        return Color(red_faded, green_faded, blue_faded, white_faded)

class BrightnessControllableAnimation(RangeableAnimation, ColorableAnimation):
    def decreaseAllPixelsBrightness(self, amount = 15):
        for i in self.range:
            self.decreasePixelBrightness(i, amount=amount)
    
    def increaseAllPixelsBrightness(self, amount = 15):
        for i in self.range:
            self.increasePixelBrightness(i, amount=amount)

    def decreasePixelBrightness(self, pixel, amount = 15):
        color = self.fadeToBlackBy(color=self.strip.getPixelColor(pixel), amount=amount)
        self.strip.setPixelColor(pixel, color)

    def increasePixelBrightness(self, pixel, amount = 15):
        color = self.fadeToWhiteBy(color=self.strip.getPixelColor(pixel), amount=amount)
        self.strip.setPixelColor(pixel, color)

    def decreaseRandomPixelsBrightness(self, amount = 15, random_stdev=5):
        for i in self.range:
            if (random.randint(0, 10) > random_stdev):
                self.decreasePixelBrightness(i, amount=amount)
    
    def increaseRandomPixelsBrightness(self, amount = 15, random_stdev=5):
        for i in self.range:
            if (random.randint(0, 10) > random_stdev):
                self.increasePixelBrightness(i, amount=amount)

class DualColorableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.color_one = Color(*args.get("color_one_args", [0,0,0]))
        self.color_two = Color(*args.get("color_two_args", [0,0,0]))

class EndWaitableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.end_wait_ms = args.get("end_wait_ms", None)

    def endWait(self):
        if self.end_wait_ms == None:
            return
        time.sleep(self.end_wait_ms/1000.0)

class WaitableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.wait_ms = args.get("wait_ms", 50)
    
    def wait(self):
        time.sleep(self.wait_ms/1000.0)

class IntervalableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.intervals = args.get("intervals", 5)

class StepableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.steps = args.get("steps", 10)

class TimeoutableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.timeout_ms = args.get("timeout_ms", 5000)

    def timeout(self):
        time.sleep(self.timeout_ms/1000.0)

class ClearableAnimation(RangeableAnimation):
    def clear(self):
        for i in self.range:
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

class LoopableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args=args)
        self.loops = int(args.get("loops"))

class MultiEffectableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args=args)
        self.effects = args.get("effects")

class CounterModeCallableAnimation(Animation):
    def __init__(self, args):
        super().__init__(args=args)
        self.counterModeCall = args.get("counter_mode_call")