#!/usr/bin/python3
# 0-square_matrix_simple.py
# Edd

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
