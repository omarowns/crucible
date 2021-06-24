#!/usr/bin/env python3

import argparse
import threading
from models.zone import Zone
from models.action import Action
from models.effect import Effect
from queues import EffectQueue, SubEffectQueue

def mainEffectWorker():
    while True:
        effect, zone = EffectQueue().get()
        import pdb; pdb.set_trace()
        effect.stage(zone=zone)
        effect.render()
        EffectQueue().task_done()

def subEffectWorker():
    while True:
        effect, zone = SubEffectQueue().get()
        import pdb; pdb.set_trace()
        effect.stage(zone=zone)
        effect.render()
        SubEffectQueue().task_done()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--zone', default="1", help='the zone to run the effect on')
    parser.add_argument('--action', help='action to run')
    args = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        threading.Thread(target=mainEffectWorker, daemon=True).start()
        threading.Thread(target=subEffectWorker, daemon=True).start()

        zone = Zone.find_by("id", args.zone) or Zone.find_by("name", args.zone)
        action = Action.find_by("id", args.action) or Action.find_by("name", args.action)

        for effect_item in action.effects:
            EffectQueue().put([Effect(**effect_item), zone])

        EffectQueue().join()
    except KeyboardInterrupt:
        if args.clear:
            Effect(name="ClearAnimation").stage().render()
