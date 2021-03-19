#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into doc_term and tf
    doc_term, tf = line.split('\t')

    doc, term = doc_term.split()
    # output will be "term      doc tf"
    # Essentially changing the key of the pairs to term so the list gets sorted by term
    print '{0}\t{1} {2}'.format(term, doc, tf)
