# Please download the json file in the attachment and use Python to add a new employee to the file's content so that the file looks like in the expected output below.

import json
with open('intermediate\company1.json', 'r+') as f:
    
    d = json.load(f)
    d['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})

    f.seek(0)
    json.dump(d, f, indent=4)