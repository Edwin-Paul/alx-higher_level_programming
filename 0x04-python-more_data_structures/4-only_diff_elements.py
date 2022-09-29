#!/usr/bin/python3
# 0-square_matrix_simple.py
# Edd

def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return (set_1 ^ set_2)
