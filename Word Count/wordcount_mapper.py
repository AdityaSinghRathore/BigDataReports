#!/usr/bin/env python3.f
"""wordcount_mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split()

    for key in keys:
        value=1
        print("{0}\t{1}".format(last_key,running_total))    
