#!/usr/bin/python3
# 0-square_matrix_simple.py
# Edd

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
