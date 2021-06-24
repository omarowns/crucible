import time
from rpi_ws281x import Color
from animations.basics import StaticAnimation
from animations.interfaces import *
from models.zone import Zone
from models.effect import Effect
from effect_queue import EffectQueue

class SirenAnimation(StaticAnimation, ClearableAnimation):
    def render(self, siren_one, siren_two):
        first_siren_effect = Effect(siren_one.get("name"), siren_one.get("arguments"))
        second_siren_effect = Effect(siren_two.get("name"), siren_two.get("arguments"))
        clear_effect = Effect("ClearAnimation")

        first_siren_zone = Zone(start=self.range[0], end=self.range[-1]/2)
        second_siren_zone = Zone(start=self.range[-1]/2, end=self.range[-1])

        effects = [first_siren_zone, clear_effect, second_siren_effect, clear_effect]
        zones = [first_siren_zone, first_siren_zone, second_siren_zone, second_siren_zone]

        effect_zones = zip(effects, zones)

        for (effect, zone) in effect_zones:
            EffectQueue().put([effect, zone])
        EffectQueue().join()