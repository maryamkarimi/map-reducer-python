#!/usr/bin/env python
"""reducer.py"""

import sys

previous_term = None
current_term = None
current_df = 0
current_doc_tfs = []


# This function prints results to stdout. The output will have the form {term, doc, tf, '\t', df}
def print_output():
    for current_doc_tf in current_doc_tfs:
        print '{0} {1}\t{2}'.format(previous_term, current_doc_tf, current_df)


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    current_term, doc_tf = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: term) before it is passed to the reducer
    if previous_term == current_term:
        current_doc_tfs.append(doc_tf)
        current_df += 1
    else:
        if previous_term:
            print_output()
            
        current_df = 1
        current_doc_tfs = [doc_tf]
        previous_term = current_term

# do not forget to output the last term if needed!
if previous_term == current_term:
    print_output()
