#!/usr/bin/env python3

import argparse
import threading
from time import sleep, time
from models.zone import Zone
from models.action import Action
from models.effect import Effect
from queues import EffectQueue, SubEffectQueue

def mainEffectWorker():
    while True:
        effect, zone = EffectQueue().get()
        import pdb; pdb.set_trace()
        effect.render(zone=zone)
        EffectQueue().task_done()

def subEffectWorker():
    while True:
        effect, zone = SubEffectQueue().get()
        effect.render(zone=zone)
        SubEffectQueue().task_done()

def actionWorker():
    while True:
        for effect_item in action.effects:
            EffectQueue().put([Effect(**effect_item), zone])
        EffectQueue().join()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--zone', default="1", help='the zone to run the effect on')
    parser.add_argument('--action', help='action to run')
    program_arguments = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not program_arguments.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        threading.Thread(target=mainEffectWorker, daemon=True).start()
        threading.Thread(target=subEffectWorker, daemon=True).start()

        zone = Zone.find_by("id", program_arguments.zone) or Zone.find_by("name", program_arguments.zone)
        action = Action.find_by("id", program_arguments.action) or Action.find_by("name", program_arguments.action)

        if action.is_loopable():
            for _ in range(0, action.loop_iterations()):
                for effect_item in action.effects:
                    EffectQueue().put([Effect(**effect_item), zone])
            EffectQueue().join()
        elif action.is_timeable():
            threading.Thread(target=actionWorker, daemon=True).start()
            sleep(action.time)
        else:
            for effect_item in action.effects:
                EffectQueue().put([Effect(**effect_item), zone])
            EffectQueue().join()

    except KeyboardInterrupt:
        if program_arguments.clear:
            Effect(name="ClearAnimation").stage().render()
