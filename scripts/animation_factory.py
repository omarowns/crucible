import logging
from strip import Strip
from default_animations import *
from rpi_ws281x import Color

class AnimationFactory():
    _AVAILABLE_FACTORIES = {
        "ClearAnimation": ClearAnimation,
        "StaticAnimation": StaticAnimation
    }

    def  __init__(self):
        self.strip = Strip()
        logging.debug("Strip initialized")

    def render(self, renderer_class, rest = None):
        logging.debug(f'Invoking {renderer_class} with args {rest}')
        self._AVAILABLE_FACTORIES[renderer_class](self.strip, args = rest).render