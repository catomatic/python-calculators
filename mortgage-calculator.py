#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import traceback
import sys


def from_year(yr, to):
    # Function to convert from years
    calc = {
        'yr': yr,
        'mon': round(yr * 12.0, 2)
    }
    return calc[to]


def find_pmt(int_rate, term_len, loan_amt):
    # Function to calculate mortgage PMT
    pmt = ((int_rate / 100 / 12) / (
        1 - (1 + int_rate / 100 / 12) ** (
            - term_len * 12))) * loan_amt
    return pmt


def main():
    try:
        int_rate = abs(float(raw_input('Enter interest rate (%):\n> ')))
        loan_amt = abs(float(raw_input('Enter loan amount ($):\n> ')))
        term_len = abs(float(raw_input('Enter term length (years):\n> ')))
        
        term_months = from_year(term_len, 'mon')
        total_loan = find_pmt(int_rate, term_len, loan_amt) * term_months

        print '\nInterest rate: {0}%'.format(int_rate)
        print 'Loan amount: ${0}'.format(loan_amt)
        print 'Term length: {0} years'.format(term_len)
        print 'Term length: {0} months'.format(term_months)
        print 'Monthly payments: ${0}'.format(round(find_pmt(int_rate, term_len, loan_amt), 2))
        print 'Total loan amount with compounded interest: ${0}\n'.format(round(total_loan, 2))
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
