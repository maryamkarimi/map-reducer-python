#!/usr/bin/env python
"""reducer.py"""

import sys

previous_doc_term = None
previous_doc = None

current_count = 0
doc_total_term_count = 0

# this array will have tuples of form (doc_term, count), for example, ("1.txt dog", 2)
doc_term_counts = []


# This function prints results to stdout. The output has the form {doc_term, '\t', tf}
def print_output():
    for doc_term_count in doc_term_counts:
        tf = float(doc_term_count[1]) / doc_total_term_count
        print '{0}\t{1}'.format(doc_term_count[0], tf)


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    current_doc_term, count = line.split('\t', 1)
    current_doc, term = current_doc_term.split()

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: term) before it is passed to the reducer
    if previous_doc_term == current_doc_term:
        current_count += count
    else:
        if previous_doc_term:
            doc_term_counts.append((previous_doc_term, current_count))

        if previous_doc != current_doc:
            # write result to STDOUT
            print_output()
            doc_total_term_count = 0
            doc_term_counts = []

        current_count = count
        previous_doc_term = current_doc_term
        previous_doc = current_doc

    doc_total_term_count += 1

# do not forget to output the last doc_term if needed!
if previous_doc_term == current_doc_term:
    doc_term_counts.append((previous_doc_term, current_count))

if previous_doc == current_doc:
    print_output()
