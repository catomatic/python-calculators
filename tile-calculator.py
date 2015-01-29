#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import traceback
import sys


def from_ft(ft, to):
    # Function to convert from feet
    calc = {
        'in': round(ft * 12.0, 2),
        'ft': ft
    }    
    return calc[to]


def main():
    try:
        tile_cost = abs(float(raw_input('Enter cost per tile ($): ')))
        tile_width = abs(float(raw_input('Enter tile width (in): ')))
        tile_length = abs(float(raw_input('Enter tile length (in): ')))
        floor_width = abs(float(raw_input('Enter floor width (ft): ')))
        floor_length = abs(float(raw_input('Enter floor length (ft): ')))

        # Need to calculate everything based on square inches of both floor
        # and tile to get accurate results
        tile_sq = round(tile_width * tile_length, 2)
        floor_sq = round(from_ft(floor_width, 'in') * from_ft(floor_length, 'in'), 2)
        total_tile = round(floor_sq / tile_sq, 2)
        total_cost = round((floor_sq / tile_sq) * tile_cost, 2)

        print '\nTile size: {0}in x {1}in'.format(round(tile_width, 2), round(tile_length, 2))
        print 'Floor size: {0}ft x {1}ft'.format(round(floor_width, 2), round(floor_length, 2))
        print 'Total tile needed: {0}'.format(round(total_tile, 2))
        print 'Total cost: ${0}\n'.format(round(total_cost, 2))
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
