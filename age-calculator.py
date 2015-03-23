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
    base_age = int(strftime('%Y')) - year
    bday_string = '{0} {1} {2}'.format(month, day, int(strftime('%Y')))
    day_of_year = datetime.datetime.strptime(bday_string, 
        '%m %d %Y').strftime('%j')

    if int(day_of_year) > int(strftime('%j')):
        return base_age - 1
    elif int(strftime('%j')) == int(day_of_year):
        print 'Happy Birthday!'
        return base_age
    else:
        return base_age


def usage_info():
    print 'Usage: [MM] [DD] [YYYY]'
    print 'MM: month of birth'
    print 'DD: day of birth'
    print 'YYYY: year of birth'


def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            usage_info()
        else:
            month = sys.argv[1]
            day = sys.argv[2]
            year = sys.argv[3]
            print '{0} years old.'.format(calc_age(int(month), 
                int(day), int(year)))
    except Exception:
        usage_info()
        #print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
