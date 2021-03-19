#!/usr/bin/env python
"""mapper.py"""

import glob
import ntpath

PATH = 'Documents'
files = glob.glob(PATH + '/*') 

for currentFile in files:
    # open current file and read line by line
    with open(currentFile) as current_file:
        for line in current_file:
            # remove leading and trailing whitespace
            line = line.strip()

            # split the line into terms
            terms = line.split()

            # increase counters
            for term in terms:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial term count is 1
                print '{0} {1}\t{2}'.format(ntpath.basename(currentFile), term, '1')
