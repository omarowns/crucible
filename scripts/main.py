#!/usr/bin/env python3

import argparse
import time
from default_animations import StaticAnimation
from renderer import Renderer

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    lightsRenderer = Renderer()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        while True:
            lightsRenderer.render(StaticAnimation, 0, 6, [255,0,0])
            time.sleep(500/1000.0)
            lightsRenderer.render(StaticAnimation, 7, 13, [0,0,255])
            time.sleep(500/1000.0)

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
            lightsRenderer.clear()