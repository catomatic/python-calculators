#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import traceback
import sys

def calculate_coins(num):
    # Function to calculate amount of each coin in 
    # the change
    # Use tuples in a list so the calculation is in proper order
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
    # Loop to find out how many of each coins are in total
    # change and add them to coins_each, from largest coin
    # to smallest
    for k, v in coins:
        count = 0
        while num >= v:
            num = round(num - v, 2)
            count = count + 1
        coins_each[k] = count

    for k, v in coins_each.iteritems():
        print '{0}: {1}'.format(k, v)


def main():
    try:
        cost = abs(float(raw_input('Cost of item:\n> ')))
        total_given = abs(float(raw_input('Total amount given:\n> ')))
        change_total = total_given - cost

        print '\nCost: ${0}'.format(round(cost, 2))
        print 'Total amount given: ${0}'.format(round(total_given, 2))
        print 'Total change: ${0}\n'.format(round(change_total, 2))

        calculate_coins(change_total)

    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
