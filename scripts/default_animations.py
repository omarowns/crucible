import time
from strip import Strip

class DefaultAnimations:
    def __init__(self):
        self.strip = Strip()

    def colorWipe(self, color, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)
