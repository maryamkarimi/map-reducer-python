#!/usr/bin/env python
"""reducer.py"""

import sys

current_file_word = None
current_count = 0
file_word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    file_word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_file_word == file_word:
        current_count += count
    else:
        if current_file_word:
            # write result to STDOUT
            print '(({0}), {1})'.format(current_file_word, current_count)
        current_count = count
        current_file_word = file_word

# do not forget to output the last word if needed!
if current_file_word == file_word:
    print '(({0}), {1})'.format(current_file_word, current_count)
