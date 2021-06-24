import time
from rpi_ws281x import Color

class Animation():
    def __init__(self, strip, args = None):
        self.strip = strip

# Interfaces

class SegmentableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} SegmentableAnimation, args:{args}')
        self.led_start = args.get("led_start", 0)
        self.led_end = args.get("led_end", self.strip.numPixels())

class ColorableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} ColorableAnimation, args:{args}')
        self.color = Color(*args.get("color_args", [0,0,0]))

class EndWaitableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} EndWaitableAnimation, args:{args}')
        self.end_wait_ms = args.get("end_wait_ms", 500)

class WaitableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} WaitableAnimation, args:{args}')
        self.wait_ms = args.get("wait_ms", 50)

class IntervalableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} IntervalableAnimation, args:{args}')
        self.intervals = args.get("intervals", 5)

class TimeoutableAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(strip, args = args)
        print(f'{self} TimeoutableAnimation, args:{args}')
        self.timeout_ms = args.get("timeout_ms", 5000)

class ClearableAnimation(SegmentableAnimation):
    def clear(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()