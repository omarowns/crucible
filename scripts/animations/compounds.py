import time
from rpi_ws281x import Color
from animations.basics import StaticAnimation
from animations.interfaces import *

from models.zone import Zone
from models.effect import Effect
from effect_queue import EffectQueue

class SirenAnimation(StaticAnimation, ClearableAnimation):

    def __init__(self, strip, args):
        super().__init__(strip, args=args)
        
        self.first_zone = Zone(start=self.range[0], end=(self.range[-1]/2))
        self.last_zone = Zone(start=(self.range[-1]/2), end=self.range[-1])

        self.siren_one_effect = self.siren_effect_for(args.get("siren_one"))
        self.siren_two_effect = self.siren_effect_for(args.get("siren_two"))
        self.clear_effect = Effect(name="ClearAnimation")

    def render(self):
        effects = [self.siren_one_effect, self.clear_effect, self.siren_two_effect, self.clear_effect]
        zones = [self.first_zone, self.first_zone, self.last_zone, self.last_zone]

        for (effect, zone) in zip(effects, zones):
            EffectQueue().put([effect, zone])
        EffectQueue().join()

    def siren_effect_for(args = {}):
        name = args.get("name")
        attributes = args.get("attributes")
        Effect(name=name, attributes=attributes)
