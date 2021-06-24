#!/usr/bin/env python3

import argparse
import threading
from models.zone import Zone
from models.action import Action
from models.effect import Effect
from effect_queue import EffectQueue

def effectWorker():
    while True:
        effect, zone = EffectQueue().get()
        effect.stage(zone=zone)
        effect.render()
        EffectQueue().task_done()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('zone', default="1", action='store_true', help='the zone to run the effect on')
    parser.add_argument('action', action='store_true', help='action to run')
    args = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        threading.Thread(target=effectWorker, daemon=True).start()

        zone = Zone().find_by("id", args.zone) or Zone().find_by("name", args.zone)
        action = Action().find_by("id", args.action) or Action().find_by("name", args.action)
        for effect in action.effects:
            EffectQueue().put([effect, zone])
        EffectQueue().join()
    except KeyboardInterrupt:
        if args.clear:
            Effect(name="ClearAnimation").stage().render()
