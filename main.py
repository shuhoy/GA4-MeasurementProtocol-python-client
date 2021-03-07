# coding: utf-8
# editor: shuhoyo

import json
import urllib.request
from time import time


# Testing

url = 'https://www.google-analytics.com/mp/collect?measurement_id=G-XXXXXXXXXXXXXX&api_secret=YYYYYYYYYYYYYYYYYYY'


now_time = str(int(time() * 1e6))
request = {
    "client_id": "CCCCCCCCCCCCCCCCCCCC",
    "events": [{
      "name": "test_ce_1",
      "params": {"test_param_1": "200"}
      }],
    "timestamp_micros": now_time
    }
    
  

req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(request)
json_data_as_bytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(json_data_as_bytes))
result = urllib.request.urlopen(req, json_data_as_bytes)
status_code = result.status
print(result.status)
