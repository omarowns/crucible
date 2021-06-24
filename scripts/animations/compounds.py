import time
from animations.basics import StaticAnimation
from animations.interfaces import *

from models.zone import Zone
from models.effect import Effect
from effect_queue import EffectQueue

class SirenAnimation(StaticAnimation):

    def __init__(self, args={}):
        super().__init__(args=args)
        
        self.first_zone = Zone(start=self.range[0], end=int(self.range[-1]/2))
        self.last_zone = Zone(start=int(self.range[-1]/2), end=self.range[-1])
        import pdb; pdb.set_trace()
        self.siren_one_effect = self.siren_effect_for(args.get("siren_one"))
        self.siren_two_effect = self.siren_effect_for(args.get("siren_two"))
        self.clear_effect = Effect(name="ClearAnimation")

        self.effects = [self.siren_one_effect, self.clear_effect, self.siren_two_effect, self.clear_effect]
        self.zones = [self.first_zone, self.first_zone, self.last_zone, self.last_zone]

    def render(self):
        for (effect, zone) in zip(self.effects, self.zones):
            EffectQueue().put([effect, zone])
        EffectQueue().join()

    def siren_effect_for(self, arguments):
        Effect(name=arguments.get("name"), arguments=arguments.get("arguments"))
