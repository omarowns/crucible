#!/usr/bin/env python3

import argparse
import time
from default_animations import StaticAnimation, ClearAnimation
from animation_factory import AnimationFactory

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    animation_factory = AnimationFactory()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        while True:
            time.sleep(500/1000.0)

            animation_factory.render(
                "StaticAnimation",
                renderer_led_start=0,
                renderer_led_end=6,
                color_args=[255,0,0])

            time.sleep(500/1000.0)

            animation_factory.render(
                "StaticAnimation",
                renderer_led_start=0,
                renderer_led_end=6,
                color_args=[0,0,255])

            # print ('Theater chase animations.')
            # strip.theaterChase(Color(127, 127, 127))  # White theater chase
            # strip.theaterChase(Color(127,   0,   0))  # Red theater chase
            # strip.theaterChase(Color(  0,   0, 127))  # Blue theater chase
            # print ('Rainbow animations.')
            # strip.rainbow
            # strip.rainbowCycle
            # strip.theaterChaseRainbow

    except KeyboardInterrupt:
        if args.clear:
            animation_factory.render(ClearAnimation)