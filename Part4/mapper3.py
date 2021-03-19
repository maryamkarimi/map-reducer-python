#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # get term, doc, term_doc_count, N, and df from the line
    key, df = line.split('\t')
    term, doc, tf = key.split()

    # Set doc as the key so pairs get sorted by that key
    # This is useful to find the total number of docs in our corpus
    print '{0}\t{1} {2} {3}'.format(doc, term, tf, df)
