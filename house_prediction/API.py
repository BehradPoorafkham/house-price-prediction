import http.client
import json
from house_prediction.config import API_KEY
from house_prediction.decorators import timer, logging_API

@timer
@logging_API
def call_API():
    conn = http.client.HTTPSConnection("open-api.divar.ir")
    payload = json.dumps({
      "category": "apartment-sell",
      "city": "tehran",
      "districts": [
        "jeyhoun",
        "sarsabil",
        "tehran-zanjan",
        "selsebil-shomali",
        "hashemi"
        ]
      }
    )
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'X-API-Key': API_KEY
    }
    conn.request("POST", "/v2/open-platform/finder/post", payload, headers)
    res = conn.getresponse()
    datas = res.read().decode("utf-8")
    data = json.loads(datas)
    return data