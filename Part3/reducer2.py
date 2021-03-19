#!/usr/bin/env python
"""reducer.py"""

import sys

current_count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # convert line (currently a string) to int
    try:
        count = int(line)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # if bigram is unique
    if count == 1:
        current_count += count

# print the total number of unique bigrams
print current_count
