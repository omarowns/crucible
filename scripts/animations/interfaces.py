import time
from rpi_ws281x import Color
from strip import Strip

class Stripable():
    def __init__(self):
        super().__init__()
        self.strip = Strip()

class Animation(Stripable):
    def __init__(self, args = None):
        super().__init__()

class SegmentableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
        self.led_start = args.get("led_start", 0)
        self.led_end = args.get("led_end", self.strip.numPixels())
        self.range = args.get("range", [self.led_start, self.led_end])

class ColorableAnimation(Animation):
    def __init__(self, args = {}):
        super().__init__(args = args)
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
        time.sleep(self.timeout_ms)

class ClearableAnimation(SegmentableAnimation):
    def clear(self):
        for i in range(*self.range):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()