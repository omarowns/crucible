from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class AnimationFactory():
    def  __init__(self):
        self.strip = Strip()

    def render(self, renderer_class, *rest):
        render_led_start = rest.led_start or None
        render_led_end = rest.led_end or None
        color_args = rest.color_args or None

        renderer_class(
            self.strip,
            led_start=render_led_start,
            led_end=render_led_end,
            base_color_args=color_args).render