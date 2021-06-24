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

# Implementations

class ClearAnimation(SegmentableAnimation):
    def render(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

class StaticAnimation(SegmentableAnimation, ColorableAnimation, EndWaitableAnimation):
    def render(self):
        import pdb; pdb.set_trace()
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        time.sleep(self.end_wait_ms/1000.0)

class ColorWipe(SegmentableAnimation, ColorableAnimation, WaitableAnimation):
    def render(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(self.wait_ms/1000.0)

class TheaterChase():
    @classmethod
    def call(cls, strip, led_start, led_end, color_args, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(led_start, led_end, 3):
                    strip.setPixelColor(i+q, Color(*color_args))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(led_start, led_end, 3):
                    strip.setPixelColor(i+q, 0)

class Rainbow():
    @classmethod
    def call(cls, strip, led_start, led_end, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(led_start, led_end):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

class RainbowCycle():
    @classmethod
    def call(cls, strip, led_start, led_end, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes it across all pixels."""
        for j in range(256*iterations):
            for i in range(led_start, led_end):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

class TheaterChaseRainbow():
    @classmethod
    def call(cls, strip, led_start, led_end, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((i+j) % 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)