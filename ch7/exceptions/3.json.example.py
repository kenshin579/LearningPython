import json

json_data = 2 # try: json_data = 2, and json_data = '{{'

try:
    data = json.loads(json_data)
except (ValueError, TypeError) as e:
    print(type(e), e)
