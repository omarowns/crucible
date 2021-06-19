import time

class DefaultAnimations(object):
    def __init__(self):
       self.strip = self.strip

    def colorWipe(self, color, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)
