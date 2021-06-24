#!/usr/bin/env python3

import argparse
from default_animations import StaticAnimation, ClearAnimation
from animation_factory import AnimationFactory

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    animation_factory = AnimationFactory()
    zone_one_args = {"led_start": 0, "led_end": 6, "base_color_args": [255,0,0], "end_wait": 500}
    zone_two_args = {"led_start": 7, "led_end": 14, "base_color_args": [0,0,255], "end_wait": 500}

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        while True:
            animation_factory.render("StaticAnimation", zone_one_args)
            animation_factory.render("ClearAnimation")
            animation_factory.render("StaticAnimation", zone_two_args)
            animation_factory.render("ClearAnimation")

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
            animation_factory.render("ClearAnimation")