#!/usr/bin/env python3

import ipdb

def plus_two(num):
    num=num + 2
    return num
import ipdb

def plus_two(num):
    num = num + 2
    ipdb.set_trace()  # Program will pause here, let you inspect `num`
    return num
