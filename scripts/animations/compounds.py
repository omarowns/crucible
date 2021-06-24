import time
from rpi_ws281x import Color
from models.factories import AnimationFactory
from animations.interfaces import *
from animations.basics import StaticAnimation

class SirenAnimation(StaticAnimation, ClearableAnimation):
    def render(self, siren_one, siren_two):
        led_start = self.led_start
        led_end = self.led_end
        led_mid = led_end/2

        AnimationFactory().build(
            siren_one.get("name"),
            {
                led_start: 0,
                led_end: led_mid,
                **siren_one.get("arguments")
            }).render()
        self.clear()
        AnimationFactory().build(
            siren_two.get("name"),
            {
                led_start: led_mid,
                led_end: led_end,
                **siren_two.get("arguments")
            }).render()
        self.clear()