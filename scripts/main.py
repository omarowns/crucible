#!/usr/bin/env python3

import argparse
from strip import Strip
from default_animations import DefaultAnimations
from rpi_ws281x import Color

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    strip = Strip(DefaultAnimations)

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        while True:
            print ('Color wipe animations.')
            strip.colorWipe(Color(255, 0, 0))  # Red wipe
            strip.colorWipe(Color(0, 255, 0))  # Blue wipe
            strip.colorWipe(Color(0, 0, 255))  # Green wipe
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
            strip.colorWipe(Color(0,0,0), 10)