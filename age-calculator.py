#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

from time import strftime
import time
import sys
import traceback
import datetime


def calc_age(month, day, year):
    # Calculate a person's age based on current month, day, year
    # Takes person's birth month, day and year as args
    base_age = int(strftime('%Y')) - year
    bday_string = '{0} {1} {2}'.format(month, day, int(strftime('%Y')))
    day_of_year = datetime.datetime.strptime(bday_string, '%m %d %Y').strftime('%j')

    if int(day_of_year) > int(strftime('%j')):
        return base_age - 1
    elif int(strftime('%j')) == int(day_of_year):
        print 'Happy Birthday!'
        return base_age
    else:
        return base_age


def main():
    try:
        month = int(raw_input('Enter month of birth (MM):\n> '))
        day = int(raw_input('Enter day of birth (DD):\n> '))
        year = int(raw_input('Enter year of birth (YYYY):\n> '))
        print '\n{0} years old.\n'.format(calc_age(month, day, year))
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
