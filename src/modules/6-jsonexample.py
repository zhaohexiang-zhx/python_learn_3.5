#!/usr/bin/env python
# coding=utf-8

import json

python_dict = {'name': 'shuxue', u'sex': 'Male', 'c': 3, 'd': 4, 'e': 5}
# dumps
print(type(json.dumps(python_dict)))
print(json.dumps(python_dict).encode('utf-8'))

print('*'*50)

# loads
json_str = '{"name": "shuxue", "sex": "Male", "c": 3, "d": 4, "e": 5}'
print(type(json.loads(json_str)))
print(json.loads(json_str))

