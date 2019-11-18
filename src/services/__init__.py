import json
from flask import make_response
def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
   
