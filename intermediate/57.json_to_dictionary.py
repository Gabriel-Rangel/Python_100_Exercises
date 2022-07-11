# Please download the file in the attachment and use Python to print out its content.

import json
from pprint import pprint

with open('intermediate\company1.json') as f:
    d = json.load(f)
    pprint(d)
