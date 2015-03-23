#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import traceback
import sys

def calculate_coins(num):
    coins = [
        ('Twenties', 20.00),
        ('Tens', 10.00),
        ('Fives', 5.00),
        ('Ones', 1.00),
        ('Quarters', .25),
        ('Dimes', .10),
        ('Nickels', .05),
        ('Pennies', .01)
    ]
    coins_each = {}
    for k, v in coins:
        count = 0
        while num >= v:
            num = round(num - v, 2)
            count = count + 1
        coins_each[k] = count

    for k, v in coins_each.iteritems():
        print '{0}: {1}'.format(k, v)


def usage_info():
    print 'Usage: [Cost of item] [Total given]'


def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            usage_info()
        else:
            cost = sys.argv[1]
            total_given = sys.argv[2]
            change_total = float(total_given) - float(cost)

            print 'Cost: ${0}'.format(round(float(cost), 2))
            print 'Total amount given: ${0}'.format(round(float(total_given), 2))
            print 'Total change: ${0}'.format(round(change_total, 2))

            calculate_coins(change_total)

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
