#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import traceback
import sys


def pct_to_dec(num):
    # Function to convert percent to decimal
    dec = num / 100
    return dec


def main():
    try:
        base_cost = abs(float(raw_input('Enter cost without tax ($):\n> ')))
        tax = abs(float(raw_input('Enter sales tax (%):\n> ')))
        total_cost = (pct_to_dec(tax) * base_cost) + base_cost

        print '\nCost before tax: ${0}'.format(base_cost)
        print 'Tax: {0}'.format(tax)
        print 'Cost after tax: ${0}\n'.format(round(total_cost, 2))
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
