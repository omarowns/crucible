import time
from rpi_ws281x import Color
from animation_factory import AnimationFactory
from interfaces import *
from basics import StaticAnimation

class SirenAnimation(StaticAnimation, ClearableAnimation):
    def render(self, siren_one, siren_two):
        led_start = 0
        led_end = self.strip.numPixels()
        led_mid = led_end/2

        AnimationFactory().render(
            siren_one.get("name"),
            {
                led_start: 0,
                led_end: led_mid,
                **siren_one.get("arguments")
            })
        self.clear()
        AnimationFactory().render(
            siren_two.get("name"),
            {
                led_start: led_mid,
                led_end: led_end,
                **siren_two.get("arguments")
            })
        self.clear()