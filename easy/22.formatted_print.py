# Create a dictionary of keys a, b, and c and their respective list of values 1 to 10, 11 to 20, and 21 to 30.

from pprint import pprint

d = {"a": list(range(1, 11)), "b": list(range(11, 21)), "c": list(range(21, 31))}

pprint(d)