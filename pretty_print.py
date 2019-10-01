# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:22:04 2019

@author: igloo
"""


widths = [
        (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
        (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
        (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
        (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
        (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
        (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
        (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
        (120831, 1), (262141, 2), (1114109, 1),
]


def calc_len(string):
    def chr_width(o):
        global widths
        if o == 0xe or o == 0xf:
            return 0
        for num, wid in widths:
            if o <= num:
                return wid
        return 1
    return sum(chr_width(ord(c)) for c in string)


def pretty_print(push, title, date, author):
    pattern = '%3s\t%s%s%s\t%s'
    padding = ' ' * (50 - calc_len(title))
    print(pattern % (push, title, padding, date, author))

def pretty_print1(symbol):
    pattern = '%3s'
    padding = ' ' * (50 - calc_len(symbol))
    print(pattern % (symbol))

def pretty_print2(symbol, PE, symbol1, EPS):
    pattern = '%3s\t%s\t%s\t%s'
    padding = ' ' * (50 - calc_len(symbol))
    print(pattern % (symbol, PE, symbol1, EPS))
    
def pretty_print3(symbol, GAIN):
    pattern = '%3s\t%s'
    padding = ' ' * (50 - calc_len(symbol))
    print(pattern % (symbol, GAIN))