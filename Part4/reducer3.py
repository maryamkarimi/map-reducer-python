#!/usr/bin/env python
"""reducer.py"""

import sys
import math

previous_file = None
current_file = None
file_count = 0
results = []


# This function prints results to stdout. The output will have the form {term, doc, tf, '\t', df}
def print_output():
    for current_term_tf_df in results:
        doc, term, tf, df = current_term_tf_df.split()
        idf = math.log10(file_count / float(df))
        print '(({0}, {1}), ({2}, {3}, {4}))'.format(doc, term, tf, idf, float(tf) * idf)


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    current_file, term_tf_df = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: term) before it is passed to the reducer
    if previous_file != current_file:
        file_count += 1
    
    # Add current value to list of results
    results.append(current_file + ' ' + term_tf_df)

    previous_file = current_file

# Print the final results
print_output()