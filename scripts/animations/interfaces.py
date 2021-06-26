from inspect import getmembers as implementations
from importlib import import_module
import time
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
        super().__init__()
        self.range.reverse()

class ColorableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        import pdb; pdb.set_trace()
        self.color = Color(*args.get("color_args", [0,0,0]))

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
