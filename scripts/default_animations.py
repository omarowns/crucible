import time
from rpi_ws281x import Color

class Animation():
    def __init__(self, strip, args = {}):
        self.strip = strip
        self.led_start = args.get("led_start", 0)
        self.led_end = args.get("led_end", 0)
        self.base_color_args = args.get("base_color_args", [0,0,0])

class ClearAnimation(Animation):
    def render(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

class StaticAnimation(Animation):
    def __init__(self, strip, args = {}):
        super().__init__(self, strip, args)
        self.end_wait = args.get("end_wait", 500)

    def render(self):
        for i in range(self.led_start, self.led_end):
            self.strip.setPixelColor(i, Color(*self.base_color_args))
        self.strip.show()
        time.sleep(self.end_wait/1000.0)

class ColorWipe():
    @classmethod
    def call(cls, strip, led_start, led_end, color_args, wait_ms=50):
        for i in range(led_start, led_end):
            strip.setPixelColor(i, Color(*color_args))
            strip.show()
            time.sleep(wait_ms/1000.0)

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