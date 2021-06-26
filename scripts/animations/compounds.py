from pdb import set_trace
from threading import Thread
import time
from animations.interfaces import RangeableAnimation, LoopableAnimation, MultiEffectableAnimation

from models.zone import Zone
from models.effect import Effect
from queues import SubEffectQueue

class SirenAnimation(RangeableAnimation):

    def __init__(self, args={}):
        super().__init__(args=args)
        
        self.first_zone = Zone(start=self.range[0], end=int(self.range[-1]/2))
        self.last_zone = Zone(start=int(self.range[-1]/2), end=self.range[-1])

        self.siren_one_effect = self.siren_effect_for(args.get("siren_one"))
        self.siren_two_effect = self.siren_effect_for(args.get("siren_two"))
        self.clear_effect = Effect(name="ClearAnimation")

        self.effects = [self.siren_one_effect, self.clear_effect, self.siren_two_effect, self.clear_effect]
        self.zones = [self.first_zone, self.first_zone, self.last_zone, self.last_zone]

    def render(self):
        for (effect, zone) in zip(self.effects, self.zones):
            SubEffectQueue().put([effect, zone])
        SubEffectQueue().join()

    def siren_effect_for(self, arguments) -> Effect:
        return Effect(name=arguments.get("name"), arguments=arguments.get("arguments"))

class ParallelAnimation(RangeableAnimation, MultiEffectableAnimation):
    def __init__(self, args):
        super().__init__(args=args)
        self.effect_args = None

    def render(self):
        for effect_args in self.effects:
            thread = Thread(target=self._renderAsync, kwargs={"args":effect_args})
            thread.start()
            thread.join()

    def _renderAsync(self, arguments={}):
        while arguments.get("name") and arguments.get("arguments"):
            effect = Effect(arguments)
            effect.render()

class LoopAnimation(LoopableAnimation, MultiEffectableAnimation):
    def __init__(self, args):
        super().__init__(args=args)

    def render(self):
        for i in range(self.loops):
            for effect_args in self.effects:
                SubEffectQueue().put([Effect(**effect_args), None])
        SubEffectQueue().join()